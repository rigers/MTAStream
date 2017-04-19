import os
from pprint import pprint
from google.transit import gtfs_realtime_pb2
from google.protobuf import text_format

for file in os.listdir("F:\\Documents\\Github\\MTAStream\\"):
    if file.endswith("_123456.json"):
        with open(file,'r') as myfile:
            data = myfile.read()
            # print data
            feed = gtfs_realtime_pb2.FeedMessage()
            # pprint(dir(feed))
            text_format.Merge(data,feed)
            
            pprint(feed.entity)
        
        
# from google.transit import gtfs_realtime_pb2
# import requests
# from pprint import pprint
# import json
# import time
# import numpy as np
# import stops
# key = '10a12f7b56a78c2111a54c380493a96b'

# # while True:

# vehicleStopStatus={
    # '0':'comming at',
    # '1':'stopped at',
    # '2':'in transit to'}


# feed = gtfs_realtime_pb2.FeedMessage()
# response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%key)

# feed.ParseFromString(response.content)

# pprint(feed)
    