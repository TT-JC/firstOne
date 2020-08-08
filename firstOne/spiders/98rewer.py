import scrapy
from firstOne.items import JbItem
import bs4
import requests
import json


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

        items = []
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

                item = {}
                item['thread'] = i  # 记录帖子序号
                response_transient = requests.get(
                    response.url + str(item['thread']))  # 获取新url请求内容对象
                soup = bs4.BeautifulSoup(
                    response_transient.text, 'html.parser')  # 对内容进行bs4包装
                head_tag = soup.head  # 定义head的Tag（重复利用）
                if head_tag.select('title').txt:  # 记录帖子标题
                    item['title'] = head_tag.select('title').txt
                else:
                    item['title'] = 'error'
                if head_tag.select('meta')[1]['content']:  # 记录帖子关键字
                    item['keywords'] = head_tag.select('meta')[1]['content']
                else:
                    item['keywords'] = 'error'
                if head_tag.select('meta')[2]['content']:  # 记录帖子描述
                    item['description'] = head_tag.select('meta')[2]['content']
                else:
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
