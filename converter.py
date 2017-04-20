import re
import json

with open ('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r') as gpsFile:
    myGPS = []
    data = {}
    ignore = [' GPS reading', '----------------------------------------', 'time utc', 'Killing', 'Done', 'Exiting']

    for line in gpsFile:

        if line.strip():                                            #Ignore the blank lines
            if any(name in line for name in ignore):                #Ignore additional info
                continue
            else:
                if 'sats' in line:
                    line.split('[')
                    myGPS.append(data)
                    data = {}
                else:
                    tempfield = re.findall("[a-zA-Z]+", line)
                    field = ' '.join(tempfield)
                    tempvalue = re.findall(r'[-+]?\d*\.\d+|\d+', line)
                    value = ''.join(tempvalue).strip()
                    try:
                        value = float(value)
                    except ValueError as e:
                        print('error')
                        #print(value)
                        #print(line)
                    data[field] = value

    del myGPS[0]['']
    print(myGPS[0])
    print(myGPS[1])


    jsonData = json.dumps(myGPS)                                       #Save Python dictionary as JSON File
    with open('JSONGPSData.json','w') as f:
        json.dump(jsonData,f)


