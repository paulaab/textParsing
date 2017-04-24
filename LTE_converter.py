import re
import json
with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\LTETrace_runde1.txt', 'r') as ltefile:
    ignore = {'Zeit',  '>>>>>>>>>>>>>>>>>>>>>>>>', '!GSTATUS: ','!LTEINFO:','--','2017'}
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
            elif line.startswith('LTE Pegel'):
                if not next(ltefile):
                    time = next(ltefile)
                    time = next(ltefile).replace(' ','T').replace('\n','')
                    data['time utc'] = time
                else:
                    continue
            elif line.startswith('Serving'):

                fields = line[8:].replace('\n','').split(' ')
                fields = [item for item in fields if item]

                values = next(ltefile)
                values = values.replace('\n', '').split(' ')
                values = [item for item in values if item]

                d = dict(zip(fields,values))

                data['Serving'] = d
                #print(values)
            elif line.startswith('IntraFreq'):
                fields = line[10:].split()
                values = []
                temp = []
                for i in range (0,100):
                    myline = next(ltefile)
                    if not myline.isspace():
                        myvalues = myline.replace('\n', '').split(' ')
                        myvalues = [item for item in myvalues if item]
                        temp.append(myvalues)
                    else:
                        break


                values = list(zip(*temp))
                values = [list(item) for item in values]
                d = dict(zip(fields, values))
                data['IntraFreq'] = d




            elif line.startswith('CDMA HRPD:'):
                data['CMDA HRPD'] = line[10:].strip()
                myLTE.append(data)
                data = {}

            elif 'PCC' in line:
                field = line[:12]
                item = re.findall(r'[-+]?\d+(?:\.\d+)?', line)
                data[field] = {}
                data[field]['value'] = item[0]
                data[field]['RSRP (dBm)'] = item[1]

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


    print(myLTE)

    jsonData = json.dumps(myLTE)                                       #Save Python dictionary as JSON File
    with open('JSONLTEData.json', 'w') as f:
        json.dump(jsonData, f)





