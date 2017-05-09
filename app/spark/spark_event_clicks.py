from pyspark import SparkContext
import itertools
import MySQLdb

# Set up SparkContext
sc = SparkContext("spark://spark-master:7077", "PopularItems")

# Read in data from event_clicks.log
data = sc.textFile("/tmp/data/logs/event_clicks.log", 2)

# line => (user_id, event_id)
pairs = data.map(lambda line: line.split("\t"))

# (user_id, event_id) => (user_id, list of event_ids)
user_to_events = pairs.groupByKey()

# (user_id, list of event_ids) => (user_id, (event_id1, event_id2))
user_to_event_tuple = user_to_events.flatMap(lambda x: [(x[0], y) for y in itertools.combinations(x[1], 2)]).distinct()

# (user_id, (event_id1, event_id2)) => ((event_id1, event_id2), user_id)
event_tuple_to_user = user_to_event_tuple.map(lambda x: (x[1], x[0]))

# filter out where where event_id1 == event_id2
event_tuple_to_user = event_tuple_to_user.filter(lambda x: x[0][0] != x[0][1])

# ((event_id1, event_id2), user_id) => ((event_id1, event_id2), len(list of user_ids))
event_tuple_to_user_count = event_tuple_to_user.groupByKey().mapValues(len)

# filter out where user_id count is < 3
filtered_event_tuple_to_user_count = event_tuple_to_user_count.filter(lambda x: x[1] > 2)

# ((event_id1, event_id2), len(list of user_ids)) => (event_id1, list of corresponding event_id2 for recommendations)
event_to_reco_events = filtered_event_tuple_to_user_count.map(lambda x: x[0]).groupByKey()

output = event_to_reco_events.collect()

# End SparkContext
sc.stop()

# Open database connection
db = MySQLdb.connect("db", "root", "$3cureUS", "cs4501")

# Set up SQL db cursor
cursor = db.cursor()

# Get version to db to test connection
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)

# Insert event recommendation item query
insert_query = "INSERT INTO services_eventrecommendation (event_id, recommended_events) VALUES (%s, %s);"

truncate_query = "TRUNCATE TABLE services_eventrecommendation;"
cursor.execute(truncate_query)

for event_id, event_list in output:

    # Print output
    print("event_id: %s" % event_id)
    reco_list = ",".join(event_list)
    print("reco_list %s" % reco_list)

    # Insert recommendation item into db
    try:
        cursor.execute(insert_query, (event_id, reco_list))
        db.commit()
    except:
        db.rollback()

# Disconnect from server
db.close()