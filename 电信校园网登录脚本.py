# -*- coding: utf-8 -*-

# @Time    : 2021/10/10 18:04
# @Author  : Suxin
# @File    : 校园网登录.py

import requests
from lxml import etree



# 学校手机号
userId = "19161526795"

# 校园网密码# 默认123456
passwd = "1234567"








success = "离线"
success1 = "修改密码"
# 浏览器标头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31"
}
# 创建地址
url = 'http://172.17.0.2/webauth.do?wlanacname=ZAX_BRAS_JYCJ&wlanuserip=10.2.91.26&mac=44:00:4d:35:e3:d3'
#
data = {
    "loginType": "", "auth_type": "0", "isBindMac1": "0", "pageid": "3", "templatetype": "1", "listbindmac": "0", "recordmac": "0", "isRemind": "1", "loginTimes": "", "groupId": "", "distoken": "", "echostr": "", "url": "", "isautoauth": "", "notice_pic_loop2": "/portal/uploads/pc/demo2/images/bj.png", "notice_pic_loop1": "/portal/uploads/pc/demo2/images/logo.png",
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
# 判断是否登录成功
# '离线'
check = html.xpath("/html/body/form[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div/span/text()")[0]
# '修改密码'
check_r = html.xpath("/html/body/form[1]/div[1]/div[1]/div[2]/div[2]/div[6]/div/span/text()")[0]
# '提示'
title1 = html.xpath("/html/body/form[1]/div[1]/div[1]/div[2]/div[2]/div[4]/p/text()")[0]
# 用户手机号
successTitle = html.xpath("/html/body/form[1]/div[1]/div[1]/div[2]/div[2]/div[3]/text()")[0]
print(successTitle)

print("登录成功-success!", title1) if check == success or check_r == success1 else print("登录失败-false!")
