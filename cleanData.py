__author__ = 'elsieyao'

import csv
from pprint import pprint

with open('1114_1015_airline_delay_causes.csv') as csvfile:

    reader = csv.DictReader(csvfile)
    dict = {}
    for now in reader:
        dict_inc = {}
        now.pop('',None)
        if len(now[' month'])==1:
            dict_inc['year_month'] = now['year'] + '-0' + now[' month']
        else:
            dict_inc['year_month'] = now['year'] + '-' + now[' month']
        try: dict_inc['all_flights'] = float(now['arr_flights']) + float(now['arr_del15']) + float(now['arr_diverted']) + float(now['arr_cancelled'])
        except:
            #pprint(now)
            continue
        dict_inc['arr_flights'] = float(now['arr_flights'])
        if now['carrier_name'] not in dict:
            dict[now['carrier_name']] = []
        existed = False
        for month in dict[now['carrier_name']]:
            if dict_inc['year_month'] == month['year_month']:
                month['all_flights'] += dict_inc['all_flights']
                month['arr_flights'] += dict_inc['arr_flights']
                month['on_time_ct'] = month['arr_flights']/month['all_flights']
                existed = True
        if existed == False:
            dict_inc['on_time_ct'] = dict_inc['arr_flights']/dict_inc['all_flights']
            dict[now['carrier_name']].append(dict_inc)
    #pprint(dict)

output = []
for key in dict:
    for out_dict in dict[key]:
        out_dict['carrier'] = key
        output.append(out_dict)
#print output

with open('airline_data.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, output[0].keys())
    w.writeheader()
    for i in range(len(output)):
        w.writerow(output[i])
