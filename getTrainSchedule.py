import L_stops as L
import trip
import time
import stops
import numpy as np
# import datetime.datetime as dt


L114to116 = [stops.line1Nbound['14 St'],stops.line1Nbound['116 St - Columbia University']]
L196to116 = [stops.line1Nbound['96 St'],stops.line1Nbound['116 St - Columbia University']]

L114to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
# L214to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]
# L314to96 = [stops.line1Nbound['14 St'],stops.line1Nbound['96 St']]

routes = ['1','2','3']

fastestTrip = trip.getFastestTrip(L114to96,routes)        
print(fastestTrip)
   
timeDiff = fastestTrip[1]-int(time.time())
fastestTransfer = trip.getFastestTransfer(L196to116,'1',timeDiff)

print fastestTransfer
    
fastestTripSingle = trip.getFastestTrip(L114to116,['1'])

print fastestTripSingle
    
if fastestTransfer[2] < fastestTripSingle[1]:
    print('Take transfer trip')
else:
    print('Take single trip')