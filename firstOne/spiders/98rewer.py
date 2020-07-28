import scrapy
from firstOne.items import JbItem
import bs4
import requests


class JbSpider(scrapy.Spider):
    name = "98"
    allowed_domains = ["98rewer.me"]
    start_urls = [
        "https://www.98rewer.me/forum.php?mod=viewthread&tid=",  # 369153
    ]

    def parse(self, response):
        item = JbItem()
        # item['name'] = response.xpath(
        #     "//*[@id='postmessage_2819543']/text()").extract()
        # item['lookTimes'] = response.xpath(
        #     "/html/body/div[6]/div[6]/div[2]/table[1]/tbody/tr/td[1]/div/span[2]/text()").extract()
        # item['replyTimes'] = response.xpath(
        #     "//*[@id='postlist']/table[1]/tbody/tr/td[1]/div/span[5]/text()").extract()

        # item['magnet'] = response.xpath(
        #     "//*[@id = 'code_EWm']/ol/li/text()").extract()
        # item['torrent'] = response.xpath(
        #     "//*[@id='aid634287']/@href").extract()
        # item['torrentMessage'] = response.xpath(
        #     "//*[@id='pid2819543']/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[2]/ignore_js_op/dl/dd/p[3]/text()").extract()
        items = []
        for i in range(1, 370000):  # 0-99
            item = {}
            item['thread'] = i  # 记录帖子序号
            response_transient = requests.get(
                response.url + str(item['thread']))  # 获取新url请求内容对象
            soup = bs4.BeautifulSoup(
                response_transient.text, 'html.parser')  # 对内容进行bs4包装
            head_tag = soup.head  # 定义head的Tag（重复利用）
            if head_tag.select('meta')[2]['content']:  # 记录帖子描述
                item['description'] = head_tag.select(                                           'meta')[2]['content']
            else :
                item['description'] = 'error'
            # print(item)
            # items.append(item)
            yield item  # 获取数据，执行pipe，继续执行
        # return items  # 获取数据结束程序
        # print(requests.get(urlSend))
        #

        # 返回所有子节点的列表
        # print(head_tag)

        # 返回所有子节点的迭代器
        # for child in head_tag.children:
        #     print(child)

        # 循环head标签内部的所有标签的文本（不是属性内的文本）
        # for string in head_tag.strings:
        #     print(repr(string))

        # item['thread'] = 369153  # 记录帖子序号
        # response_transient = requests.get(
        #     response.url + str(item['thread']))  # 获取新url请求内容对象
        # soup = bs4.BeautifulSoup(
        #     response_transient.text, 'html.parser')  # 对内容进行bs4包装
        # head_tag = soup.head
        # # print(head_tag.select('meta')[1])
        # print(head_tag.select('meta')[2]['content'])
        # for meta in head_tag.select('meta'):
        #     print(meta['content'])

        # --------------------下载html内容
        # with open('98-1.html', 'wb') as f:
        #     f.write(response.body)
        # ----------------------------------
        # ----------------通过bs4将获取到的内容写入文本
        # soup = bs4.BeautifulSoup(response.body, 'html.parser')
        # with open('98.txt', 'wb') as file_object:
        #     file_object.write(soup.encode('utf-8'))
        # 写入的内容的形式容易出错，这里使用utf8编码
        # -----------------------------------------
