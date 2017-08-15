# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
import re
import os

from scrapy.exceptions import DropItem
import scrapy
from scrapy.crawler import CrawlerProcess
from dam.spiders.damwra import DamwraSpider

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter

class DamPipeline(object):
    
    
    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.files = {}

    def spider_opened(self, spider):
        file = open('%s_items1.json' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = JsonItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    
    
    
    
#     def open_spider(self, spider):
#         self.conn = MySQLdb.connect(host='localhost',
#                                     user='demouser',
#                                     passwd='demo1234',
#                                     db='demo',
#                                     charset='utf8')
#         self.cursor = self.conn.cursor()
    
#     def check_item(self, item):
#         for key, val in item.items():
#             if re.match('^M', key) or re.match('^Percentage', key):   #挑出M開頭的key
#                 if val and not re.match('^\d+?\.\d+?$', val): #???
#                     item[key] = None
#         return item
        
#     def re_run(self, item):
#         count = 0
#         for key, val in item.items():
#             if(count==3):
#                 item[key] = '---'
#                 print('error in the website server')
#                 break
            
#             if re.match('^TimeStamp', key) or re.match('^R_ID', key):   #挑出M開頭的key
#                 if(val == '--'): 
#                     count = count + 1
# #                    process = CrawlerProcess({
# #                    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# #                    })
# #                    process.crawl(DamwraSpider)
# #                    process.start()
                    
#                     os.system("scrapy crawl damwra -o dam2.json")
#                     break
#         return item
        
#     def process_item(self, item, spider):
#         item = self.check_item(item)
#         #self.re_run(item)
#         self.cursor.execute("""INSERT INTO ReservoirState (R_ID, Reservoir, TimeStamp, WaterLevel, EffectiveWaterStorageCapacity, PercentageUsedInReservoirCapacity, MaximumCapacity) VALUES (%s, %s, %s, %s, %s, %s, %s)""",(
#             item['R_ID'],
#             item['Reservoir'],
#             item['TimeStamp'],
#             item['WaterLevel'],
#             item['EffectiveWaterStorageCapacity'],
#             item['PercentageUsedInReservoirCapacity'],
#             item['MaximumCapacity']
#         ))  
#         self.conn.commit()
#         return item
        
    def close_spider(self, spider):
        #self.conn.close() 
        pass