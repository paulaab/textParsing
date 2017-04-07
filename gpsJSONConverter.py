import json
import re

numLines = 0;

gpsFile = open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt','r')

#Creting an empty Python dictionary to store future data from the textfile
gps = {
    "latitude" : None,
    "longitude" : None,
    "time utc" : None,
    "altitude" : None,
    "eps" : None,
    "epx" : None,
    "epv" : None,
    "ept" : None,
    "speed" : None,
    "climb" : None,
    "mode" : None,
    "sats" : [

        {
            "PRN" : None,
            "E" : None,
            "Az" : None,
            "Ss" : None,
            "Used" : None
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

#Process that allows me to jump to a certain line of the document
line_offset = []
offset = 0
for line in gpsFile:
    line_offset.append(offset)
    offset += len(line)
gpsFile.seek(0)


#Example of jumping to a specific file, the first line is 0:
#gpsFile.seek(line_offset[n])


#Creating a loop that depends on the number of measurements in the file


















#-------------------------LINKS IMPORTANTES-------------------------------------------------#

#http://stackoverflow.com/questions/41542734/how-to-create-json-object-in-python
#http://stackoverflow.com/questions/18688298/how-to-create-multiple-json-objects-via-for-loop
#http://stackoverflow.com/questions/14575433/json-how-to-properly-create-json-array

