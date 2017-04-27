# import L_stops as L
import tripUpdated as trip
import time
import stops
import numpy as np
import json
import sys
from pprint import pprint
# import datetime.datetime as dt


if sys.argv[1]=='14 St' and sys.argv[2]=='116 St - Columbia University':

    single = [stops.line1Nbound['14 St'],stops.line1Nbound['116 St - Columbia University']]
    transfer = [stops.line1Nbound['96 St'],stops.line1Nbound['116 St - Columbia University']]
    start = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
    routes = ['1','2', '3']
    # transfer_route = ['1']
    
elif sys.argv[1]=='116 St - Columbia University' and sys.argv[2]=='14 St':
    single = [stops.line1Sbound['116 St - Columbia University'],stops.line1Sbound['14 St']]
    transfer = [stops.line1Sbound['96 St'],stops.line1Sbound['14 St']]
    start = [stops.line1Sbound['116 St - Columbia University'],stops.line1Sbound['96 St']]
    routes = ['1','2','3']
    # transfer_route = ['1']
    
    
    
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
    # data['transfer']={}
    
    # data['start']['trip_id']=fastestTripSingle[0]
    # data['start']['route_id']=fastestTripSingle[0][7]
    # data['start']['start_station']=single[0]
    # data['start']['departure']=fastestTripSingle[1]
    # data['start']['end_station']=single[1]
    
    json_data = json.dumps(data)
    
    print json_data
    