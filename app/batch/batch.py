from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json


while True:
    try:
        consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
    except:
        problem = "node not ready error"
    else:
        for message in consumer:
            newListing = json.loads((message.value).decode('utf-8'))
            # try:
            #     es = Elasticsearch(['es'])
            #     es.index(index='listing_index', doc_type='listing', id=some_new_listing['id'], body=some_new_listing)