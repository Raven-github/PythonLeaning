# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtxbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #文章名字
    name=scrapy.Field()
    #引用次数
    quoteCount=scrapy.Field()
    #下载次数
    download=scrapy.Field()
    pass
