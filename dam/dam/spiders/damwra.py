# -*- coding: utf-8 -*-
import scrapy
from dam.items import DamItem 

class DamwraSpider(scrapy.Spider):
    name = 'damwra'
    allowed_domains = ['fhy.wra.gov.tw']
    start_urls = ['http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx']
        

    
    def parse(self, response):
        item = DamItem()
        res =  response.xpath('//table[@class="list nowrap"]/tr/td/text()').extract() 
        #def float_check_percent(str_float):
        #    if(str_float == '--'):
        #        return('-999')
        #    if(str_float != '--'):
        #        return(str_float.replace(',','').replace(' %',''))
        
        #def float_check(str_float):
        #    if(str_float == '--'):
        #        return('-999')
        #    if(str_float != '--'):
        #        return(float(str_float.replace(',','')))
        
        #Build R_ID dict
        l = [{"SiteId":"-9999","SiteName":"阿公店水庫"},{"SiteId":"-9999","SiteName":"湖山水庫"},{"SiteId":"10201","SiteName":"石門水庫"},{"SiteId":"10203","SiteName":"西勢水庫"},{"SiteId":"10204","SiteName":"新山水庫"},{"SiteId":"10205","SiteName":"翡翠水庫"},{"SiteId":"10206","SiteName":"榮華壩"},{"SiteId":"10207","SiteName":"鳶山堰"},{"SiteId":"10209","SiteName":"桂山壩"},{"SiteId":"10210","SiteName":"三峽攔河堰"},{"SiteId":"10211","SiteName":"青潭堰"},{"SiteId":"10212","SiteName":"直潭壩"},{"SiteId":"10213","SiteName":"羅好壩"},{"SiteId":"10214","SiteName":"阿玉壩"},{"SiteId":"10215","SiteName":"木瓜壩"},{"SiteId":"10401","SiteName":"寶山水庫"},{"SiteId":"10402","SiteName":"青草湖"},{"SiteId":"10403","SiteName":"上坪攔河堰"},{"SiteId":"10404","SiteName":"隆恩堰"},{"SiteId":"10405","SiteName":"寶山第二水庫"},{"SiteId":"10501","SiteName":"永和山水庫"},{"SiteId":"10502","SiteName":"劍潭水庫"},{"SiteId":"10503","SiteName":"大埔水庫"},{"SiteId":"10601","SiteName":"明德水庫"},{"SiteId":"10801","SiteName":"粗坑溪攔河堰"},{"SiteId":"10802","SiteName":"羅東攔河堰"},{"SiteId":"20101","SiteName":"鯉魚潭水庫"},{"SiteId":"20201","SiteName":"德基水庫"},{"SiteId":"20202","SiteName":"石岡壩"},{"SiteId":"20203","SiteName":"谷關壩"},{"SiteId":"20204","SiteName":"八寶攔河堰"},{"SiteId":"20205","SiteName":"天輪壩"},{"SiteId":"20206","SiteName":"馬鞍壩"},{"SiteId":"20207","SiteName":"青山壩"},{"SiteId":"20405","SiteName":"鯉魚潭二期(士林堰)"},{"SiteId":"20501","SiteName":"霧社水庫"},{"SiteId":"20502","SiteName":"日月潭水庫"},{"SiteId":"20503","SiteName":"集集攔河堰"},{"SiteId":"20504","SiteName":"頭社水庫"},{"SiteId":"20505","SiteName":"明潭下池"},{"SiteId":"20506","SiteName":"銃櫃壩"},{"SiteId":"20507","SiteName":"武界壩"},{"SiteId":"20508","SiteName":"明湖下池"},{"SiteId":"30301","SiteName":"仁義潭水庫"},{"SiteId":"30302","SiteName":"蘭潭水庫"},{"SiteId":"30303","SiteName":"鹿寮溪"},{"SiteId":"30304","SiteName":"東口攔河堰"},{"SiteId":"30305","SiteName":"隘寮堰"},{"SiteId":"30306","SiteName":"內埔子"},{"SiteId":"30401","SiteName":"白河水庫"},{"SiteId":"30402","SiteName":"尖山埤"},{"SiteId":"30403","SiteName":"德元埤"},{"SiteId":"30501","SiteName":"烏山頭水庫"},{"SiteId":"30502","SiteName":"曾文水庫"},{"SiteId":"30503","SiteName":"南化水庫"},{"SiteId":"30504","SiteName":"鏡面水庫"},{"SiteId":"30601","SiteName":"虎頭埤"},{"SiteId":"30602","SiteName":"鹽水埤"},{"SiteId":"30603","SiteName":"玉峰攔河堰"},{"SiteId":"30801","SiteName":"澄清湖水庫"},{"SiteId":"30802","SiteName":"阿公店水庫(洩洪至阿公店溪)"},{"SiteId":"30803","SiteName":"鳳山水庫"},{"SiteId":"30804","SiteName":"觀音湖"},{"SiteId":"30805","SiteName":"中正湖"},{"SiteId":"30806","SiteName":"阿公店水庫(洩洪至二仁溪)"},{"SiteId":"30901","SiteName":"高屏溪攔河堰"},{"SiteId":"31001","SiteName":"東港溪攔河堰"},{"SiteId":"31002","SiteName":"甲仙攔河堰"},{"SiteId":"31201","SiteName":"牡丹水庫"},{"SiteId":"31202","SiteName":"龍鑾潭"},{"SiteId":"31301","SiteName":"成功水庫"},{"SiteId":"40201","SiteName":"溪畔壩"},{"SiteId":"40202","SiteName":"水簾壩"},{"SiteId":"40203","SiteName":"龍溪壩"},{"SiteId":"40701","SiteName":"酬勤水庫"},{"SiteId":"50102","SiteName":"興仁水庫"},{"SiteId":"50103","SiteName":"東衛水庫"},{"SiteId":"50104","SiteName":"赤崁水庫"},{"SiteId":"50105","SiteName":"西安水庫"},{"SiteId":"50106","SiteName":"七美水庫"},{"SiteId":"50108","SiteName":"小池水庫"},{"SiteId":"50109","SiteName":"烏溝蓄水塘"},{"SiteId":"50201","SiteName":"太湖水庫"},{"SiteId":"50202","SiteName":"田埔水庫"},{"SiteId":"50203","SiteName":"陽明湖水庫"},{"SiteId":"50204","SiteName":"山西蓄水塘"},{"SiteId":"50205","SiteName":"榮湖水庫"},{"SiteId":"50206","SiteName":"擎天水庫"},{"SiteId":"50207","SiteName":"金沙水庫"},{"SiteId":"50208","SiteName":"蓮湖水庫"},{"SiteId":"50209","SiteName":"菱湖水庫"},{"SiteId":"50210","SiteName":"西湖水庫"},{"SiteId":"50212","SiteName":"金湖水庫"},{"SiteId":"50213","SiteName":"瓊林水庫"},{"SiteId":"50214","SiteName":"蘭湖"},{"SiteId":"50301","SiteName":"勝利水庫"},{"SiteId":"50302","SiteName":"邱桂山水庫"},{"SiteId":"50303","SiteName":"珠螺水壩"},{"SiteId":"50304","SiteName":"儲水沃上壩"},{"SiteId":"50305","SiteName":"儲水沃水庫"},{"SiteId":"50306","SiteName":"津沙水庫"},{"SiteId":"50307","SiteName":"津沙1號壩"},{"SiteId":"50308","SiteName":"板里水庫"},{"SiteId":"50309","SiteName":"東湧水庫"},{"SiteId":"50310","SiteName":"后沃水庫"}]
        R = {}
        for x in range(0,102,1):
            R[l[x]['SiteName']] = l[x]['SiteId'] 
            
            
        for i in range(0,20,1):
            item['R_ID'] = "1"
            #item['Reservoir'] = res[0+12*i]
            item['TimeStamp'] = res[2+12*i][36:46] 
            item['WaterLevel'] = float(res[9+12*i].replace(',',''))
            item['EffectiveWaterStorageCapacity'] = float(res[10+12*i].replace(',',''))
            item['PercentageUsedInReservoirCapacity'] = res[11+12*i].replace(',','').replace(' %','') #float(float_check_percent(res[11+12*i]))
            item['MaximumCapacity'] = res[1+12*i].replace(',','') #float_check(res[1+12*i])
            yield item