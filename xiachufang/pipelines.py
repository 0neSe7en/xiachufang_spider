# -*- coding: utf-8 -*-
import json
import codecs
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiachufangPipeline(object):
    def __init__(self):
        self.file = codecs.open('xcf_2000_.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if item['name'] and item['materials']:
            item['name'] = item['name'][0].strip()
            item['cooked'] = item['cooked'][0].strip()
            item['favourite'] = item['favourite'][0].split(' ')[0].strip()
            item['time'] = item['time'][0].split(' ')[1].strip()
            item['desc'] = map(lambda x: x.strip(), item['desc'])
            item['units'] = map(lambda x: x.strip(), item['units'])
            if item['score']:
                item['score'] = item['score'][0]
            else:
                item['score'] = 0
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
        else:
            raise DropItem("ID:%s not EXIST", item['url'])
        return item
