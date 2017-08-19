# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
import re
import os
from datetime import datetime

from scrapy.exceptions import DropItem
import scrapy
from scrapy.crawler import CrawlerProcess
from dam.spiders.damwra import DamwraSpider

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import JsonLinesItemExporter

class DamPipeline(object):
    def check_item(self, item):
        if (item['MaximumCapacity'] != "--"):
            a = datetime.strptime(item['TimeStamp'], '%Y-%m-%d')
            b = datetime.strptime("2017-01-01", '%Y-%m-%d')
            if(a<b):
                if(float(item['EffectiveWaterStorageCapacity']) > (float(item['MaximumCapacity'])*1.1)): #用1.1被去篩選，考慮到淤積因素
                    item['EffectiveWaterStorageCapacity'] = -888
            else:
                if(float(item['EffectiveWaterStorageCapacity']) > float(item['MaximumCapacity'])): #2017年後只要大於就排除
                    item['EffectiveWaterStorageCapacity'] = -888  
        else:
            if item['EffectiveWaterStorageCapacity'] and not re.match('^\d+?\.\d+?$', item['EffectiveWaterStorageCapacity']): #check format
                item['EffectiveWaterStorageCapacity'] = -999
            else:
                if(float(item['EffectiveWaterStorageCapacity']) > 100000):
                    item['EffectiveWaterStorageCapacity'] = -888
        
        for key, val in item.items():
            if( re.match('^Max', key) or re.match('^Percentage', key) or re.match('^Water', key) ):   #select key from item   or re.match('^Effective', key)
                if val and not re.match('^\d+?\.\d+?$', val): #check format
                    item[key] = -999  # can use None or NULL
            if re.match('^TimeStamp',key):
                if val == "--\r\n      ":
                    raise DropItem("Missing value in %s" % item)
        return item
    
    def __init__(self):
        path = os.path.abspath("dir.txt").replace("dir.txt","") # To find the path
        print("Download file is set to be this path: ",path,"\nIf it's not right please make sure dir.txt file is at the same location of the execute file.py")
        
        if(os.path.isfile(path + "damwra_items1.json") and os.path.isfile(path + "damwra_items2.json")):
            print('Err: damwra_items1.json & damwra_items2.json are already exist.')
        elif(os.path.isfile(path +'ReservoirPastState_items1.json') and os.path.isfile(path +'ReservoirPastState_items2.json')):
            print('Err: ReservoirPastState_items1.json & ReservoirPastState_items2.json are already exist.')
        else:
            dispatcher.connect(self.spider_opened, signals.spider_opened)
            dispatcher.connect(self.spider_closed, signals.spider_closed)
            self.files = {}
            
    def spider_opened(self, spider):
        path = os.path.abspath("dir.txt").replace("dir.txt","")
        # For checking usage
        if(os.path.isfile(path +'check_item1.txt')):
            if(os.path.isfile(path +'check_item2.txt')):
                print('check_item2 is already exist.')
            else:
                file = open('%s_items2.json' % spider.name, 'w+b')
                self.files[spider] = file
                self.exporter = JsonLinesItemExporter(file)
                self.exporter.start_exporting()
                print('check_item1 is already exist.')
        else:
            file = open('%s_items1.json' % spider.name, 'w+b')
            self.files[spider] = file
            self.exporter = JsonLinesItemExporter(file)
            self.exporter.start_exporting()

    def spider_closed(self, spider):
        path = os.path.abspath("dir.txt").replace("dir.txt","")
        print("Download file is set to be this path: ",path,"\nIf it's not right please make sure dir.txt file is at the same location of the execute file.py")
        if(os.path.isfile(path +'check_item1.txt') and os.path.isfile(path +'check_item2.txt')):
            print('check_item1 and check_item2 are already exist.',"\nNothing change in DB.")
        else:
            self.exporter.finish_exporting()
            file = self.files.pop(spider)
            file.close()
            
        if(os.path.isfile(path +'damwra_items1.json') or os.path.isfile(path +'ReservoirPastState_items1.json')):
            file = open('check_item1.txt', 'w')
            file.write("This is for scrapy to check item accuracy")
            file.close()
        
        if(os.path.isfile(path +'damwra_items2.json') or os.path.isfile(path +'ReservoirPastState_items2.json')):
            file = open('check_item2.txt', 'w')
            file.write("This is for scrapy to check item accuracy")
            file.close()

    def process_item(self, item, spider):
        path = os.path.abspath("dir.txt").replace("dir.txt","")
        item = self.check_item(item)
        if(os.path.isfile(path +'check_item1.txt') and os.path.isfile(path +'check_item2.txt')):
            print('File exist!!')
        else:
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
        
    # def close_spider(self, spider):
    #     #self.conn.close() 
    #     pass# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import MySQLdb
# import MySQLdb.cursors
# import re
# import os

# from scrapy.exceptions import DropItem
# import scrapy
# from scrapy.crawler import CrawlerProcess
# from dam.spiders.damwra import DamwraSpider

# from scrapy.xlib.pydispatch import dispatcher
# from scrapy import signals
# from scrapy.contrib.exporter import JsonLinesItemExporter

# class DamPipeline(object):
#     def check_item(self, item):
#         for key, val in item.items():
#             if re.match('^M', key) or re.match('^Percentage', key):   #挑出M開頭的key
#                 if val and not re.match('^\d+?\.\d+?$', val): #???
#                     item[key] = -999  # can use None or NULL
#         return item
    
#     def __init__(self):
#         if(os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/damwra_items1.json') and os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/damwra_items2.json')):
#             print('File exist!!')
#         else:
#             dispatcher.connect(self.spider_opened, signals.spider_opened)
#             dispatcher.connect(self.spider_closed, signals.spider_closed)
#             self.files = {}

#     def spider_opened(self, spider):
        
#         # For checking usage
#         if(os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/check_item1.txt')):
#             if(os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/check_item2.txt')):
#                 print('file exist')
#             else:
#                 file = open('%s_items2.json' % spider.name, 'w+b')
#                 self.files[spider] = file
#                 self.exporter = JsonLinesItemExporter(file)
#                 self.exporter.start_exporting()
#         else:
#             file = open('%s_items1.json' % spider.name, 'w+b')
#             self.files[spider] = file
#             self.exporter = JsonLinesItemExporter(file)
#             self.exporter.start_exporting()

#     def spider_closed(self, spider):
#         if(os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/check_item1.txt') and os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/check_item2.txt')):
#             print('File exist!!')
#         else:
#             self.exporter.finish_exporting()
#             file = self.files.pop(spider)
#             file.close()
            
#         if(os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/damwra_items1.json')):
#             file = open('check_item1.txt', 'w')
#             file.write("This is for scrapy to check item accuracy")
#             file.close()
        
#         if(os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/damwra_items2.json')):
#             file = open('check_item2.txt', 'w')
#             file.write("This is for scrapy to check item accuracy")
#             file.close()

#     def process_item(self, item, spider):
#         item = self.check_item(item)
#         if(os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/check_item1.txt') and os.path.isfile('/home/ubuntu/workspace/scrapy_dam/dam/check_item2.txt')):
#             print('File exist!!')
#         else:
#             self.exporter.export_item(item)
#             return item
        
    
    
    
    
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
        
    # def close_spider(self, spider):
    #     #self.conn.close() 
    #     pass