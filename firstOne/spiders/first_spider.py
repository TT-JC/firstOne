import scrapy
from firstOne.items import FirstoneItem
# import time


class FoodmateSpider(scrapy.Spider):
    name = "foodmate"
    allowed_domains = ["foodmate.net"]
    start_urls = [
        "http://bbs.foodmate.net/forum-19-1.html",
    ]

    def parse(self, response):
        items = []
        for each in response.xpath("// *[@id='threadlisttableid']/tbody"):
            item = FirstoneItem()
            item['name'] = each.xpath("tr/th/a[1]/text()").extract()
            item['href'] = each.xpath("tr/th/a[1]/@href").extract()

            items.append(item)
        print(items)
        return items
        # count = 0
        # for each in response.xpath("//*[@id = 'threadlisttableid']"):
        #     count += 1
        #     print("检测到！！", count)

        # items = []

        # for each in response.xpath("//*[@id = 'threadlisttableid']"):
        #     #

        #     name = each.xpath("tr/th/a[1]/text()")
        #     href = each.xpath("tr/th/a[1]/@href").extract()
        #     print(name, '+')
        #     time.sleep(2)
