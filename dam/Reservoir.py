#!/home/ubuntu/.env/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/ubuntu/workspace/scrapy_dam/")
from dbhelper import dbuser_connect

l = [{"ReservoirIdentifier":"-9999","ReservoirName":"阿公店水庫"},{"ReservoirIdentifier":"-9999","ReservoirName":"湖山水庫"},{"ReservoirIdentifier":"10201","ReservoirName":"石門水庫"},{"ReservoirIdentifier":"10203","ReservoirName":"西勢水庫"},{"ReservoirIdentifier":"10204","ReservoirName":"新山水庫"},{"ReservoirIdentifier":"10205","ReservoirName":"翡翠水庫"},{"ReservoirIdentifier":"10206","ReservoirName":"榮華壩"},{"ReservoirIdentifier":"10207","ReservoirName":"鳶山堰"},{"ReservoirIdentifier":"10209","ReservoirName":"桂山壩"},{"ReservoirIdentifier":"10210","ReservoirName":"三峽攔河堰"},{"ReservoirIdentifier":"10211","ReservoirName":"青潭堰"},{"ReservoirIdentifier":"10212","ReservoirName":"直潭壩"},{"ReservoirIdentifier":"10213","ReservoirName":"羅好壩"},{"ReservoirIdentifier":"10214","ReservoirName":"阿玉壩"},{"ReservoirIdentifier":"10215","ReservoirName":"木瓜壩"},{"ReservoirIdentifier":"10401","ReservoirName":"寶山水庫"},{"ReservoirIdentifier":"10402","ReservoirName":"青草湖"},{"ReservoirIdentifier":"10403","ReservoirName":"上坪攔河堰"},{"ReservoirIdentifier":"10404","ReservoirName":"隆恩堰"},{"ReservoirIdentifier":"10405","ReservoirName":"寶山第二水庫"},{"ReservoirIdentifier":"10501","ReservoirName":"永和山水庫"},{"ReservoirIdentifier":"10502","ReservoirName":"劍潭水庫"},{"ReservoirIdentifier":"10503","ReservoirName":"大埔水庫"},{"ReservoirIdentifier":"10601","ReservoirName":"明德水庫"},{"ReservoirIdentifier":"10801","ReservoirName":"粗坑溪攔河堰"},{"ReservoirIdentifier":"10802","ReservoirName":"羅東攔河堰"},{"ReservoirIdentifier":"20101","ReservoirName":"鯉魚潭水庫"},{"ReservoirIdentifier":"20201","ReservoirName":"德基水庫"},{"ReservoirIdentifier":"20202","ReservoirName":"石岡壩"},{"ReservoirIdentifier":"20203","ReservoirName":"谷關壩"},{"ReservoirIdentifier":"20204","ReservoirName":"八寶攔河堰"},{"ReservoirIdentifier":"20205","ReservoirName":"天輪壩"},{"ReservoirIdentifier":"20206","ReservoirName":"馬鞍壩"},{"ReservoirIdentifier":"20207","ReservoirName":"青山壩"},{"ReservoirIdentifier":"20405","ReservoirName":"鯉魚潭二期(士林堰)"},{"ReservoirIdentifier":"20501","ReservoirName":"霧社水庫"},{"ReservoirIdentifier":"20502","ReservoirName":"日月潭水庫"},{"ReservoirIdentifier":"20503","ReservoirName":"集集攔河堰"},{"ReservoirIdentifier":"20504","ReservoirName":"頭社水庫"},{"ReservoirIdentifier":"20505","ReservoirName":"明潭下池"},{"ReservoirIdentifier":"20506","ReservoirName":"銃櫃壩"},{"ReservoirIdentifier":"20507","ReservoirName":"武界壩"},{"ReservoirIdentifier":"20508","ReservoirName":"明湖下池"},{"ReservoirIdentifier":"30301","ReservoirName":"仁義潭水庫"},{"ReservoirIdentifier":"30302","ReservoirName":"蘭潭水庫"},{"ReservoirIdentifier":"30303","ReservoirName":"鹿寮溪"},{"ReservoirIdentifier":"30304","ReservoirName":"東口攔河堰"},{"ReservoirIdentifier":"30305","ReservoirName":"隘寮堰"},{"ReservoirIdentifier":"30306","ReservoirName":"內埔子"},{"ReservoirIdentifier":"30401","ReservoirName":"白河水庫"},{"ReservoirIdentifier":"30402","ReservoirName":"尖山埤"},{"ReservoirIdentifier":"30403","ReservoirName":"德元埤"},{"ReservoirIdentifier":"30501","ReservoirName":"烏山頭水庫"},{"ReservoirIdentifier":"30502","ReservoirName":"曾文水庫"},{"ReservoirIdentifier":"30503","ReservoirName":"南化水庫"},{"ReservoirIdentifier":"30504","ReservoirName":"鏡面水庫"},{"ReservoirIdentifier":"30601","ReservoirName":"虎頭埤"},{"ReservoirIdentifier":"30602","ReservoirName":"鹽水埤"},{"ReservoirIdentifier":"30603","ReservoirName":"玉峰攔河堰"},{"ReservoirIdentifier":"30801","ReservoirName":"澄清湖水庫"},{"ReservoirIdentifier":"30802","ReservoirName":"阿公店水庫(洩洪至阿公店溪)"},{"ReservoirIdentifier":"30803","ReservoirName":"鳳山水庫"},{"ReservoirIdentifier":"30804","ReservoirName":"觀音湖"},{"ReservoirIdentifier":"30805","ReservoirName":"中正湖"},{"ReservoirIdentifier":"30806","ReservoirName":"阿公店水庫(洩洪至二仁溪)"},{"ReservoirIdentifier":"30901","ReservoirName":"高屏溪攔河堰"},{"ReservoirIdentifier":"31001","ReservoirName":"東港溪攔河堰"},{"ReservoirIdentifier":"31002","ReservoirName":"甲仙攔河堰"},{"ReservoirIdentifier":"31201","ReservoirName":"牡丹水庫"},{"ReservoirIdentifier":"31202","ReservoirName":"龍鑾潭"},{"ReservoirIdentifier":"31301","ReservoirName":"成功水庫"},{"ReservoirIdentifier":"40201","ReservoirName":"溪畔壩"},{"ReservoirIdentifier":"40202","ReservoirName":"水簾壩"},{"ReservoirIdentifier":"40203","ReservoirName":"龍溪壩"},{"ReservoirIdentifier":"40701","ReservoirName":"酬勤水庫"},{"ReservoirIdentifier":"50102","ReservoirName":"興仁水庫"},{"ReservoirIdentifier":"50103","ReservoirName":"東衛水庫"},{"ReservoirIdentifier":"50104","ReservoirName":"赤崁水庫"},{"ReservoirIdentifier":"50105","ReservoirName":"西安水庫"},{"ReservoirIdentifier":"50106","ReservoirName":"七美水庫"},{"ReservoirIdentifier":"50108","ReservoirName":"小池水庫"},{"ReservoirIdentifier":"50109","ReservoirName":"烏溝蓄水塘"},{"ReservoirIdentifier":"50201","ReservoirName":"太湖水庫"},{"ReservoirIdentifier":"50202","ReservoirName":"田埔水庫"},{"ReservoirIdentifier":"50203","ReservoirName":"陽明湖水庫"},{"ReservoirIdentifier":"50204","ReservoirName":"山西蓄水塘"},{"ReservoirIdentifier":"50205","ReservoirName":"榮湖水庫"},{"ReservoirIdentifier":"50206","ReservoirName":"擎天水庫"},{"ReservoirIdentifier":"50207","ReservoirName":"金沙水庫"},{"ReservoirIdentifier":"50208","ReservoirName":"蓮湖水庫"},{"ReservoirIdentifier":"50209","ReservoirName":"菱湖水庫"},{"ReservoirIdentifier":"50210","ReservoirName":"西湖水庫"},{"ReservoirIdentifier":"50212","ReservoirName":"金湖水庫"},{"ReservoirIdentifier":"50213","ReservoirName":"瓊林水庫"},{"ReservoirIdentifier":"50214","ReservoirName":"蘭湖"},{"ReservoirIdentifier":"50301","ReservoirName":"勝利水庫"},{"ReservoirIdentifier":"50302","ReservoirName":"邱桂山水庫"},{"ReservoirIdentifier":"50303","ReservoirName":"珠螺水壩"},{"ReservoirIdentifier":"50304","ReservoirName":"儲水沃上壩"},{"ReservoirIdentifier":"50305","ReservoirName":"儲水沃水庫"},{"ReservoirIdentifier":"50306","ReservoirName":"津沙水庫"},{"ReservoirIdentifier":"50307","ReservoirName":"津沙1號壩"},{"ReservoirIdentifier":"50308","ReservoirName":"板里水庫"},{"ReservoirIdentifier":"50309","ReservoirName":"東湧水庫"},{"ReservoirIdentifier":"50310","ReservoirName":"后沃水庫"}]

conn = dbuser_connect()
cursor = conn.cursor() 

for x in range(0,len(l),1):
    myDict = l[x]
    a =  list(myDict.values())
    values = '\"' + '\",\"'.join(myDict.values()) + '\"'
    column_name = ', '.join(myDict.keys()) 
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("Reservoir", column_name, values)
    print(x+1,". ",values)
    print(sql)
    cursor.execute(sql)
    conn.commit()

# Close DB link
cursor.close()
conn.close()

print("Done!!")

