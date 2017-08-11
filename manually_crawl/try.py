#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-

#import os
#os.system("scrapy crawl damwra -o dam2.json")

import MySQLdb
import MySQLdb.cursors

def colorcheck(word):
    if(word == "水情正常"):
        return('blue')
    elif(word == "水情稍緊"):
         return("green")
    elif(word == "一階限水"):
         return("yellow")
    elif(word == "二階限水"):
         return("orange")
    elif(word == "三階限水"):
         return("red")
    else:
        return("unknown")
        
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

I = "3"
T = "2017/06/03"
R = colorcheck("二階限水")
print(I +T+ R)
sql = "INSERT INTO RegionalWaterRegime (C_ID, TimeStamp, ReservoirLightsNow) VALUES("+I+",\""+T+"\",\""+R+"\")"
print(sql)
cursor.execute(sql)

cursor.close()
conn.close()