# -*- coding: utf-8 -*-
import scrapy


class DamwraSpider(scrapy.Spider):
    name = 'damwra'
    allowed_domains = ['fhy.wra.gov.tw']
    start_urls = ['http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx']
    
    def parse(self, response):
        res =  response.xpath('//table[@class="list nowrap"]/tr/td/text()').extract() 
        for i in range(0,19,1):
            yield{
                'name': res[0+12*i],
                'effective capacity': res[1+12*i],
                'start recording time': res[2+12*i],
                'end recording time': res[3+12*i],
                'rainfall(mm)': res[4+12*i],
                'inflow(10^5*m^3)': res[5+12*i],
                'outflow(10^5*m^3)': res[6+12*i],
                'water level change(yesterday)(m)': res[7+12*i],
                'water condition time': res[8+12*i],
                'water level(m)': res[9+12*i],
                'effective water storage((10^5*m^3))': res[10+12*i],
                'storage(%)': res[11+12*i],
                }
