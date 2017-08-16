#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors
import sys
import os
import time
import json

def run_scrapy():
    if(os.path.isfile('damwra_items1.json') and os.path.isfile('damwra_items2.json')):
        os.remove('damwra_items1.json')
        os.remove('damwra_items2.json')
        os.remove('check_item1.txt')
        os.remove('check_item2.txt')
    os.system("scrapy crawl damwra")
    print("Please wait.....")
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
    l = len(s_list)
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

#run_scrapy()



for t in range(1,5,1):
    dict_item1 = convert2list("/home/ubuntu/workspace/scrapy_dam/dam/damwra_items1.json")
    dict_item2 = convert2list("/home/ubuntu/workspace/scrapy_dam/dam/damwra_items2.json")
    
    if(ordered(dict_item1) == ordered(dict_item2)):
        l = len(dict_item1)
        #print(l)
        #print(dict_item1)
        for i in range(0,l,1):
            myDict = dict_item1[i]
            # Insert object to mysql 
            a =  list(myDict.values())
            values = '\"' + '\",\"'.join(map(str, a)) + '\"'
            column_name = ', '.join(myDict.keys())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("ReservoirState", column_name, values)
            print(i+1,". ",values)
            cursor.execute(sql)
            conn.commit()
            
        print("File comparison pass and has been insert into DB table ReservoirState!")
        break
    else:
        print("comparison is fail. Try ",t," times")
        time.sleep(5)
        run_scrapy()

# Close DB link
cursor.close()
conn.close()
