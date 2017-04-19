import re
gpsFile = open ('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r')
myGPS = []
data = {}
ignore = [
' GPS reading', '----------------------------------------', 'time utc', 'Killing', 'Done', 'Exiting']

for line in gpsFile:
    if any(name in line for name in ignore):
        continue
    else:
        if 'sats' in line:
            myGPS.append(data)
            data = {}
        else:
            temp = re.findall("[a-zA-Z]+", line)
            field = ' '.join(temp)
            value = re.findall(r'[-+]?\d*\.\d+|\d+', line)
            data[field] = value


print(myGPS[10])

