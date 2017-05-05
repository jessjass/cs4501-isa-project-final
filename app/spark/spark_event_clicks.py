from pyspark import SparkContext
import itertools

# Set up SparkContext
sc = SparkContext("spark://spark-master:7077", "PopularItems")

# Read in data from event_clicks.log
data = sc.textFile("/tmp/data/logs/event_clicks.log", 2)

# line => (user_id, event_id)
pairs = data.map(lambda line: line.split("\t"))

# output = pairs.collect()
# for pair in output:
#     print("user_id: %s  event_id: %s" % (pair[0], pair[1]))
# print("END: Read (user_id, event_id) pairs")

# (user_id, event_id) => (user_id, list of event_ids)
user_to_events = pairs.groupByKey()

# output = user_to_events.collect()
# for user_id, events in output:
#     print("user_id: %s" % user_id)
#     for e in events:
#         print(" - event_id: %s" % e)
# print("END: (user_id, event_id) => (user_id, list of event_ids)")

user_to_event_tuple = user_to_events.flatMap(lambda x: [(x[0], y) for y in itertools.combinations(x[1], 2)]).distinct()

# output = user_to_event_tuple.collect()
# for user_id, event_tuple in output:
#     print("user_id: %s  event_id: (%s, %s)" % (user_id, event_tuple[0], event_tuple[1]))
# print("END: (user_id, list of event_ids) => (user_id, (event_id1, event_id2))")

event_tuple_to_user = user_to_event_tuple.map(lambda x: (x[1], x[0]))

# output = event_tuple_to_user.collect()
# for event_tuple, user_id in output:
#     print("event_id: (%s, %s)   user_id: %s" % (event_tuple[0], event_tuple[1], user_id))
# print("END: (user_id, (event_id1, event_id2)) => ((event_id1, event_id2), user_id)")

event_tuple_to_user_count = event_tuple_to_user.groupByKey().mapValues(len)

# output = event_tuple_to_user_count.collect()
# for event_tuple, user_count in output:
#     print("event_id: (%s, %s)   user_count: %d" % (event_tuple[0], event_tuple[1], user_count))
#
# print("END: ((event_id1, event_id2), user_id) => ((event_id1, event_id2), user_count)")

filtered_event_tuple_to_user_count = event_tuple_to_user_count.filter(lambda x: x[1] > 2)

# output = filtered_event_tuple_to_user_count.collect()
# for event_tuple, user_count in output:
#     print("event_id: (%s, %s)   user_count: %d" % (event_tuple[0], event_tuple[1], user_count))
# print("END: ((event_id1, event_id2), user_id) => ((event_id1, event_id2), user_count)")

event_to_reco_events = filtered_event_tuple_to_user_count.map(lambda x: x[0]).groupByKey()

output = event_to_reco_events.collect()

for event_id, event_list in output:
    print("event_id: %s" % event_id)
    for e in event_list:
        print( " - reco event_id: %s" % e)


# End SparkContext
sc.stop()