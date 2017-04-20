import re
import csv
data = []
mySats = []
with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\sats.txt', 'r') as satsfile:

    for line in satsfile:
        if 'sats' in line:
            mystring = line.split('[')
            satsstring = mystring[1][:-1]
            satsstring = satsstring.split(',')
           # print(satsstring)
            #Differentiate each object from the array
            for item in satsstring:
                myObject = item
                #Create dictionary for each one of the objects
                #print(myObject)
                myObject2 = re.findall('[A-Z][^A-Z]*', myObject)
                myObject2 = myObject2[2:]
                myObject2[0] = "PR"+myObject2[0]
                #print(myObject2)
                myDict = dict((k.strip(), v.strip()) for k,v in (item.split(':')for item in myObject2))
                mySats.append(myDict)
                #data['sats'] = myDict
          #  print(myDict)
    mySats[-1]['Used'] = mySats[-1]['Used'].replace("]","")
    print(mySats)








