import re
import json

with open ('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r') as gpsFile:
    myGPS = []
    mySats = []
    data = {}
    ignore = [' GPS reading', '----------------------------------------', 'time utc', 'Killing', 'Done', 'Exiting']

    for line in gpsFile:

        if line.strip():                                            #Ignore the blank lines
            if any(name in line for name in ignore):                #Ignore additional info
                continue
            else:
                if 'sats' in line:
                    mystring = line.split('[')
                    satsstring = mystring[1][:-1]
                    satsstring = satsstring.split(',')
                    # print(satsstring)
                    # Differentiate each object from the array
                    for item in satsstring:

                        # Create dictionary for each one of the objects
                        # print(myObject)
                        myObject = re.findall('[A-Z][^A-Z]*', item)
                        myObject = myObject[2:]
                        myObject[0] = "PR" + myObject[0]
                        # print(myObject2)
                        myDict = dict((k.strip(), v.strip()) for k, v in (item.split(':') for item in myObject))
                        mySats.append(myDict)

                    data['sats'] = mySats
                    #adding for each data object
                    myGPS.append(data)
                    data = {}
                    mySats = []
                else:
                    tempfield = re.findall("[a-zA-Z]+", line)
                    field = ' '.join(tempfield)
                    tempvalue = re.findall(r'[-+]?\d*\.\d+|\d+', line)
                    value = ''.join(tempvalue).strip()

                    try:
                        value = float(value)
                    except ValueError as e:
                        print('error: blank space in the value')
                        #print(value)
                        #print(line)
                    data[field] = value

    #del myGPS[0]['']
    print(myGPS[0]['sats'])
   # print(myGPS[1])


    jsonData = json.dumps(myGPS)                                       #Save Python dictionary as JSON File
    with open('JSONGPSData.json','w') as f:
        json.dump(jsonData,f)


