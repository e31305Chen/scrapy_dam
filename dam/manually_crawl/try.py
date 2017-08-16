#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

#import os
#os.system("scrapy crawl damwra -o dam2.json")

import MySQLdb
import MySQLdb.cursors
import sys
import os

# def colorcheck(word):
#     if(word == "水情正常"):
#         return('blue')
#     elif(word == "水情稍緊"):
#          return("green")
#     elif(word == "一階限水"):
#          return("yellow")
#     elif(word == "二階限水"):
#          return("orange")
#     elif(word == "三階限水"):
#          return("red")
#     else:
#         return("unknown")
        
# try:
#     conn = MySQLdb.connect(host='localhost',
#                             user='demouser',
#                             passwd='demo1234',
#                             db='demo',
#                             charset='utf8')
# except:
#     print("Can't Connect Database via demouser: ", sys.exc_info()[0])
#     sys.exit()
    
# cursor = conn.cursor() 
# myDict = {'EffectiveWaterStorageCapacity': 17154.58,
#  'MaximumCapacity': '20134.00',
#  'PercentageUsedInReservoirCapacity': '31.2',
#  'R_ID': 1,
#  'TimeStamp': '2017-08-14',
#  'WaterLevel': 999}

# a =  list(myDict.values())
# placeholders = '\"' + '\",\"'.join(map(str, a)) + '\"'
# columns = ', '.join(myDict.keys())
# sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("ReservoirState", columns, placeholders)
# print(sql)
# cursor.execute(sql)

# qmarks = ', '.join('?' * len(myDict))
# qry = "Insert Into ReservoirState (%s) Values (%s)" % (qmarks, qmarks)
# cursor.execute(qry, list(myDict.keys()) + list(myDict.values()))



# I = "3"
# T = "2017/06/03"
# R = colorcheck("二階限水")
# print(I +T+ R)
# sql = "INSERT INTO RegionalWaterRegime (C_ID, TimeStamp, ReservoirLightsNow) VALUES("+I+",\""+T+"\",\""+R+"\")"
# print(sql)
# cursor.execute(sql)

# cursor.close()
# conn.close()

# a = open("/home/ubuntu/workspace/scrapy_dam/dam/damwra_items1.json","r")
# k = a.read().splitlines()  #.replace("\'","")
# print(k)

os.system('/home/ubuntu/workspace/scrapy_dam/dam/ReservoirState.py')