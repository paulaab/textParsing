import re
with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\sats.txt', 'r') as satsfile:
    for line in satsfile:
        if 'sats' in line:
            mystring = line.split('[')
            satsstring = mystring[1][:-1]

            #found = re.search('[(.+?)]',line).group(1)

print(satsstring)



