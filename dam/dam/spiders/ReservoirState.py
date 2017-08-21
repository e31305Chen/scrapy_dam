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
import sys
sys.path.append("/home/ubuntu/workspace/scrapy_dam/")
from dbhelper import dbuser_connect
from config import *

class ReservoirstatePySpider(scrapy.Spider):
    name = 'ReservoirState'
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
                "ctl00$cphMain$cboSearch": "所有水庫",
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
        
        #Search in mysql
        def Reservoir_id(name):
            conn = dbuser_connect()
            cursor = conn.cursor() 
            sql = "SELECT * FROM "+MYSQL_CONFIG['db']+".Reservoir WHERE ReservoirName = \""+name+"\""
            try:
                cursor.execute(sql)
                row = cursor.fetchone()
            except:
                print("Make the table Reservoir is not empty. You can create it by \"./CYcrawler.py Reservoir\"")
                sys.exit()
            #print(type(row[0]))
            cursor.close()
            conn.close()
            return(str(row[0]))
            
        #Generate a list of date
        # def dateRange(start, end, step=1, format="%Y-%m-%d"):
        #     strptime, strftime = datetime.datetime.strptime, datetime.datetime.strftime
        #     days = (strptime(end, format) - strptime(start, format)).days
        #     return [strftime(strptime(start, format) + datetime.timedelta(i), format) for i in range(0, days, step)]
            
        # bd = input("Please enter the start crawling date (Default to be \"2005-1-1\")." )
        # if(bd == ""):
        #     bd = "2005-1-1"
        date_list = []#dateRange(bd, time.strftime("%Y-%m-%d"))  #"2005-01-01"
        #date_list = dateRange("2009-05-06", "2009-05-7")
        date_list.append(time.strftime("%Y-%m-%d"))
        w = 0
        #Input all data into item 
        for d in date_list:
            w = w+1
            if(w==5):
                w = 0
                time.sleep(1)
            da = d.split("-")  # tpye is a list of str
            res = PostResponse(int(da[0]),int(da[1]),int(da[2]),soup_get)
            for i in range(0,54,1):
                item['R_ID'] = Reservoir_id(res[0+11*i].get_text())#"1"
                #item['Reservoir'] = res[0+12*i]
                item['TimeStamp'] =  res[7+11*i].get_text()[0:10]  #bs4
                item['WaterLevel'] = res[8+11*i].get_text().replace(',','')
                item['EffectiveWaterStorageCapacity'] = res[9+11*i].get_text().replace(',','')
                item['PercentageUsedInReservoirCapacity'] = res[10+11*i].get_text().replace(',','').replace(' %','') 
                item['MaximumCapacity'] = res[1+11*i].get_text().replace(',','') 
                yield item