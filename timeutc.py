import re
with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\sats.txt', 'r') as f:
    times = []
    for line in f:
        if 'time utc' in line:

            d = line.split('time utc')

            for item in d:
                #item = item.split('+')
                item = item.strip()
            times.append(d)
    print(times)