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

    thread = scrapy.Field()
    title = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    lookTimes = scrapy.Field()
    replyTimes = scrapy.Field()

    magnet = scrapy.Field()
    torrent = scrapy.Field()
    torrentMessage = scrapy.Field()
