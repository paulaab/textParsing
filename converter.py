import re
import json
gpsFile = open ('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r')
myGPS = []
data = {}
ignore = [' GPS reading', '----------------------------------------', 'time utc', 'Killing', 'Done', 'Exiting']

for line in gpsFile:
    if line.strip():
        if any(name in line for name in ignore):
            continue
        else:
            if 'sats' in line:
                myGPS.append(data)
                data = {}
            else:
                tempfield = re.findall("[a-zA-Z]+", line)
                field = ' '.join(tempfield)
                value = re.findall(r'[-+]?\d*\.\d+|\d+', line)
                data[field] = value
del myGPS[0]['']
print(myGPS[1])
jsonData = json.dumps(myGPS)
#print(jsonData)

with open('JSONGPSData.json','w') as f:
    json.dump(jsonData,f)


