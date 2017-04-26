# import L_stops as L
import trip
import time
import stops
import numpy as np
<<<<<<< HEAD
import json
=======
from datetime import datetime as dt
>>>>>>> ab07b012e66d93da7ec7987507d59654ff350aac
# import datetime.datetime as dt


L114to1116 = [stops.line1Nbound['14 St'],stops.line1Nbound['116 St - Columbia University']]
L196to1116 = [stops.line1Nbound['96 St'],stops.line1Nbound['116 St - Columbia University']]

L114to196 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
# L214to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
# L314to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]

routes = ['1','2','3']

fastestTrip = trip.getFastestTrip(L114to196,routes)        
print(fastestTrip)
   
timeDiff = fastestTrip[1]-int(time.time())
fastestTransfer = trip.getFastestTransfer(L196to1116,'1',timeDiff)

print fastestTransfer
    
fastestTripSingle = trip.getFastestTrip(L114to1116,['1'])

print fastestTripSingle
    
if fastestTransfer[2] < fastestTripSingle[1]:

    print('Transfer trip')
    print fastestTrip
    
    print("Train to take: %s at %s"%(fastestTrip[0][7],dt.fromtimestamp(fastestTrip[1]).strftime('%H:%M:%S')))
    print("After transfer to %s at %s and you'll arrive at destination at %s"%(fastestTransfer[0][7],dt.fromtimestamp(fastestTransfer[1]).strftime('%H:%M:%S'), dt.fromtimestamp(fastestTransfer[2]).strftime('%H:%M:%S')))
    

    
    
    
else:
    print('Take single trip')

    print("Train to take: %s at %s"%(fastestTripSingle[0][7],dt.fromtimestamp(fastestTripSingle[1]).strftime('%H:%M:%S')))

