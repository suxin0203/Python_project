# -*- coding: utf-8 -*-

# @Time    : 2021/8/19 0:09
# @Author  : Suxin
# @File    : 我的微信连三界小说爬取8.23.py
import time

import requests
from lxml import etree


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
}
# 创建地址
url = 'https://www.xquge.com/book/606.html'
# 请求 《我的微信连三界》
response = requests.get(url=url, headers=headers)
r = response.content.decode()

# 验证网站源码是否反回
# print(r)
html = etree.HTML(r)
all_list = html.xpath('/html/body/div[1]/div[6]/div[5]/div[2]/ul/li/a')
title_book = html.xpath('/html/body/div[1]/div[6]/div[2]/div/dl/dt/div[1]/a/text()')[0]
# 验证章节目录返回
data_list = []
for i in all_list:
    temp = {'title': i.xpath('./text()')[0], 'href': i.xpath('./@href')[0]}
    data_list.append(temp)
# 验证章节标题和链接返回
# print(data_list)
fp = open('./'+title_book+'.txt', 'w', encoding='utf-8')
for a in data_list:
    # print(a["href"])
    url1 = a['href']
    title = a['title']
    # 验证遍历链接
    # print(url1)
    response1 = requests.get(url=url1, headers=headers)
    r1 = response1.content.decode()
    # 验证链接对应的章节源码
    # print(r1)
    html1 = etree.HTML(r1)
    all_list1 = html1.xpath('//*[@id="content"]/p/text()')
    print(title, "\n", all_list1, "\n")
    # 爬取延迟0.5s
    time.sleep(0.5)
    fp.write(title + ':' + '\n')
    for p in all_list1:
        # 存储
        fp.write(p + '\n')
    print(title, '爬取成功')
fp.close()





