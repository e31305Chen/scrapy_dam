#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors
import sys
import os
import time

os.system("scrapy crawl damwra")
time.sleep(10)
os.system("scrapy crawl damwra")

#Compare two json file
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj



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
myDict = {'EffectiveWaterStorageCapacity': 17154.58,
 'MaximumCapacity': '20134.00',
 'PercentageUsedInReservoirCapacity': '31.2',
 'R_ID': 1,
 'TimeStamp': '2017-08-14',
 'WaterLevel': 999}

a =  list(myDict.values())
placeholders = '\"' + '\",\"'.join(map(str, a)) + '\"'
columns = ', '.join(myDict.keys())
sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("ReservoirState", columns, placeholders)
print(sql)
cursor.execute(sql)