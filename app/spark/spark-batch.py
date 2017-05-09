from kafka import KafkaConsumer
import json


while True:
    try:
        # Set up KafkaConsumer to build log file when a user clicks an event
        event_click_consumer = KafkaConsumer('event_clicks', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])

    except:
        problem = "Node not ready error"

    else:

        # Log each event click in events_click.log
        for message in event_click_consumer:
            new_event_click = json.loads(message.value.decode('utf-8'))
            log_item = "{0}\t{1}\n".format(new_event_click['user_id'], new_event_click['event_id'])
            with open("logs/event_clicks.log", "a") as logfile:
                logfile.write(log_item)