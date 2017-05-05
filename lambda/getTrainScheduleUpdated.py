from google.transit import gtfs_realtime_pb2
import tripUpdated as trip
import time
import stops
# import numpy as np
import json
# import sys
from pprint import pprint
from datetime import datetime as dt
import requests
APIkey = "10a12f7b56a78c2111a54c380493a96b"


def getlist(start,end):

    if start=="14 St" and end=="116 St - Columbia University":

        single = [stops.line1Nbound["14 St"],stops.line1Nbound["116 St - Columbia University"]]
        transfer = [stops.line1Nbound["96 St"],stops.line1Nbound["116 St - Columbia University"]]
        start = [stops.line1Nbound["14 St"],stops.line1Nbound["96 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="116 St - Columbia University" and end=="14 St":
        single = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["14 St"]]
        transfer = [stops.line1Sbound["96 St"],stops.line1Sbound["14 St"]]
        start = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["96 St"]]
        routes = ["1","2","3"]
        line = stops.line1

    elif start=="14 St" and end=="34 St - Penn Station":
        single = [stops.line1Nbound["14 St"],stops.line1Nbound["34 St - Penn Station"]]
        # transfer = [stops.line1Nbound["14 St"],stops.line1Nbound["34 St - Penn Station"]]
        transfer = None
        start = [stops.line1Nbound["14 St"],stops.line1Nbound["34 St - Penn Station"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="34 St - Penn Station" and end=="14 St":
        single = [stops.line1Sbound["34 St - Penn Station"],stops.line1Sbound["14 St"]]
        # transfer = [stops.line1Sbound["96 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["34 St - Penn Station"],stops.line1Sbound["14 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="14 St" and end=="Times Sq - 42 St":
        single = [stops.line1Nbound["14 St"],stops.line1Nbound["Times Sq - 42 St"]]
        # transfer = [stops.line1Nbound["14 St"],stops.line1Nbound["34 St - Penn Station"]]
        transfer = None
        start = [stops.line1Nbound["14 St"],stops.line1Nbound["Times Sq - 42 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="Times Sq - 42 St" and end=="14 St":
        single = [stops.line1Sbound["Times Sq - 42 St"],stops.line1Sbound["14 St"]]
        # transfer = [stops.line1Sbound["96 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["Times Sq - 42 St"],stops.line1Sbound["14 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="14 St" and end=="59 St - Columbus Circle":
        single = [stops.line1Nbound["14 St"],stops.line1Nbound["59 St - Columbus Circle"]]
        transfer = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["59 St - Columbus Circle"]]
        # transfer = None
        start = [stops.line1Nbound["14 St"],stops.line1Nbound["Times Sq - 42 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="59 St - Columbus Circle" and end=="14 St":
        single = [stops.line1Sbound["59 St - Columbus Circle"],stops.line1Sbound["14 St"]]
        transfer = [stops.line1Sbound["Times Sq - 42 St"],stops.line1Sbound["14 St"]]
        # transfer = None
        start = [stops.line1Sbound["59 St - Columbus Circle"],stops.line1Sbound["Times Sq - 42 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="14 St" and end=="72 St":
        single = [stops.line1Nbound["14 St"],stops.line1Nbound["72 St"]]
        # transfer = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["72 St"]]
        transfer = None
        start = [stops.line1Nbound["14 St"],stops.line1Nbound["72 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="72 St" and end=="14 St":
        single = [stops.line1Sbound["72 St"],stops.line1Sbound["14 St"]]
        # transfer = [stops.line1Sbound["72 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["72 St"],stops.line1Sbound["14 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    #-------------
    elif start=="34 St - Penn Station" and end=="116 St - Columbia University":

        single = [stops.line1Nbound["34 St - Penn Station"],stops.line1Nbound["116 St - Columbia University"]]
        transfer = [stops.line1Nbound["96 St"],stops.line1Nbound["116 St - Columbia University"]]
        start = [stops.line1Nbound["34 St - Penn Station"],stops.line1Nbound["96 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="116 St - Columbia University" and end=="34 St - Penn Station":
        single = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["34 St - Penn Station"]]
        transfer = [stops.line1Sbound["96 St"],stops.line1Sbound["34 St - Penn Station"]]
        start = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["96 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="34 St - Penn Station" and end=="Times Sq - 42 St":
        single = [stops.line1Nbound["34 St - Penn Station"],stops.line1Nbound["Times Sq - 42 St"]]
        # transfer = [stops.line1Nbound["14 St"],stops.line1Nbound["34 St - Penn Station"]]
        transfer = None
        start = [stops.line1Nbound["34 St - Penn Station"],stops.line1Nbound["Times Sq - 42 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="Times Sq - 42 St" and end=="34 St - Penn Station":
        single = [stops.line1Sbound["Times Sq - 42 St"],stops.line1Sbound["34 St - Penn Station"]]
        # transfer = [stops.line1Sbound["96 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["Times Sq - 42 St"],stops.line1Sbound["34 St - Penn Station"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="34 St - Penn Station" and end=="59 St - Columbus Circle":
        single = [stops.line1Nbound["34 St - Penn Station"],stops.line1Nbound["59 St - Columbus Circle"]]
        # transfer = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["59 St - Columbus Circle"]]
        transfer = None
        start = [stops.line1Nbound["34 St - Penn Station"],stops.line1Nbound["59 St - Columbus Circle"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="59 St - Columbus Circle" and end=="34 St - Penn Station":
        single = [stops.line1Sbound["59 St - Columbus Circle"],stops.line1Sbound["34 St - Penn Station"]]
        # transfer = [stops.line1Sbound["Times Sq - 42 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["59 St - Columbus Circle"],stops.line1Sbound["34 St - Penn Station"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="34 St - Penn Station" and end=="72 St":
        single = [stops.line1Nbound["34 St - Penn Station"],stops.line1Nbound["72 St"]]
        # transfer = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["72 St"]]
        transfer = None
        start = [stops.line1Nbound["34 St - Penn Station"],stops.line1Nbound["72 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="72 St" and end=="34 St - Penn Station":
        single = [stops.line1Sbound["72 St"],stops.line1Sbound["34 St - Penn Station"]]
        # transfer = [stops.line1Sbound["72 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["72 St"],stops.line1Sbound["34 St - Penn Station"]]
        routes = ["1","2","3"]
        line = stops.line1
    #-------------
    elif start=="Times Sq - 42 St" and end=="116 St - Columbia University":

        single = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["116 St - Columbia University"]]
        transfer = [stops.line1Nbound["96 St"],stops.line1Nbound["116 St - Columbia University"]]
        start = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["96 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="116 St - Columbia University" and end=="Times Sq - 42 St":
        single = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["Times Sq - 42 St"]]
        transfer = [stops.line1Sbound["96 St"],stops.line1Sbound["Times Sq - 42 St"]]
        start = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["96 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="Times Sq - 42 St" and end=="59 St - Columbus Circle":
        single = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["59 St - Columbus Circle"]]
        # transfer = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["59 St - Columbus Circle"]]
        transfer = None
        start = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["59 St - Columbus Circle"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="59 St - Columbus Circle" and end=="Times Sq - 42 St":
        single = [stops.line1Sbound["59 St - Columbus Circle"],stops.line1Sbound["Times Sq - 42 St"]]
        # transfer = [stops.line1Sbound["Times Sq - 42 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["59 St - Columbus Circle"],stops.line1Sbound["Times Sq - 42 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="Times Sq - 42 St" and end=="72 St":
        single = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["72 St"]]
        # transfer = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["72 St"]]
        transfer = None
        start = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["72 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="72 St" and end=="Times Sq - 42 St":
        single = [stops.line1Sbound["72 St"],stops.line1Sbound["Times Sq - 42 St"]]
        # transfer = [stops.line1Sbound["72 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["72 St"],stops.line1Sbound["Times Sq - 42 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    #-------------
 
    elif start=="59 St - Columbus Circle" and end=="116 St - Columbia University":

        single = [stops.line1Nbound["59 St - Columbus Circle"],stops.line1Nbound["116 St - Columbia University"]]
        # transfer = [stops.line1Nbound["96 St"],stops.line1Nbound["116 St - Columbia University"]]
        transfer=None
        start = [stops.line1Nbound["59 St - Columbus Circle"],stops.line1Nbound["116 St - Columbia University"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="116 St - Columbia University" and end=="59 St - Columbus Circle":
        single = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["59 St - Columbus Circle"]]
        # transfer = [stops.line1Sbound["96 St"],stops.line1Sbound["Times Sq - 42 St"]]
        transfer = None
        start = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["59 St - Columbus Circle"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    elif start=="59 St - Columbus Circle" and end=="72 St":
        single = [stops.line1Nbound["59 St - Columbus Circle"],stops.line1Nbound["72 St"]]
        # transfer = [stops.line1Nbound["Times Sq - 42 St"],stops.line1Nbound["72 St"]]
        transfer = None
        start = [stops.line1Nbound["59 St - Columbus Circle"],stops.line1Nbound["72 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="72 St" and end=="59 St - Columbus Circle":
        single = [stops.line1Sbound["72 St"],stops.line1Sbound["59 St - Columbus Circle"]]
        # transfer = [stops.line1Sbound["72 St"],stops.line1Sbound["14 St"]]
        transfer = None
        start = [stops.line1Sbound["72 St"],stops.line1Sbound["59 St - Columbus Circle"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    
    #-------------
    elif start=="72 St" and end=="116 St - Columbia University":

        single = [stops.line1Nbound["72 St"],stops.line1Nbound["116 St - Columbia University"]]
        transfer = [stops.line1Nbound["96 St"],stops.line1Nbound["116 St - Columbia University"]]
        start = [stops.line1Nbound["72 St"],stops.line1Nbound["96 St"]]
        routes = ["1","2", "3"]
        line = stops.line1
        
    elif start=="116 St - Columbia University" and end=="72 St":
        single = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["72 St"]]
        transfer = [stops.line1Sbound["96 St"],stops.line1Sbound["72 St"]]
        start = [stops.line1Sbound["116 St - Columbia University"],stops.line1Sbound["96 St"]]
        routes = ["1","2","3"]
        line = stops.line1
    
    
    return(single, transfer, start, routes, line)
    
def getTrip(event, context):
    
    # print(event)
    try:
        feed = gtfs_realtime_pb2.FeedMessage()
        response = requests.get("http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1"%APIkey)
        # print response       
        feed.ParseFromString(response.content)
        
        
        (single, transfer, start, routes, line)=getlist(event["start"],event["end"])
        # (single, transfer, start, routes, line)=getlist(event["queryStringParameters"]["start"],event["queryStringParameters"]["end"])
            
            

        fastestTrip = trip.getFastestTrip(start,routes, feed)        
        # print(fastestTrip)
        if transfer == None:
            fastestTransfer = fastestTrip
        else:
            timeDiff = fastestTrip["arrivalTime"]-int(time.time())
            fastestTransfer = trip.getFastestTransfer(transfer,routes,timeDiff,feed)

        # print fastestTransfer
            
        # fastestTripSingle = trip.getFastestTrip(single,transfer_route)
        fastestTripSingle = trip.getFastestTrip(single,routes,feed)

        # print fastestTripSingle
            
        if fastestTransfer["arrivalTime"] < fastestTripSingle["arrivalTime"]:
            # print("Take transfer trip")
            # print(fastestTrip)
            # print(fastestTransfer)
            data = {}
            data["start"]=fastestTrip
            if transfer == None:
                data["transfer"]=None
            else:
                data["transfer"]=fastestTransfer

            json_data = json.dumps(data)

            # print(json_data)
            
            
            
        else:
            # print("Take single trip")
            data = {}
            data["start"]=fastestTripSingle
            data["transfer"]=None
            
            # data["start"]["trip_id"]=fastestTripSingle[0]
            # data["start"]["route_id"]=fastestTripSingle[0][7]
            # data["start"]["start_station"]=single[0]
            # data["start"]["departure"]=fastestTripSingle[1]
            # data["start"]["end_station"]=single[1]
            
            json_data = json.dumps(data)
            
            # print(json_data)

        # print(json_data)
        # print(data)
        return(data)
    except:
        pass
    # return(json_data)
    
def getTripUpdate(event, context):
    # time.sleep(30)
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get("http://datamine.mta.info/mta_esi.php?key=%s&feed_id=1"%APIkey)
    # print response       
    feed.ParseFromString(response.content)
    # print(event)
    (single, transfer, start, routes, line)=getlist(event["start"],event["end"])
    # (single, transfer, start, routes, line)=getlist(event[u"queryStringParameters"][u"start"],event[u"queryStringParameters"][u"end"])
    
    # try:
    update = trip.tripUpdate(event["tripstart"], start,feed)
    # update = trip.tripUpdate(event[u"queryStringParameters"][u"tripstart"], start,feed)
    
    udata = {}
    udata["start"]={}
        
    udata["start"]["trip_id"]=update[0]
    # udata["start"]["departureTime"]=dt.fromtimestamp(update[1]).strftime("%H:%M:%S")
    udata["start"]["departureTime"]=update[1]
    # udata["start"]["arrivalTime"]=dt.fromtimestamp(update[2]).strftime("%H:%M:%S")
    udata["start"]["arrivalTime"]=update[2]
    # udata["start"]["current_stop_id"]=line[str(update[3][:3])]
    udata["start"]["current_stop_id"]=update[3]
    udata["start"]["current_status"]=update[5]
    udata["start"]["train_status"]=update[6]
    # udata["start"]["time"]=dt.fromtimestamp(update[7]).strftime("%H:%M:%S")
    udata["start"]["time"]=update[7]
    
    
    if event["tripend"]!="":
    # if event[u"queryStringParameters"][u"tripend"]!=None:
        transfer = trip.tripUpdate(event["tripend"], transfer,feed)
        # transfer = trip.tripUpdate(event[u"queryStringParameters"][u"tripend"], transfer,feed)
        
        udata["transfer"]={}
        udata["transfer"]["trip_id"]=transfer[0]
        # udata["transfer"]["departureTime"]=dt.fromtimestamp(transfer[1]).strftime("%H:%M:%S")
        udata["transfer"]["departureTime"]=transfer[1]
        # udata["transfer"]["arrivalTime"]=dt.fromtimestamp(transfer[2]).strftime("%H:%M:%S")
        udata["transfer"]["arrivalTime"]=transfer[2]
        # udata["transfer"]["current_stop_id"]=line[str(transfer[3][:3])]
        udata["transfer"]["current_stop_id"]=transfer[3]
        udata["transfer"]["current_status"]=transfer[5]
        udata["transfer"]["train_status"]=transfer[6]
        # udata["transfer"]["time"]=dt.fromtimestamp(transfer[7]).strftime("%H:%M:%S")
        udata["transfer"]["time"]=transfer[7]
    else:
        udata["transfer"]=None
    
    
    # print(udata)
    return(udata)
    # except:
        # pass
            
# getTrip(["14 St","116 St - Columbia University"],1)
# {"start":"14 St","end":"34 St - Penn Station"}