#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-
import json
import urllib.request
import sys
import MySQLdb
import MySQLdb.cursors

# Light table
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

# Connect to database
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

# Download open data   
try:
    data_json = urllib.request.urlopen('http://data.gov.tw/iisi/logaccess/51339?dataUrl=https://data.wra.gov.tw/Service/OpenData.aspx?format=json&id=3C082D33-AF41-4558-81A5-7A092E08F845&ndctype=JSON&ndcnid=36695')
    data = json.loads(data_json.read().decode())
except:
    print("Can't Connect to the data server. Maybe the site is under maintain.\n", sys.exc_info()[0],"\nCheck the link below.","\nhttp://data.gov.tw/iisi/logaccess/51339?dataUrl=https://data.wra.gov.tw/Service/OpenData.aspx?format=json&id=3C082D33-AF41-4558-81A5-7A092E08F845&ndctype=JSON&ndcnid=36695")
    sys.exit()

end = len(data['DroughtWarning_OPENDATA'])-1

# Insert into Database 
for i in range(0,end,1):
    I = str(i)
    T = data['DroughtWarning_OPENDATA'][i]['DroughtWarningDate'].replace('/','-')
    R = colorcheck(data['DroughtWarning_OPENDATA'][i]['DroughtWarningStage'])
    sql = "INSERT INTO RegionalWaterRegime (C_ID, TimeStamp, ReservoirLightsNow) VALUES("+I+",\""+T+"\",\""+R+"\")"
    cursor.execute(sql)

# Close DB link
cursor.close()
conn.close()