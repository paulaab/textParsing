import json
import re
import itertools
#gpsFile = open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r')

#
# numBlocks = 0  # Number of blocks of measurements
# # Creating an empty Python dictionary to store future data from the text file
# gps = {
#     "latitude": None,
#     "longitude": None,
#     "time utc": None,
#     "altitude": None,
#     "eps": None,
#     "epx": None,
#     "epv": None,
#     "ept": None,
#     "speed": None,
#     "climb": None,
#     "mode": None,
#     "sats": [
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#
#         {
#             "PRN": None,
#             "E": None,
#             "Az": None,
#             "Ss": None,
#             "Used": None
#         },
#     ]
# }
#
# def is_separator (line):
#     return line == 'GPS reading'
# cont = 0
# data = {}
# myGPS = []  # Empty list
gpsFile = open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r')
    # data = {}
    # myGPS = []  # Empty list
    #
    # for line in gpsFile:
    #     if cont <= 2:
    #         if line.strip():
    #             if 'GPS reading' in line:
    #                 continue
    #             if '----------------------------------------' in line:
    #                 continue
    #             if 'time utc' in line:
    #                 continue
    #             if 'sats' in line:
    #                 continue
    #             if 'Killing' in line:
    #                 continue
    #             if 'Done' in line:
    #                 continue
    #             if 'Exiting' in line:
    #                 continue
    #
    #             else:
    #
    #                 temp = re.findall("[a-zA-Z]+", line)
    #                 field = ' '.join(temp)
    #                 value = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #                 data[field] = value
    #
    #                 #print(data)
    #                 if 'sats' in line:
    #
    #                     cont =+ 1
    #
    #
    #     else:
    #
    #         break



    #----------------------------------------
    cont = 0
    myGPS = []
    data = {}
    ignore = (' GPS reading' , '----------------------------------------' , 'time utc' ,  'Killing' , 'Done' , 'Exiting', 'sats', ' ')
    for line in gpsFile:


            if any(name in line for name in ignore):
                continue
            else:
                temp = re.findall("[a-zA-Z]+", line)
                field = ' '.join(temp)
                value = re.findall(r'[-+]?\d*\.\d+|\d+', line)
                print(field)









# print(myGPS[0])
# print()
# print(myGPS[1])
                        #print (field + value)
    #print(myGPS)
                    #print(item.format(**data))


        # if not key:
        #     for item in group:
        #         print(item)
        #         # s = item
        #         # parts = re.split('(\d.*)', s)
        #         # print(len(parts))
        #         # print(parts)
        #         if 'GPS reading' in item:
        #             break

#print(myGPS)





# i = 0
# cont = 0
# with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r') as gpsFile:
#     for line in gpsFile:
#
#         if 'GPS reading' in line:
#             numBlocks += 1
#             myGPS.append(gps)
#         if 'latitude' in line:
#             myGPS[i]["latitude"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'longitude' in line:
#             myGPS[i]["longitude"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'time utc' in line:
#             prueba = 0
#             # gps["time utc"] = re.findall()
#         if 'altitude' in line:
#             myGPS[i]["altitude"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'eps' in line:
#             myGPS[i]["eps"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'epx' in line:
#             myGPS[i]["epx"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'epv' in line:
#             myGPS[i]["epv"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'ept' in line:
#             myGPS[i]["ept"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'speed' in line:
#             myGPS[i]["speed"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'climb' in line:
#             myGPS[i]["climb"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'track' in line:
#             myGPS[i]["track"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'mode' in line:
#             myGPS[i]["mode"] = re.findall(r'[-+]?\d*\.\d+|\d+', line)
#         if 'sats' in line:
#             i += 1
#             cont += 1
#         if cont == 2:
#             break
#        # print(i)
#  #i += 1
#     #i = 0
# print (myGPS[0])
# print (myGPS[1])
# #print(myGPS[2])


            # Read the complete file to know the quantity of Blocks of measurements a.k.a. GPS reading that there is.
            # for line in gpsFile:
            #   if 'GPS reading' in line:
            #      numBlocks += 1
            # print(numBlocks)
            # Create a list of GPS Measurements depending on the quantity of blocks.
            # for x in range(0, numBlocks):
            #   myGPS.append(gps)
            # print(numBlocks)

            #  print(myGPS[104])


            # myGPS = [gps]
    # for line in gpsFile:
    #     if 'GPS reading' in line:
    #         numBlocks += 1
    #         myGPS.append(gps)
    #     if 'latitude' in line:
    #         lat = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'longitude' in line:
    #         long = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'time utc' in line:
    #         prueba = 0
    #         # gps["time utc"] = re.findall()
    #     if 'altitude' in line:
    #         alt = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'eps' in line:
    #         eps = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'epx' in line:
    #         epx = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'epv' in line:
    #         epv = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'ept' in line:
    #         ept = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'speed' in line:
    #         speed = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'climb' in line:
    #         climb = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'track' in line:
    #         track = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'mode' in line:
    #         mode = re.findall(r'[-+]?\d*\.\d+|\d+', line)
    #     if 'sats' in line:
    #         print(i)
    #         myGPS[i]["latitude"] = lat
    #         myGPS[i]["longitude"] = long
    #         myGPS[i]["altitude"] = alt
    #         myGPS[i]["eps"] = eps
    #         myGPS[i]["epx"] = epx
    #         myGPS[i]["epv"] = epv
    #         myGPS[i]["ept"] = ept
    #         myGPS[i]["speed"] = speed
    #         myGPS[i]["climb"] = climb
    #         myGPS[i]["track"] = track
    #         myGPS[i]["mode"] = mode
    #         i += 1
    #         print(myGPS[i])
    #         print(i)


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
