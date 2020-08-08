# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstoneItem(scrapy.Item):

    name = scrapy.Field()
    href = scrapy.Field()


class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()


class JbItem(scrapy.Item):

    thread = scrapy.Field()         # 序列号
    title = scrapy.Field()          # 标题
    keywords = scrapy.Field()       # 关键字
    description = scrapy.Field()    # 描述
    publishtime = scrapy.Field()    # 发布时间
    lookTimes = scrapy.Field()      # 查看次数
    replyTimes = scrapy.Field()     # 回复次数

    magnet = scrapy.Field()
    torrent = scrapy.Field()
    torrentMessage = scrapy.Field()
