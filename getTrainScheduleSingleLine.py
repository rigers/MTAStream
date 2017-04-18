import L_stops as L
import trip
import time
import stops
# import datetime.datetime as dt

south = 0
north = 1

#Choose only specific trains
#14st to Columbia Via the 1 train
#14st to columbia via 2 or 3 train to Columbia (transfer to 1)


vehicleStopStatus={
    '0':'comming at',
    '1':'stopped at',
    '2':'in transit to'}

L114to116 = [stops.line1Nbound['14 St'],stops.line1Nbound['116 St - Columbia University']]
L196to116 = [stops.line1Nbound['96 St'],stops.line1Nbound['116 St - Columbia University']]

L114to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
L214to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
L314to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]

routes = ['1','2','3']

# for i in range(0,len(stops.line1Seq)):
    # print('%s : %s'%(i,stops.line1Seq[i]))

# startStation = None
    
# while startStation == None:
    # try:
        # startIndex = int(raw_input("Enter starting station: "))
        # # startStation = L.stationNames[startIndex]
        # # startStation = stops.line1Seq[startIndex]
        
    # except:
        # print 'Please enter a valid station name'
        # startStation = None

# endStation = None        
# while endStation == None:
    # try:
        # endIndex = int(raw_input("Enter destination: "))
        # # endStation = L.stationNames[startIndex]
        # # endStation = stops.line1Seq[endIndex]
        
    # except:
        # print 'Please enter a valid station name'
        # startStation = None
startStation = L114to96[0]
endStation = L114to96[1]
   
        
# if startIndex < endIndex:
    # direction = south
# elif startIndex > endIndex:
    # direction = north
# else:
    # print "You're already there!"
    
start_stop_id = startStation
end_stop_id = endStation
    
# if direction == north:
    # # start_stop_id = L.L_northBound[len(L.L_northBound)-startIndex-1]    
    # # end_stop_id = L.L_northBound[len(L.L_northBound)-endIndex-1]
    # start_stop_id = stops.line1Nbound[startStation]    
    # end_stop_id = stops.line1Nbound[endStation]
# elif direction == south:
    # # start_stop_id = L.L_southBound[startIndex]
    # # end_stop_id = L.L_southBound[endIndex] 
    # start_stop_id = stops.line1Sbound[startStation]
    # end_stop_id = stops.line1Sbound[endStation]
    
print start_stop_id
print end_stop_id

# (trip_id, departureTime) = trip.getTripId(start_stop_id, route)
trip_ids = []
for route in ['2','3']:
    trip_ids.append(trip.getTripId(start_stop_id, route, 960))

# minutes = ((departureTime)-int(time.time()))/60

# print('Train with trip_id: %s will leave %s in %s minutes.'%(trip_id,L.stationNames[startIndex], minutes))
# print('Train with trip_id: %s will leave %s in %s minutes.'%(trip_id,stops.line1Seq[startIndex], minutes))
print trip_ids

# tripStatus = 'IN_PROGRESS'
# while tripStatus == 'IN_PROGRESS':

arrivalTimes = {}
for trip_id in trip_ids:
    trip_data = trip.getTripStatus(trip_id, start_stop_id, end_stop_id)
    departureTime = trip_data[0]
    arrivalTime = trip_data[1]
    currentStop = trip_data[2]
    currentStatus = trip_data[3]
    vehicleTime = trip_data[4]
        
    
    
    # if direction == north and currentStop != None:
        # # currentStopName = L.stationNames[len(L.stationNames)-currentStop]
        # currentStopName = stops.line1Seq[len(stops.line1Seq)-currentStop]
    # if direction == south and currentStop != None:
        # # currentStopName = L.stationNames[currentStop-1]
        # currentStopName = stops.line1Seq[currentStop-1]
    if currentStop != None:
        # currentStopName = L.stationNames[len(L.stationNames)-currentStop]
        currentStopName = stops.line1Seq[len(stops.line1Seq)-currentStop]
 
    
    
    if departureTime == None:
        arrivalMinutes = ((arrivalTime)-int(time.time()))/60
        arrivalTimes[trip_id] = arrivalTime
        print('Your train has left the station and is expected to be at the destination in %s minutes.'%arrivalMinutes)
        try:
            print('Your train is %s %s.'%(vehicleStopStatus[currentStatus],currentStopName))
        except:
            print('No information about train location avaialble')
    else:
        departMinutes = ((departureTime)-int(time.time()))/60
        try:
            arrivalMinutes = ((arrivalTime)-int(time.time()))/60
            arrivalTimes[trip_id] = arrivalTime
        except:
            print('No arrival information avaialble')
        print('Your train will depart in %s minutes and is expected to be at the destination in %s minutes.'%(departMinutes,arrivalMinutes))
        try:
            print('Your train is %s %s.'%(vehicleStopStatus[currentStatus],currentStopName))
        except:
            print('No information about train location avaialble')


if arrivalTimes[trip_ids[0]]<arrivalTimes[trip_ids[1]]:
    trip_id_express = trip_ids[0]
else:
    trip_id_express = trip_ids[1]
# time.sleep(30)
print('===============================')
    
    
    
    
    
    
    
    
    
    
    
    