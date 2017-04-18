import json
import re
#gpsFile = open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r')

myGPS = []  # Empty list
numBlocks = 0  # Number of blocks of measurements
# Creating an empty Python dictionary to store future data from the text file
gps = {
    "latitude": None,
    "longitude": None,
    "time utc": None,
    "altitude": None,
    "eps": None,
    "epx": None,
    "epv": None,
    "ept": None,
    "speed": None,
    "climb": None,
    "mode": None,
    "sats": [

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },

        {
            "PRN": None,
            "E": None,
            "Az": None,
            "Ss": None,
            "Used": None
        },
    ]
}
i = 0

with open ('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r') as gpsFile:
    # Read the complete file to know the quantity of Blocks of measurements a.k.a. GPS reading that there is.
    #for line in gpsFile:
     #   if 'GPS reading' in line:
      #      numBlocks += 1
    #print(numBlocks)
    # Create a list of GPS Measurements depending on the quantity of blocks.
    #for x in range(0, numBlocks):
     #   myGPS.append(gps)
        #print(numBlocks)

      #  print(myGPS[104])
    numBlocks = -1

    #myGPS = [gps]

    # for line in gpsFile:
    #
    #     if 'GPS reading' in line:
    #         numBlocks += 1
    #
    #         myGPS.append(gps)
    #     if 'latitude' in line:
    #         myGPS[i]["latitude"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'longitude' in line:
    #         myGPS[i]["longitude"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'time utc' in line:
    #         prueba = 0
    #         # gps["time utc"] = re.findall()
    #     if 'altitude' in line:
    #         myGPS[i]["altitude"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'eps' in line:
    #         myGPS[i]["eps"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'epx' in line:
    #         myGPS[i]["epx"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'epv' in line:
    #         myGPS[i]["epv"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'ept' in line:
    #         myGPS[i]["ept"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'speed' in line:
    #         myGPS[i]["speed"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'climb' in line:
    #         myGPS[i]["climb"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'track' in line:
    #         myGPS[i]["track"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'mode' in line:
    #         myGPS[i]["mode"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'sats' in line:
    #         i += 1
    i = 0

    for line in gpsFile:
        if 'GPS reading' in line:
            numBlocks += 1
            myGPS.append(gps)
        if 'latitude' in line:
            lat = re.findall(r'[-+]?\d*\.\d+|\d+', line)
            print(line)
        if 'longitude' in line:
            long = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'time utc' in line:
            prueba = 0
            # gps["time utc"] = re.findall()
        if 'altitude' in line:
            alt = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'eps' in line:
            eps = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'epx' in line:
            epx = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'epv' in line:
            epv = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'ept' in line:
            ept = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'speed' in line:
            speed = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'climb' in line:
            climb = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'track' in line:
            track = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'mode' in line:
            mode = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        if 'sats' in line:
            print(i)
            myGPS[i]["latitude"] = lat
            myGPS[i]["longitude"] = long
            myGPS[i]["altitude"] = alt
            myGPS[i]["eps"] = eps
            myGPS[i]["epx"] = epx
            myGPS[i]["epv"] = epv
            myGPS[i]["ept"] = ept
            myGPS[i]["speed"] = speed
            myGPS[i]["climb"] = climb
            myGPS[i]["track"] = track
            myGPS[i]["mode"] = mode
            i += 1
            print(myGPS[i])
            print(i)


        #print (i)

#print(len(myGPS))
#print(line)
#print(myGPS[0])





#print(myGPS[0])
#print (myGPS[104])
        # Creating a loop that depends on the number of block-measurements in the file




#print(myGPS[0])

    #gpsFile.close()
    # Saving the Python dictionary
    # json_data = json.dumps(dictList)


#http://www.computerhope.com/issues/ch001721.htm
#http://www.computerhope.com/issues/ch001721.htm
























# -------------------------LINKS IMPORTANTES-------------------------------------------------#

# http://stackoverflow.com/questions/41542734/how-to-create-json-object-in-python
# http://stackoverflow.com/questions/18688298/how-to-create-multiple-json-objects-via-for-loop
# http://stackoverflow.com/questions/14575433/json-how-to-properly-create-json-array
