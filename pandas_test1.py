# encoding: utf-8
# @author: ji ey an so ng
# @file: pandas_test1.py
# @time: 2021/11/6 2:44


import pandas as pd

path = "C:/Users/suxin/Desktop/info.csv"
df = pd.read_csv(path, encoding='gbk')
df1 = df.dropna()
df2 = df1.drop_duplicates()
# print(df2.duplicated(subset=None, keep='first'))
# df2.to_csv("C:/Users/suxin/Desktop/111.csv", encoding='gbk')
bool1 = df2["入会时间"].str.contains("2014")
df3 = df2[bool1]
s1 = df3["入会时间"]
l1 = list(s1)
l2 = []
for i in l1:
    s = i.split("/")
    l2.append(int(s[1]))
s2 = pd.Series(l2)
s2.index = s1.index



