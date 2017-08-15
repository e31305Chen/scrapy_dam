# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DamItem(scrapy.Item):
    R_ID = scrapy.Field()
    #Reservoir = scrapy.Field()
    TimeStamp = scrapy.Field()
    WaterLevel = scrapy.Field()
    EffectiveWaterStorageCapacity = scrapy.Field()
    PercentageUsedInReservoirCapacity = scrapy.Field()
    MaximumCapacity = scrapy.Field()
