# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 就是模型类，插入数据库时需要此类
class JianshuItem(scrapy.Item):
    name = title = url = collection = scrapy.Field()
