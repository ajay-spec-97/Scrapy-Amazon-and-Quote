# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#######---- Store extratced data into Item[Containers] --> Store to Database
#                                                      --> Store to csv/json//xml file
import scrapy


class QuotescrapItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()             #these variables are used in spider.py file
    author = scrapy.Field()
    tag = scrapy.Field()
    
