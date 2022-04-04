# -*- coding: utf-8 -*-

# @Time    : 2021/8/19 0:09
# @Author  : Suxin
# @File    : 我的微信连三界小说爬取8.23.py
import time

from lxml import etree
import requests
from multiprocessing.pool import Pool

name = '全职法师'
# 可搜书名、作者名，请少字也别输错字


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
}
# 创建地址 二选一
url = 'https://www.biqugeso.org/searche2.html?searchkey=' + name
url0 = 'https://www.biquge.so/searchd4.html?searchkey=' + name
# 请求 《我的微信连三界》
response = requests.get(url=url, headers=headers)
r = response.content.decode()

# # 验证网站源码是否反回
# print(r)
html = etree.HTML(r)
book_name = html.xpath('/html/body/article/div/div/div/dl')
# print(book_name)
tis = '-' * 30 + '↓' * 20 + "请选择你想下载的小说序号" + '↓' * 20 + '-' * 30 + '\n'
tis1 = '-' * 30 + '↑' * 20 + "请选择你想下载的小说序号" + '↑' * 20 + '-' * 30 + '\n'
tis2 = '-' * 30 + '↓' * 20 + "正在下载" + '↓' * 20 + '-' * 30 + '\n'
title_name = []
num = 0
for n in book_name:
    # print(n.xpath('./dd/text()')[0])
    try:
        p1 = n.xpath('./dd/text()')[0]
    except:
        p1 = "暂无介绍"

    temp = {'title': str(num) + "." + '《' + n.xpath('./dt/a/text()')[0] + '》',
            'page': '内容介绍：' + p1,
            'author': '作者：' + n.xpath('./div/a/text()')[0],
            'href': 'https://www.biquge.so' + n.xpath('./dt/a/@href')[0]}
    title_name.append(temp)
    num = num + 1

print(title_name)
print(tis, tis, tis)
for b in title_name:
    u1 = b['href']
    t1 = b['title']
    a1 = b['author']
    p1 = b['page']
    # 验证遍历链接
    print(t1 + '\n', a1 + '\n', p1 + '\n', u1 + '\n')
print(tis1, tis1, tis1)
num11 = int(input('请输入你想下载的小说序号：\n'))
print('你想下载的小说为：\n' + title_name[num11]['title'] + '\n' + title_name[num11]['author'] + '\n')
print(tis2, tis2, tis2)
response1 = requests.get(url=title_name[num11]['href'], headers=headers)
r1 = response1.content.decode()
html1 = etree.HTML(r1)
# print(r1)
all_list = html1.xpath('/html/body/article[2]/div[1]/dl/a')
# print(all_list)
title_book = title_name[num11]['title']
# html.xpath('/html/body/article[1]/div[1]/a[3]/text()')[0]
# 验证章节目录返回
data_list = []
for i in all_list:
    try:
        p1 = i.xpath('./@title')[0]
    except:
        p1 = "暂无介绍"
    temp = {'title': p1,
            'href': 'https://www.biquge.so' + i.xpath('./@href')[0]}
    data_list.append(temp)
# 验证章节标题和链接返回
# print(data_list)
fp = open('./' + title_book + '.txt', 'w', encoding='utf-8')


#
def down():
    for a in data_list:
        # print(a["href"])
        url1 = a['href']
        title = a['title']
        # 验证遍历链接
        print(url1)
        response1 = requests.get(url=url1, headers=headers)
        r11 = response1.content.decode()
        # 验证链接对应的章节源码
        # print(r1)
        html1 = etree.HTML(r11)
        # print(html1.xpath('/html/body/article/div[5]/div[1]/text()'))
        all_list1 = html1.xpath('/html/body/article/div[5]/div[1]/p/text()')
        print(title, "\n", all_list1, "\n")
        # 爬取延迟0.5s
        time.sleep(0.5)
        fp.write(title + ':' + '\n')
        for p in all_list1:
            # 存储
            fp.write(p + '\n')
        print(title, '爬取成功')
down()




print("开启多线程")
poollist = []
pool = Pool(16)
res3 = pool.map(down, poollist)
print("开启成功")
# pool.close()
# pool.join()
print("线程结束")


fp.close()
print('爬取完毕')
