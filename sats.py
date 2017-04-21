import re
import csv
data = []
mySats = []
with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\sats.txt', 'r') as satsfile:

    for line in satsfile:
        if 'sats' in line:
            start = line.find('[') + 1
            end = line.find(']', start)
            satsstring = line[start:end]
            if satsstring == '':            #Check if sats string is empty
                continue
            else:
                satsstring = satsstring.split(',')
                print(satsstring)
                for item in satsstring:
                    #Create dictionary for each one of the objects
                    item = re.findall('[A-Z][^A-Z]*', item)[2:] # Separate each key-value depending on the start of capital letters
                    item[0] = "PR"+item[0] #Correction for PRN, before was just N
                    myDict = dict((k.strip(), v.strip()) for k,v in (item.split(':')for item in item)) #Separate in each par of key-value, the key value depending on the : , then strip both values and add them to the dictionary as key/value pairs again
                    mySats.append(myDict)
    #print(mySats)








