from google.transit import gtfs_realtime_pb2
import tripUpdated as trip
import time
import stops
import numpy as np
import json
import sys
from pprint import pprint
from datetime import datetime as dt
import requests
APIkey = '10a12f7b56a78c2111a54c380493a96b'

print sys.argv
if sys.argv[1]=='14 St' and sys.argv[2]=='116 St - Columbia University':

    single = [stops.line1Nbound['14 St'],stops.line1Nbound['116 St - Columbia University']]
    transfer = [stops.line1Nbound['96 St'],stops.line1Nbound['116 St - Columbia University']]
    start = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
    routes = ['1','2', '3']
    line = stops.line1
    # transfer_route = ['1']
    
elif sys.argv[1]=='116 St - Columbia University' and sys.argv[2]=='14 St':
    single = [stops.line1Sbound['116 St - Columbia University'],stops.line1Sbound['14 St']]
    transfer = [stops.line1Sbound['96 St'],stops.line1Sbound['14 St']]
    start = [stops.line1Sbound['116 St - Columbia University'],stops.line1Sbound['96 St']]
    routes = ['1','2','3']
    line = stops.line1
    # transfer_route = ['1']
    
    
# elif sys.argv[1]=='116 St - Columbia University' and sys.argv[2]=='14 St':
    # single = [stops.line1Sbound['116 St - Columbia University'],stops.line1Sbound['14 St']]
    # transfer = [stops.line1Sbound['96 St'],stops.line1Sbound['14 St']]
    # start = [stops.line1Sbound['116 St - Columbia University'],stops.line1Sbound['96 St']]
    # routes = ['1','2','3']
    # line = stops.line1
    # # transfer_route = ['1']
    
    
    
fastestTrip = trip.getFastestTrip(start,routes)        
# print(fastestTrip)
   
timeDiff = fastestTrip['arrivalTime']-int(time.time())
fastestTransfer = trip.getFastestTransfer(transfer,routes,timeDiff)

# print fastestTransfer
    
# fastestTripSingle = trip.getFastestTrip(single,transfer_route)
fastestTripSingle = trip.getFastestTrip(single,routes)

# print fastestTripSingle
    
if fastestTransfer['arrivalTime'] < fastestTripSingle['arrivalTime']:
    # print('Take transfer trip')
    # print(fastestTrip)
    # print(fastestTransfer)
    data = {}
    data['start']=fastestTrip
    data['transfer']=fastestTransfer

    # data['start']['trip_id']=fastestTrip[0]
    # data['start']['route_id']=fastestTrip[0][7]
    # data['start']['start_station']=start[0]
    # data['start']['departure']=fastestTrip[1]
    # data['start']['end_station']=start[1]
    # # data['start']['arrival']=

    # data['transfer']['trip_id']=fastestTransfer[0]
    # data['transfer']['route_id']=fastestTransfer[0][7]
    # data['transfer']['start_station']=transfer[0]
    # data['transfer']['departure']=fastestTransfer[1]
    # data['transfer']['arrival']=fastestTransfer[2]
    # data['transfer']['end_station']=transfer[1]


    json_data = json.dumps(data)

    pprint(json_data)
    
    
    
else:
    # print('Take single trip')
    data = {}
    data['start']=fastestTripSingle
    data['transfer']=None
    
    # data['start']['trip_id']=fastestTripSingle[0]
    # data['start']['route_id']=fastestTripSingle[0][7]
    # data['start']['start_station']=single[0]
    # data['start']['departure']=fastestTripSingle[1]
    # data['start']['end_station']=single[1]
    
    json_data = json.dumps(data)
    
    pprint(json_data)

    
    
while 1:
    time.sleep(30)
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%APIkey)
    # print response       
    feed.ParseFromString(response.content)
    
    try:
        update = trip.tripUpdate(data['start']['trip_id'], start,feed)
        
        udata = {}
        udata['start']={}
            
        udata['start']['trip_id']=update[0]
        udata['start']['departureTime']=dt.fromtimestamp(update[1]).strftime('%H:%M:%S')
        udata['start']['arrivalTime']=dt.fromtimestamp(update[2]).strftime('%H:%M:%S')
        udata['start']['current_stop_id']=line[str(update[3][:3])]
        udata['start']['current_status']=update[5]
        udata['start']['train_status']=update[6]
        udata['start']['time']=dt.fromtimestamp(update[7]).strftime('%H:%M:%S')
        
        if data['transfer']!=None:
            transfer = trip.tripUpdate(data['transfer']['trip_id'], transfer,feed)
            
            udata['transfer']={}
            udata['transfer']['trip_id']=transfer[0]
            udata['transfer']['departureTime']=dt.fromtimestamp(transfer[1]).strftime('%H:%M:%S')
            udata['transfer']['arrivalTime']=dt.fromtimestamp(transfer[2]).strftime('%H:%M:%S')
            udata['transfer']['current_stop_id']=line[str(transfer[3][:3])]
            udata['transfer']['current_status']=transfer[5]
            udata['transfer']['train_status']=transfer[6]
            udata['transfer']['time']=dt.fromtimestamp(transfer[7]).strftime('%H:%M:%S')
        
        
        
        
        pprint(udata)
    except:
        pass