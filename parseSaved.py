import os
from pprint import pprint
from google.transit import gtfs_realtime_pb2
from google.protobuf import text_format
import csv

with open('aggregate.csv', 'ab') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for file in os.listdir("F:\\mta_gtfs\\"):
        if file.endswith("_123456.json"):
            file = "F:\\mta_gtfs\\%s"%file
            print file
            with open(file,'r') as myfile:
                data = myfile.read()
                # print data
                feed = gtfs_realtime_pb2.FeedMessage()
                # pprint(dir(feed))
                text_format.Merge(data,feed)
                
                for entity in feed.entity:
                    timestamp = feed.header.timestamp
                    
                    if entity.HasField('vehicle'):
                        try:
                            veh_route = entity.vehicle.trip.route_id
                        except:
                            veh_route = 'NA'
                        try:
                            veh_status = entity.vehicle.current_status
                        except:
                            veh_status = 'NA'
                        
                        try:
                            veh_time = entity.vehicle.timestamp
                        except:
                            veh_time = 'NA'
                        
                        spamwriter.writerow([timestamp,'vehicle',veh_route, veh_status, veh_time])
                    
                    if entity.HasField('alert'):
                        # print entity.alert.header_text.translation
                        alt_route = []
                        alt_status = []
                        # try:
                        for trip in entity.alert.informed_entity:
                            
                            try:
                                alt_route.append(trip.trip.route_id)
                            except:
                                alt_route.append('NA')
                        # except:
                            # pass
                            
                        try:
                            for text in entity.alert.header_text.translation:
                                # print text.text
                                try:
                                    alt_status.append(text.text)
                                except:
                                    alt_status.append('NA')
                        except:
                            pass
                            
                        for i in range(0,len(alt_route)):
                            spamwriter.writerow([timestamp,'alert',alt_route[i], alt_status])
            os.rename(file,"F:\\mta_gtfs\\parsed\\%s"%file[11:])
        

# with open('eggs.csv', 'wb') as csvfile:
    # spamwriter = csv.writer(csvfile, delimiter=' ',
                            # quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
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
    