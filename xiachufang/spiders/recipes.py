# -*- coding: utf-8 -*-
import random
from scrapy.spider import Spider
from scrapy.selector import Selector
from ..items import RecipeItem

class RecipesSpider(Spider):
    name = "recipes"
    allowed_domains = ["xiachufang.com"]
    start_urls = []
    index = 0
    for url_line in open("recipes_url_list.txt"):
        start_urls.append(r"http://www.xiachufang.com/recipe/%s/" % url_line.strip())
        index += 1
        if index==2000:
            break
    random.shuffle(start_urls)

    def parse(self, response):
        sel = Selector(response)
        recipe = RecipeItem()
        recipe['url'] = response.url
        recipe['name'] = sel.xpath('//h1[@class="page-title"]/text()').extract()
        if len(recipe['name']):
            recipe['score'] = sel.xpath('//div[@class="overview"]/span[@itemprop="ratingValue"]/text()').extract()
            recipe['cooked'] = sel.xpath('//div[@class="cooked"]/div[@class="overview"]/span[@class="number"]/text()').extract()
            recipe['materials'] = sel.xpath('//td[@class="name has-border"]/a/text()').extract()
            recipe['units'] = sel.xpath('//td[@class="unit has-border"]/text()').extract()
            recipe['desc'] = sel.xpath('//div[@class="desc"]/text()').extract()
            recipe['categories'] = sel.xpath('//div[@class="recipe-cats"]/a/text()').extract()
            recipe['favourite'] = sel.xpath('//div[@class="pv"]/text()').extract()
            recipe['time'] = sel.xpath('//div[@class="time"]/text()').extract()
        return recipe