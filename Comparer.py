import json
import ast

gpsFile =  open('JSONGPSData.json','r')
lteFile = open('JSONLTEData.json','r')
gpsTime = []
lteTime=[]
gps = ast.literal_eval(json.load(gpsFile))
lte = ast.literal_eval(json.load(lteFile))
for i in range(0, len(gps)):
    gpsTime.append(gps[i]['time utc'])
for i in range(0,len(lte)):
    lteTime.append(lte[i]['time utc'])


#print(gpsTime)
print(lteTime)
