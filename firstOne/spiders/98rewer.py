import scrapy
from firstOne.items import JbItem
import bs4
import requests
import json
import re


class JbSpider(scrapy.Spider):

    name = "98"
    allowed_domains = ["98rewer.me"]
    start_urls = [
        "https://www.98rewer.me/forum.php?mod=viewthread&tid=",  # 369153
    ]

    def parse(self, response):
        # 过程计数
        count = 0
        item = JbItem()

        # items = []
        with open('/root/x0.json', 'r', encoding='utf-8') as f:  # 打开扫描文件
            # file = open('~/x0.json', 'ab+')  # 打开记录文件
            while 1:
                count += 1  # 过程计数

                jsonLinestr = f.readline()  # 读取一行的的json对象
                if jsonLinestr == '':
                    print('统计完成')
                    break
                jsonLine = json.loads(jsonLinestr)  # 转换数据
                # 筛选数据（目标记录数据）
                i = jsonLine['thread']
                if i <= 204237 or i >= 250000:
                    continue

                item = {}           # 清空字典
                item['thread'] = i  # 记录帖子序号
                response_transient = requests.get(
                    response.url + str(item['thread']))  # 获取新url请求内容对象

                try:
                    self.getcontent(response_transient, item)
                except:
                    continue
                else:
                    yield item
                # print(item)
                # items.append(item)

                # 获取数据，执行pipe，继续执行

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
    def getcontent(self, response, item):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')  # 对内容进行bs4包装
        head_tag = soup.head  # 定义head的Tag（重复利用）
        body_tag = soup.body
        #-*-*-*-*-*-*-*-*-*-*-数据记录-*-*-*-*-*-*-*-*-*-*-*-#
        #---------帖子标题---------#
        if head_tag.title.string:
            item['title'] = head_tag.title.string
        else:
            item['title'] = 'error'
        #---------帖子关键字---------#
        if head_tag.select('meta')[1]['content']:
            item['keywords'] = head_tag.select('meta')[1]['content']
        else:
            item['keywords'] = 'error'
        #---------帖子描述---------#
        if head_tag.select('meta')[2]['content']:
            item['description'] = head_tag.select('meta')[2]['content']
        else:
            item['description'] = 'error'
        #---------发帖时间---------#
        if soup.find_all("em", id=re.compile("^authorposton"))[0].string:
            item['publishtime'] = soup.find_all(
                "em", id=re.compile("^authorposton"))[0].string
        else:
            item['publishtime'] = 'error'
        #---------查看次数---------#
        if soup.find_all("span", class_="xi1")[0].string:
            item['lookTimes'] = soup.find_all("span", class_="xi1")[0].string
        else:
            item['lookTimes'] = 'error'
        #---------回复次数---------#
        if soup.find_all("span", class_="xi1")[1].string:
            item['replyTimes'] = soup.find_all("span", class_="xi1")[1].string
        else:
            item['replyTimes'] = 'error'
