import re
with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\ltereduced.txt', 'r') as ltefile:
    ignore = {'Zeit' , '>>>>>>>>>>>>>>>>>>>>>>>>','LTE Pegel','!GSTATUS: ','!LTEINFO:','--','IntraFreq','Serving','2017'}
    onestring = {'EMM','RRC','IMS','SINR','InterFreq', 'LTE CA state','GSM','WCDMA','CDMA 1x'}
    data = {}
    myLTE = []
    for line in ltefile:
        if line.strip():
            if any(item in line for item in ignore):
                continue
            elif any(item in line for item in onestring):
                line = line.strip().split(':')
                item = [i.strip().replace('     \t', '-') for i in line]
                data[item[0]] = item[1]

            elif line.startswith('CDMA HRPD:'):
                myLTE.append(data)
                data = {}
            elif 'PCC' in line:
                print(line)
            else:

                if line.startswith('System mode'):
                    line = line.strip('\n').strip().split('\t')
                else:
                    line = line.strip().split('		')
                for item in line:
                    item = item.split(':')
                    item = [i.strip() for i in item]
                    field = item[0]
                    value = item[1]
                    data[field] = value


    #print(myLTE)






