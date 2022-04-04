# -*- coding: utf-8 -*-

# @Time    : 2021/10/10 18:04
# @Author  : Suxin
# @File    : 校园网登录.py

import requests
from lxml import etree
import random


def run(count1):
    count1 = count1
    num = random.randint(1000, 9999)
    # 学校手机号
    # userId = "1916152" + str(num)
    userId = 19161536696
    # print(userId)
    # 校园网密码# 默认123456
    passwd = "124203"

    success = "离线"
    success1 = "修改密码"
    login = "登 录"
    # 浏览器标头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31"
    }
    # 创建地址
    url = 'http://172.17.0.2/webauth.do?wlanacname=ZAX_BRAS_JYCJ&wlanuserip=10.2.156.238&mac=44:00:4d:35:e3:d3'
    #
    data = {
        "loginType": "", "auth_type": "0", "isBindMac1": "0", "pageid": "3", "templatetype": "1", "listbindmac": "0",
        "recordmac": "0", "isRemind": "1", "loginTimes": "", "groupId": "", "distoken": "", "echostr": "", "url": "",
        "isautoauth": "", "notice_pic_loop2": "/portal/uploads/pc/demo2/images/bj.png",
        "notice_pic_loop1": "/portal/uploads/pc/demo2/images/logo.png",
        "userId": userId,
        "passwd": passwd,
        "remInfo": "on"
    }
    # 请求
    response = requests.post(url=url, headers=headers, data=data)
    r = response.content.decode()
    # 验证网站源码是否反回
    # print(r)
    html = etree.HTML(r)
    check = ""
    check_r = ""
    title1 = ""
    successTitle = ""
    try:
        # 判断是否登录成功
        inputq = html.xpath("/html/body/form[1]/div[1]/div[1]/div[2]/div[2]/div[3]/input/@placeholder")[0]
        # print("未登录成功", inputq)
        count1 = 0
    except:
        # 用户手机号
        successTitle = html.xpath("/html/body/form[1]/div[1]/div[1]/div[2]/div[2]/div[3]/text()")[0]
        # '离线'
        check = html.xpath("/html/body/form[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div/span/text()")[0]
        # 修改密码
        loginn = html.xpath("/html/body/form[1]/div[1]/div[1]/div[2]/div[2]/div[6]/div/span/text()")[0]
        print(successTitle)
        print(check)
        print(loginn)
        count1 = 1
    finally:
        print("登录失败-false!") if loginn == login else print("登录成功-success!")


count1 = 0
run(count1)




# for i in range(100):
#     run(count1)
#     if count1 == 1:
#         break
