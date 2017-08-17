# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from urllib.request import urlopen
from bs4 import SoupStrainer
from urllib.parse import unquote
from urllib.parse import urlencode
from dam.items import DamItem 
import datetime
import time

class ReservoirpaststateSpider(scrapy.Spider):
    name = 'ReservoirPastState'
    allowed_domains = ['fhy.wra.gov.tw']
    start_urls = ['http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx']

    def parse(self, response):
        item = DamItem()
        
        #Get the info for post
        url = "http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx"
        html_get = urlopen(url).read()
        soup_get = BeautifulSoup(html_get, 'html.parser')
        
        #Getting data from by post
        def PostResponse(year,month,date,soup_get):
            viewstate = soup_get.find("input", {"id": "__VIEWSTATE"}).attrs['value']
            viewstategenerator = soup_get.find("input", {"id": "__VIEWSTATEGENERATOR"}).attrs['value']
            snippet = soup_get.find_all('script')[5]
            ctl00_ctl02_HiddenField_encoded = snippet['src'].split('=')[2]
            ctl00_ctl02_HiddenField = " ".join(unquote(ctl00_ctl02_HiddenField_encoded).split("+"))
            postdata = urlencode({
                "ctl00$ctl02": "ctl00$cphMain$ctl00|ctl00$cphMain$btnQuery",
                "ctl00_ctl02_HiddenField": ctl00_ctl02_HiddenField,
                "__EVENTTARGET": "ctl00$cphMain$btnQuery",
                "__EVENTARGUMENT": "",
                "__LASTFOCUS": "",
                "__VIEWSTATE": viewstate,
                "__VIEWSTATEGENERATOR": viewstategenerator,
                "ctl00$cphMain$cboSearch": "防汛重點水庫",
                "ctl00$cphMain$ucDate$cboYear": year,
                "ctl00$cphMain$ucDate$cboMonth": month,
                "ctl00$cphMain$ucDate$cboDay": date,
                "__ASYNCPOST": True
            })
            postdata = postdata.encode("utf-8")
            url = "http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx"
            html_post = urlopen(url, postdata).read()
            soup_post = BeautifulSoup(html_post, 'html.parser')
            only_td_tags = SoupStrainer("td")
            data=soup_post.find_all(only_td_tags)
            return(data)

        #Generate a list of date
        def dateRange(start, end, step=1, format="%Y-%m-%d"):
            strptime, strftime = datetime.datetime.strptime, datetime.datetime.strftime
            days = (strptime(end, format) - strptime(start, format)).days
            return [strftime(strptime(start, format) + datetime.timedelta(i), format) for i in range(0, days, step)]
            
        date_list = dateRange("2017-07-01", time.strftime("%Y-%m-%d"))
        
        #Input all data into item 
        for d in date_list:
            da = d.split("-")  # tpye is a list of str
            res = PostResponse(int(da[0]),int(da[1]),int(da[2]),soup_get)
            for i in range(0,20,1):
                item['R_ID'] = "1"
                #item['Reservoir'] = res[0+12*i]
                item['TimeStamp'] =  res[2+11*i].get_text()[36:46]  #bs4
                item['WaterLevel'] = res[8+11*i].get_text().replace(',','')
                item['EffectiveWaterStorageCapacity'] = res[9+11*i].get_text().replace(',','')
                item['PercentageUsedInReservoirCapacity'] = res[10+11*i].get_text().replace(',','').replace(' %','') 
                item['MaximumCapacity'] = res[1+11*i].get_text().replace(',','') 
                yield item
        
        
        
#===============================================================================================        
        #Example code for just one specific date
        
        #res = PostResponse(2005,1,1,soup_get)
        #print(res)
        # for i in range(0,20,1):
        #     item['R_ID'] = "1"
        #     #item['Reservoir'] = res[0+12*i]
        #     item['TimeStamp'] =  res[2+11*i].get_text()[36:46]  #str(res[2+12*i][36:46]) 
        #     item['WaterLevel'] = res[8+11*i].get_text().replace(',','')#float(res[8+11*i].get_text().replace(',',''))
        #     item['EffectiveWaterStorageCapacity'] = res[9+11*i].get_text().replace(',','')#float(res[9+11*i].get_text().replace(',',''))
        #     item['PercentageUsedInReservoirCapacity'] = res[10+11*i].get_text().replace(',','').replace(' %','') #float(float_check_percent(res[11+12*i]))
        #     item['MaximumCapacity'] = res[1+11*i].get_text().replace(',','') #float_check(res[1+12*i])
        #     yield item