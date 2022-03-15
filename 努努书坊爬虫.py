import os
import re
from multiprocessing import Pool
import requests
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
start_url = "https://www.kanunu8.com/book3/7381/"

def get_source(url):
    html = requests.get(url, headers=headers)
    return html.content.decode("gbk")

def get_toc(html):
    toc_url_list = []
    toc_block = re.findall("<strong>正文(.*?)</tbody>", html, re.S)[0]
    toc_url = re.findall('href="(.*?)"', toc_block, re.S)
    for url in toc_url:
        toc_url_list.append(start_url + url)
    return toc_url_list

def get_article(html):
    chapter_name = re.search('size="4">(.*?)<', html, re.S).group(1)
    text_block = re.search('<p>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace("<br>", "")
    text_block = text_block.replace("&nbsp;", "")
    text_block = text_block.replace("<br />","")

    return chapter_name, text_block

def save(chapter, article):
    os.makedirs('通稿2003',exist_ok=True)
    with open(os.path.join('通稿2003', chapter+'.txt'),'w', encoding='utf-8') as f:
        f.write(article)

def query_article(url):
    article_html = get_source(url)
    chapter_name, article_text = get_article(article_html)
    save(chapter_name, article_text)

if __name__ == '__main__':
    toc_html = get_source(start_url)
    toc_list = get_toc(toc_html)
    pool = Pool(4)
    pool.map(query_article, toc_list)

