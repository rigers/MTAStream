import L_stops as L
import tripUpdated as trip
import time
import stops
import numpy as np
import json
# import datetime.datetime as dt


L114to1116 = [stops.line1Nbound['14 St'],stops.line1Nbound['116 St - Columbia University']]
L196to1116 = [stops.line1Nbound['96 St'],stops.line1Nbound['116 St - Columbia University']]

L114to196 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
# L214to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
# L314to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]

routes = ['1','2','3']

fastestTrip = trip.getFastestTrip(L114to196,routes)        
print(fastestTrip)
   
# timeDiff = fastestTrip[1]-int(time.time())
# fastestTransfer = trip.getFastestTransfer(L196to1116,'1',timeDiff)

# print fastestTransfer
    
# fastestTripSingle = trip.getFastestTrip(L114to1116,['1'])

# print fastestTripSingle
    
# if fastestTransfer[2] < fastestTripSingle[1]:
    # print('Take transfer trip')
    # print(fastestTrip)
    # print(fastestTransfer)
    # data = {}
    # data['start']={}
    # data['transfer']={}
    
    # data['start']['trip_id']=fastestTrip[0]
    # data['start']['route_id']=fastestTrip[0][7]
    # data['start']['start_station']=L114to196[0]
    # data['start']['departure']=fastestTrip[1]
    # data['start']['end_station']=L114to196[1]
    # # data['start']['arrival']=
    
    # data['transfer']['trip_id']=fastestTransfer[0]
    # data['transfer']['route_id']=fastestTransfer[0][7]
    # data['transfer']['start_station']=L196to1116[0]
    # data['transfer']['departure']=fastestTransfer[1]
    # data['transfer']['arrival']=fastestTransfer[2]
    # data['transfer']['end_station']=L196to1116[1]
    
    
    # json_data = json.dumps(data)
    
    # print json_data
    
    
    
# else:
    # print('Take single trip')
    # data = {}
    # data['start']={}
    # data['transfer']={}
    
    # data['start']['trip_id']=fastestTripSingle[0]
    # data['start']['route_id']=fastestTripSingle[0][7]
    # data['start']['start_station']=L114to1116[0]
    # data['start']['departure']=fastestTripSingle[1]
    # data['start']['end_station']=L114to1116[1]
    
    # json_data = json.dumps(data)
    
    # print json_data
    