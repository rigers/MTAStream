from google.transit import gtfs_realtime_pb2
import requests
from pprint import pprint
import json
import time
import numpy as np
import stops
APIkey = '10a12f7b56a78c2111a54c380493a96b'

# while True:

vehicleStopStatus={
    '0':'comming at',
    '1':'stopped at',
    '2':'in transit to',
    None:None}

def getTripId(stationName,route,wait_time,feed):
    
        
    dictTrip = {}
    departureList = []
    time_now = time.time()
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            for stop_time_update in entity.trip_update.stop_time_update:
                
                if stop_time_update.stop_id == stationName and entity.trip_update.trip.route_id == route:
                    
                    trip_id = entity.trip_update.trip.trip_id
                    departure = int(stop_time_update.departure.time)
                    # print departure
                    # if 30 < (departure - time.time()):
                    departure30min = abs(departure - time_now - wait_time)
                    # print departure30min
                    departureList.append(departure30min)
                    # print(route,departure,departure30min,trip_id)
                    # else:
                        # continue
                    
                    dictTrip[str(departure30min)]=trip_id
                    
    # print departureList
    try:
        departureTime = np.min(departureList)
        trip_id = str(dictTrip[str(departureTime)])
    except:
        trip_id = None
    # pprint(dictTrip)
    # pprint(departureTime)
    # pprint(trip_id)
    return (trip_id)
    # return (trip_id,departureTime)

    
def getTransferTripId(stationName,route,wait_time, feed):
    # feed = gtfs_realtime_pb2.FeedMessage()
    # response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%key)
    # feed.ParseFromString(response.content)
    
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
                    
    try:
        departureTime = np.min(departureList)
        trip_id = str(dictTrip[str(departureTime)])
    except:
        trip_id = None
    # pprint(dictTrip)
    # pprint(departureTime)
    # pprint(trip_id)
    return (trip_id)
    # return (trip_id,departureTime)
    
def getTripStatus(trip_id,startStationName, endStationName, feed):
    # feed = gtfs_realtime_pb2.FeedMessage()
    # response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%key)
    # feed.ParseFromString(response.content)
    departureTime=None
    arrivalTime=None
    current_stop_sequence=None
    current_status=None
    timestamp = None
    current_stop_id=None
    train_status = None
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            if entity.trip_update.trip.trip_id == trip_id:
                for stop_time_update in entity.trip_update.stop_time_update:
                    if stop_time_update.stop_id == startStationName:
                        departureTime = int(stop_time_update.departure.time)
                        # pprint(trip_id)
                        # pprint(entity)
                    
                    if stop_time_update.stop_id == endStationName:
                        arrivalTime = int(stop_time_update.arrival.time)
                        # pprint(trip_id)
                        # pprint(entity)
            
                
        if entity.HasField('vehicle'):
            if entity.vehicle.trip.trip_id == trip_id:
                current_stop_sequence = int(entity.vehicle.current_stop_sequence)
                current_status = str(entity.vehicle.current_status)
                timestamp = int(entity.vehicle.timestamp)
                current_stop_id = entity.vehicle.stop_id
        
        if entity.HasField('alert'):
			for informed_entity in entity.alert.informed_entity:
				if informed_entity.trip.trip_id == trip_id:
					# file.write(str(entity.alert.informed_entity))
					if entity.alert.HasField('header_text'):
						# file.write(str(entity.alert.header_text))
                        			train_status = entity.alert.header_text.translation[0].text
                        			# print(train_status)
                        			# print(entity.alert.header_text)
                        # print(entity.alert.header_text.translation[0].text)
                        
                        
        # if entity.HasField('alert'):
            # alt_route = []
            # alt_status = []
            # # try:
            # for trip in entity.alert.informed_entity:
                
                # try:
                    # alt_route.append(trip.trip.route_id)
                # except:
                    # alt_route.append('NA')
            # # except:
                # # pass
                
            # try:
                # for text in entity.alert.header_text.translation:
                    # # print text.text
                    # try:
                        # alt_status.append(text.text)
                    # except:
                        # alt_status.append('NA')
            # except:
                # pass
                            

        
    return(departureTime,arrivalTime,current_stop_id,current_stop_sequence,current_status,train_status,timestamp)   

def getFastestTrip(stationNames,routes):
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%APIkey)
    # print response.content       
    feed.ParseFromString(response.content)
    
    start_stop_id = stationNames[0]
    end_stop_id = stationNames[1]
    
    trip_ids = {}
    for route in routes:
        trip_id = getTripId(start_stop_id, route, 900, feed)
        if trip_id != None:
            trip_ids[trip_id] = {}
    # pprint(trip_ids.keys())
    
    arrivalTimes = {}
    for key in trip_ids.keys():
        trip_data = getTripStatus(key, start_stop_id, end_stop_id, feed)
        # print(key)
        # departureTime = trip_data[0]
        # arrivalTime = trip_data[1]
        # currentStop = trip_data[2]
        # currentStatus = trip_data[3]
        # vehicleTime = trip_data[4]
        
        trip_ids[key]['departureTime'] = trip_data[0]
        trip_ids[key]['arrivalTime'] = trip_data[1]
        trip_ids[key]['currentStopId'] = trip_data[2]
        trip_ids[key]['currentStopSequence'] = trip_data[3]
        trip_ids[key]['currentStatus'] = vehicleStopStatus[trip_data[4]]
        trip_ids[key]['train_status'] = trip_data[5]
        trip_ids[key]['vehicleTime'] = trip_data[6]
        trip_ids[key]['trip_id'] = key
        
        
        # pprint(trip_ids[key])
            
        if trip_ids[key]['currentStopSequence'] != None:
            # currentStopName = L.stationNames[len(L.stationNames)-currentStop]
            currentStopName = stops.line1Seq[len(stops.line1Seq)-trip_ids[key]['currentStopSequence']]

        if trip_ids[key]['departureTime'] == None:
            arrivalMinutes = ((trip_ids[key]['arrivalTime'])-int(time.time()))/60
            arrivalTimes[key] = trip_ids[key]['arrivalTime']
            
        else:
            departMinutes = ((trip_ids[key]['departureTime'])-int(time.time()))/60
            try:
                arrivalMinutes = ((trip_ids[key]['arrivalTime'])-int(time.time()))/60
                arrivalTimes[key] = trip_ids[key]['arrivalTime']
            except:
                print('No arrival information avaialble')
            
    # pprint(trip_ids)

    tempTimes = []
    for key in arrivalTimes:
        tempTimes.append(arrivalTimes[key])
    leastTime = np.min(tempTimes)
    for key in arrivalTimes:
        if arrivalTimes[key] == leastTime:
            trip_id_leastTime = key
    return(trip_ids[trip_id_leastTime])
    
    
def getFastestTransfer(stationNames,routes,timeDiff):
    
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%APIkey)
    # print response       
    feed.ParseFromString(response.content)
    
    
    start_stop_id = stationNames[0]
    end_stop_id = stationNames[1]
    
    trip_ids = {}
    for route in routes:
        trip_id = getTransferTripId(start_stop_id, route, timeDiff, feed)
        if trip_id != None:
            trip_ids[trip_id] = {}
    pprint(trip_ids.keys())
    
    arrivalTimes = {}
    for key in trip_ids.keys():
    
        trip_data = getTripStatus(key, start_stop_id, end_stop_id, feed)
        # print(trip_id,trip_data)
        # departureTime = trip_data[0]
        # arrivalTime = trip_data[1]
        # currentStop = trip_data[2]
        # currentStatus = trip_data[3]
        # vehicleTime = trip_data[4]
        
        trip_ids[key]['departureTime'] = trip_data[0]
        trip_ids[key]['arrivalTime'] = trip_data[1]
        trip_ids[key]['currentStopId'] = trip_data[2]
        trip_ids[key]['currentStopSequence'] = trip_data[3]
        trip_ids[key]['currentStatus'] = vehicleStopStatus[trip_data[4]]
        trip_ids[key]['train_status'] = trip_data[5]
        trip_ids[key]['vehicleTime'] = trip_data[5]
        trip_ids[key]['trip_id'] = key
        
        # pprint(trip_ids[key])
            
        if trip_ids[key]['currentStopSequence'] != None:
            # currentStopName = L.stationNames[len(L.stationNames)-currentStop]
            currentStopName = stops.line1Seq[len(stops.line1Seq)-trip_ids[key]['currentStopSequence']]

        if trip_ids[key]['departureTime'] == None:
            arrivalMinutes = ((trip_ids[key]['arrivalTime'])-int(time.time()))/60
            arrivalTimes[key] = trip_ids[key]['arrivalTime']
            
        else:
            departMinutes = ((trip_ids[key]['departureTime'])-int(time.time()))/60
            try:
                arrivalMinutes = ((trip_ids[key]['arrivalTime'])-int(time.time()))/60
                arrivalTimes[key] = trip_ids[key]['arrivalTime']
            except:
                print('No arrival information avaialble.')
            
    # pprint(trip_ids)

    tempTimes = []
    for key in arrivalTimes:
        tempTimes.append(arrivalTimes[key])
    leastTime = np.min(tempTimes)
    for key in arrivalTimes:
        if arrivalTimes[key] == leastTime:
            trip_id_leastTime = key
    return(trip_ids[trip_id_leastTime])
    
    
    
def tripUpdate(trip_id,stationNames):   
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1'%APIkey)
    # print response       
    feed.ParseFromString(response.content)
    
    
    startStationName = stationNames[0]
    endStationName = stationNames[1]
    
    departureTime=None
    arrivalTime=None
    current_stop_sequence=None
    current_status=None
    timestamp = None
    current_stop_id=None
    train_status = None
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            if entity.trip_update.trip.trip_id == trip_id:
                for stop_time_update in entity.trip_update.stop_time_update:
                    if stop_time_update.stop_id == startStationName:
                        departureTime = int(stop_time_update.departure.time)
                        # pprint(trip_id)
                        # pprint(entity)
                    
                    if stop_time_update.stop_id == endStationName:
                        arrivalTime = int(stop_time_update.arrival.time)
                        # pprint(trip_id)
                        # pprint(entity)
            
                
        if entity.HasField('vehicle'):
            if entity.vehicle.trip.trip_id == trip_id:
                current_stop_sequence = int(entity.vehicle.current_stop_sequence)
                current_status = str(entity.vehicle.current_status)
                timestamp = int(entity.vehicle.timestamp)
                current_stop_id = entity.vehicle.stop_id
        
        if entity.HasField('alert'):
			for informed_entity in entity.alert.informed_entity:
				if informed_entity.trip.trip_id == trip_id:
					# file.write(str(entity.alert.informed_entity))
					if entity.alert.HasField('header_text'):
						# file.write(str(entity.alert.header_text))
                        			train_status = entity.alert.header_text.translation[0].text
                        			# print(train_status)
                        			# print(entity.alert.header_text)
                        # print(entity.alert.header_text.translation[0].text)
                        
        
    return(departureTime,arrivalTime,current_stop_id,current_stop_sequence,current_status,train_status,timestamp)
    
    
    
    
    
    
    
    
    
    
    # trip_id = getTransferTripId(start_stop_id, route, timeDiff, feed)
    
    # print trip_id
    
    # trip[trip_id] = {}
    # arrivalTimes = {}

    # trip_data = getTripStatus(trip_id, start_stop_id, end_stop_id, feed)
    # # departureTime = trip_data[0]
    # # arrivalTime = trip_data[1]
    # # currentStop = trip_data[2]
    # # currentStatus = trip_data[3]
    # # vehicleTime = trip_data[4]
    
    # trip[trip_id]['departureTime'] = trip_data[0]
    # trip[trip_id]['arrivalTime'] = trip_data[1]
    # trip[trip_id]['currentStopId'] = trip_data[2]
    # trip[trip_id]['currentStopSequence'] = trip_data[3]
    # trip[trip_id]['currentStatus'] = vehicleStopStatus[trip_data[4]]
    # trip[trip_id]['vehicleTime'] = trip_data[5]
    # trip[trip_id]['trip_id'] = trip_id
    
    
    
    
    # if trip[trip_id]['currentStopSequence'] != None:
        # # currentStopName = L.stationNames[len(L.stationNames)-currentStop]
        # currentStopName = stops.line1Seq[len(stops.line1Seq)-trip[trip_id]['currentStopSequence']]



    # if trip[trip_id]['departureTime'] == None:
        # arrivalMinutes = ((trip[trip_id]['arrivalTime'])-int(time.time()))/60
        # arrivalTimes[trip_id] = trip[trip_id]['arrivalTime']

    # else:
        # departMinutes = ((trip[trip_id]['departureTime'])-int(time.time()))/60
        # try:
            # arrivalMinutes = ((trip[trip_id]['arrivalTime'])-int(time.time()))/60
            # arrivalTimes[trip_id] = trip[trip_id]['arrivalTime']
        # except:
            # print('No arrival information avaialble')
    
    # # print trip
    
    # return(trip[trip_id])


