import os
from pprint import pprint
from google.transit import gtfs_realtime_pb2
from google.protobuf import text_format
import csv

with open('aggregateCount.csv', 'ab') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for file in os.listdir("F:\\mta_gtfs\\parsed"):
    # for file in os.listdir("C:\\Users\\Rigers\\Documents\\MTAStream"):
        if file.endswith("_123456.json"):
            file = "F:\\mta_gtfs\\parsed\\%s"%file
            # file = "C:\\Users\\Rigers\\Documents\\MTAStream\\%s"%file
            print file
            with open(file,'r') as myfile:
                data = myfile.read()
                # print data
                feed = gtfs_realtime_pb2.FeedMessage()
                # pprint(dir(feed))
                text_format.Merge(data,feed)
                count1=0
                count2=0
                count3=0
                count4=0
                count5=0
                count6=0
                alert = False
                for entity in feed.entity:
                    timestamp = feed.header.timestamp
                    
                    if entity.HasField('trip_update'):
                    
                        if entity.trip_update.trip.route_id == '1':
                            count1+=1
                        if entity.trip_update.trip.route_id == '2':
                            count2+=1
                        if entity.trip_update.trip.route_id == '3':
                            count3+=1    
                        if entity.trip_update.trip.route_id == '4':
                            count4+=1
                        if entity.trip_update.trip.route_id == '5':
                            count5+=1    
                        if entity.trip_update.trip.route_id == '6':
                            count6+=1    
                            
                            
                        # spamwriter.writerow([timestamp,'vehicle',veh_route, veh_status, veh_time])
                    
                    if entity.HasField('alert'):
                        # print entity.alert.header_text.translation
                        alert=True
                        try:
                            for trip in entity.alert.informed_entity:
                                if trip.trip.route_id == '1':
                                    trip_id = trip.trip.trip_id
                                    spamwriter.writerow([timestamp,'1','alert',trip_id, count1])
                                if trip.trip.route_id == '2':
                                    trip_id = trip.trip.trip_id
                                    spamwriter.writerow([timestamp,'2','alert',trip_id, count2])
                                if trip.trip.route_id == '3':
                                    trip_id = trip.trip.trip_id
                                    spamwriter.writerow([timestamp,'3','alert',trip_id, count3])
                                if trip.trip.route_id == '4':
                                    trip_id = trip.trip.trip_id
                                    spamwriter.writerow([timestamp,'4','alert',trip_id, count4])
                                if trip.trip.route_id == '5':
                                    trip_id = trip.trip.trip_id
                                    spamwriter.writerow([timestamp,'5','alert',trip_id, count5])
                                if trip.trip.route_id == '6':
                                    trip_id = trip.trip.trip_id
                                    spamwriter.writerow([timestamp,'6','alert',trip_id, count6])
                        except:
                            pass
                            
                if alert==True:
                    pass
                else:
                    spamwriter.writerow([timestamp,'1','alert',0, count1])
                    spamwriter.writerow([timestamp,'2','alert',0, count2])
                    spamwriter.writerow([timestamp,'3','alert',0, count3])
                    spamwriter.writerow([timestamp,'4','alert',0, count4])
                    spamwriter.writerow([timestamp,'5','alert',0, count5])
                    spamwriter.writerow([timestamp,'6','alert',0, count6])
                        # try:
                            # for text in entity.alert.header_text.translation:
                                # # print text.text
                                # try:
                                    # alt_status.append(text.text)
                                # except:
                                    # alt_status.append('NA')
                        # except:
                            # pass
                            
                        # for i in range(0,len(alt_route)):
                            # spamwriter.writerow([timestamp,'alert',alt_route[i], alt_status])
            # os.rename(file,"F:\\mta_gtfs\\parsed\\%s"%file[11:])

            
# with open('aggregate.csv', 'rb') as csvfile, open('aggregateFiltered.csv','wb') as out:
    # spamwriter = csv.writer(out, delimiter=',')        
    # for row in csv.reader(csvfile):
        # if row[2] == '1' or row[2] == '2' or row[2] == '3' or row[2] == '4' or row[2] == '5' or row[2] == '6':
            # if row[1] == 'alert':
                # spamwriter.writerow(row)
            
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
    