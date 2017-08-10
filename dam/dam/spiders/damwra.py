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
        for i in range(0,19,1):
            item['Reservoir'] = res[0+12*i]
            item['TimeStamp'] = res[2+12*i][36:46]
            item['WaterLevel'] = res[9+12*i]
            item['EffectiveWaterStorageCapacity'] = res[10+12*i]
            item['PercentageUsedInReservoirCapacity'] = res[11+12*i]
            item['MaximumCapacity'] = res[1+12*i]
            yield item
                
                
