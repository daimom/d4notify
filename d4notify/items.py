# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class D4NotifyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    d4event = scrapy.Field()
    d4boss = scrapy.Field()
    takePlace = scrapy.Field()
    # pass
