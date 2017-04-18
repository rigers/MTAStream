from google.transit import gtfs_realtime_pb2
import requests
from pprint import pprint
import json
import time
import numpy as np
import stops
key = '10a12f7b56a78c2111a54c380493a96b'

# while True:

vehicleStopStatus={
    '0':'comming at',
    '1':'stopped at',
    '2':'in transit to'}

def getTripId(stationName,route,wait_time):
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%key)
    feed.ParseFromString(response.content)
    
    dictTrip = {}
    departureList = []
    time_now = time.time()
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            for stop_time_update in entity.trip_update.stop_time_update:
                # print stop_time_update.stop_id
                if stop_time_update.stop_id == stationName and entity.trip_update.trip.route_id == route:
                
                    trip_id = entity.trip_update.trip.trip_id
                    departure = int(stop_time_update.departure.time)
                    # if 30 < (departure - time.time()):
                    departure30min = abs(departure - time_now - wait_time)
                    
                    departureList.append(departure30min)
                    # print(route,departure,departure30min,trip_id)
                    # else:
                        # continue
                    
                    dictTrip[str(departure30min)]=trip_id
                    
            
    departureTime = np.min(departureList)
    trip_id = str(dictTrip[str(departureTime)])
    
    # pprint(dictTrip)
    # pprint(departureTime)
    # pprint(trip_id)
    return (trip_id)
    # return (trip_id,departureTime)

    
def getTransferTripId(stationName,route,wait_time):
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%key)
    feed.ParseFromString(response.content)
    
    dictTrip = {}
    departureList = []
    time_now = time.time()
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            for stop_time_update in entity.trip_update.stop_time_update:
                # print stop_time_update.stop_id
                if stop_time_update.stop_id == stationName and entity.trip_update.trip.route_id == route:
                
                    trip_id = entity.trip_update.trip.trip_id
                    departure = int(stop_time_update.departure.time)
                    # if 30 < (departure - time.time()):
                    departure30min = departure - time_now - wait_time
                    if departure30min > 0:
                        departureList.append(departure30min)
                        # print(route,departure,departure30min,trip_id)
                    # else:
                        # continue
                    
                        dictTrip[str(departure30min)]=trip_id
                    
            
    departureTime = np.min(departureList)
    trip_id = str(dictTrip[str(departureTime)])
    
    # pprint(dictTrip)
    # pprint(departureTime)
    # pprint(trip_id)
    return (trip_id)
    # return (trip_id,departureTime)
    
def getTripStatus(trip_id,startStationName, endStationName):
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%key)
    feed.ParseFromString(response.content)
    departureTime=None
    arrivalTime=None
    current_stop_sequence=None
    current_status=None
    timestamp = None
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            if entity.trip_update.trip.trip_id == trip_id:
                for stop_time_update in entity.trip_update.stop_time_update:
                    if stop_time_update.stop_id == startStationName:
                        departureTime = int(stop_time_update.departure.time)
                        # print entity
                    
                    if stop_time_update.stop_id == endStationName:
                        arrivalTime = int(stop_time_update.arrival.time)
                        # print stop_time_update
                    
        if entity.HasField('vehicle'):
            if entity.vehicle.trip.trip_id == trip_id:
                current_stop_sequence = int(entity.vehicle.current_stop_sequence)
                current_status = str(entity.vehicle.current_status)
                timestamp = int(entity.vehicle.timestamp)
        
        if entity.HasField('alert'):
			for informed_entity in entity.alert.informed_entity:
				if informed_entity.trip.trip_id == trip_id:
					file.write(str(entity.alert.informed_entity))
					if entity.alert.HasField('header_text'):
						file.write(str(entity.alert.header_text))
        
    return(departureTime,arrivalTime,current_stop_sequence,current_status,timestamp)   

def getFastestTrip(stationNames,routes):       
    start_stop_id = stationNames[0]
    end_stop_id = stationNames[1]
    
    trip_ids = []
    for route in routes:
        trip_ids.append(getTripId(start_stop_id, route, 900))
    
    arrivalTimes = {}
    for trip_id in trip_ids:
        trip_data = getTripStatus(trip_id, start_stop_id, end_stop_id)
        # print (trip_id,trip_data)
        departureTime = trip_data[0]
        arrivalTime = trip_data[1]
        currentStop = trip_data[2]
        currentStatus = trip_data[3]
        vehicleTime = trip_data[4]
            
        if currentStop != None:
            # currentStopName = L.stationNames[len(L.stationNames)-currentStop]
            currentStopName = stops.line1Seq[len(stops.line1Seq)-currentStop]

        if departureTime == None:
            arrivalMinutes = ((arrivalTime)-int(time.time()))/60
            arrivalTimes[trip_id] = arrivalTime
            
        else:
            departMinutes = ((departureTime)-int(time.time()))/60
            try:
                arrivalMinutes = ((arrivalTime)-int(time.time()))/60
                arrivalTimes[trip_id] = arrivalTime
            except:
                print('No arrival information avaialble')
            


    tempTimes = []
    for key in arrivalTimes:
        tempTimes.append(arrivalTimes[key])
    leastTime = np.min(tempTimes)
    for key in arrivalTimes:
        if arrivalTimes[key] == leastTime:
            trip_id_leastTime = key
    return(trip_id_leastTime,arrivalTimes[trip_id_leastTime])
    
    
def getFastestTransfer(stationNames,route,timeDiff):
  
    start_stop_id = stationNames[0]
    end_stop_id = stationNames[1]

    trip_id = getTransferTripId(start_stop_id, route, timeDiff)

    arrivalTimes = {}

    trip_data = getTripStatus(trip_id, start_stop_id, end_stop_id)
    departureTime = trip_data[0]
    arrivalTime = trip_data[1]
    currentStop = trip_data[2]
    currentStatus = trip_data[3]
    vehicleTime = trip_data[4]
        
    if currentStop != None:
        # currentStopName = L.stationNames[len(L.stationNames)-currentStop]
        currentStopName = stops.line1Seq[len(stops.line1Seq)-currentStop]



    if departureTime == None:
        arrivalMinutes = ((arrivalTime)-int(time.time()))/60
        arrivalTimes[trip_id] = arrivalTime

    else:
        departMinutes = ((departureTime)-int(time.time()))/60
        try:
            arrivalMinutes = ((arrivalTime)-int(time.time()))/60
            arrivalTimes[trip_id] = arrivalTime
        except:
            print('No arrival information avaialble')
            
    return(trip_id,departureTime,arrivalTime)


