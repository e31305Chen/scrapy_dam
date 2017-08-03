# -*- coding: utf-8 -*-
import scrapy
import urllib
import re 
from io import StringIO

class DamsituSpider(scrapy.Spider):
    name = 'damsitu'
    allowed_domains = ['www.wra.gov.tw']
    start_urls = ['https://www.wra.gov.tw/sp.asp?xdurl=dryInfo/dryInfoDetail.asp']
    
    def parse(self, response):
        res = response.xpath('//table[@class="clear"]//img/@src').extract()
        area = response.xpath('//table[@class="clear"]//div/@class').extract()
        date = response.xpath('//*[@id="MainContent"]/div/div/div/div[2]/div[2]/h2/span/text()').extract()[0][3:10]
        date2 = re.split('[^0-9]',date)
        date2[0] = str(int(date2[0])+1911)
        date3 = date2[0]+"/"+date2[1]+"/"+date2[2]
        l = len(res)
        for i in range(0,l-1,1):
            #file = io.StringIO(urllib.urlopen(res[i]).read())
            #img = Image.open(file)
            yield{
                "img_src": res[i],
                "name": area[i+1],
                "img": date3
                }
                
                