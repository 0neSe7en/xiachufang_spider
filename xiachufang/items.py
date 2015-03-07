# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RecipeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() #
    categories = scrapy.Field() #
    score = scrapy.Field() #
    cooked = scrapy.Field() #
    desc = scrapy.Field() #
    url = scrapy.Field() #
    materials = scrapy.Field() #
    units = scrapy.Field() #
    favourite = scrapy.Field()
    time = scrapy.Field()
