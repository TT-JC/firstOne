# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import requests
import json
import copy

# 记得去setting开启


class FirstonePipeline:
    def process_item(self, item, spider):
        return item

# 记得去setting开启


class JbPipeline:

    def open_spider(self, spider):
        # self.file = open('xxx.json', 'wb')

        self.count = 0
        # pass

    def process_item(self, item, spider):

        if self.count == 0:
            self.file = open('/root/x25.json', 'ab+')
        self.count += 1

        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(content.encode("utf-8"))
        if self.count == 5:
            self.file.close()
            self.count = 0

        return item

    def close_spider(self, spider):
        # self.file.close()
        pass
