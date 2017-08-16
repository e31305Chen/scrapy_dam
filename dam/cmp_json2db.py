#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors
import sys
import os
import time
import json

def run_scrapy():
    os.system("scrapy crawl damwra")
    time.sleep(5)
    os.system("scrapy crawl damwra")

#Compare two json file
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

def convert2list(string):
    s = open(string,"r")
    s_list = s.read().splitlines()
    l = len(s_list)-1
    object_list = []
    for i in range(0,l,1):
        object_list.append(json.loads(s_list[i]))
    return(object_list)
    
try:
    conn = MySQLdb.connect(host='localhost',
                            user='demouser',
                            passwd='demo1234',
                            db='demo',
                            charset='utf8')
except:
    print("Can't Connect Database via demouser: ", sys.exc_info()[0])
    sys.exit()
    
cursor = conn.cursor() 
# myDict = {'EffectiveWaterStorageCapacity': 17154.58,
#  'MaximumCapacity': '20134.00',
#  'PercentageUsedInReservoirCapacity': '31.2',
#  'R_ID': 1,
#  'TimeStamp': '2017-08-14',
#  'WaterLevel': 999}

run_scrapy()

dict_item1 = convert2list("/home/ubuntu/workspace/scrapy_dam/dam/damwra_items1.json")
dict_item2 = convert2list("/home/ubuntu/workspace/scrapy_dam/dam/damwra_items2.json")

for t in range(1,5,1):
    if(ordered(dict_item1) == ordered(dict_item1)):
        l = len(dict_item1)-1
        print(l)
        for i in range(0,l,1):
            myDict = dict_item1[i]
            # Insert object to mysql 
            a =  list(myDict.values())
            values = '\"' + '\",\"'.join(map(str, a)) + '\"'
            column_name = ', '.join(myDict.keys())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("ReservoirState", column_name, values)
            print(sql)
            cursor.execute(sql)
            conn.commit()
            
        print("File comparison pass and has been insert into DB table ReservoirState!")
        break
    else:
        print("comparison is fail. Try "+t+" times")
        run_scrapy()



# Close DB link
cursor.close()
conn.close()
