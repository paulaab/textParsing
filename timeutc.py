import re
import itertools
import time
with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\sats.txt', 'r') as f:
    #times = []
    for line in f:

        if 'time utc' in line:

            times = list(map(str.strip,line[8:].split('+'))).pop(0)
            print(type(times))
            #times = list(map(str.strip, times))






            #print(times)