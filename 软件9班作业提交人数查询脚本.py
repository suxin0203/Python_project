# -*- coding: utf-8 -*-

# @Time    : 2021/10/11 18:39
# @Author  : Suxin
# @File    : 作业提交人数查询.py

import os
import os.path
# 查询的文件目录
path = "C:/Users/suxin/Documents/Tencent Files/208082474/FileRecv/1class"

# arr 为遍历文件夹下提交人员名单 arr_all为总人数
arr = []
arr_all = ["刘薇", "张志军", "罗达", "陈同", "马真钛", "宋燕杰", "张自富", "龚飞", "杨利", "陈珂馨", "陈旭林", "张聪", "牛洪", "姜琴", "梁浩", "易友才", "赵礼超", "冯浪", "王江贵", "文海东", "王何平", "李虹成", "龙乙文", "李林辉", "巨鑫", "李婷婷", "闫何", "李青松", "唐宏", "刘川东", "蒋军", "杨海", "陈毅", "王鹏", "吴邦俊", "陈洪印", "王智强", "相博源", "李准", "刘良梁", "李正阳", "邓均", "彭俊杰", "秦洪波", "冯鹏", "马勇", "林春帆", "何东", "任雁宁", "廖豪", "涂浩源", "吴金龙", "顾焕良", "巴丁龙周"]
all = len(arr_all)
count = 0

# 格式化文件名
for parent, dirnames, filenames in os.walk(path):
    for filename in filenames:
        a = ''.join(filename.split())
        b = a.replace('一班', '1班')
        a = b.replace('2020级', '20级')
        arr.append(a)

print(arr)
# 未提交人数 will
will = 1
# 提交判断 t = 1 提交 默认为0
t = 0

# 循环遍历提交人员的名单是否再 总名单里面
for i in range(len(arr)):
    # print(arr_all[i])
    j = arr[i]
    for x in range(len(arr_all)):
        # print(arr[x])
        z = arr_all[x]
        if z in j:
            print("-", z)
            count = count + 1
            arr_all.remove(z)
            break
for y in range(len(arr_all)):
    will = will + 1
    print("未提交：", arr_all[y])
print("-"*50+"")
print("总人数：", all)
print("-"*50+"")
print("总共提交人数：", count)
print("-"*50+"")
print("未提交人数：", will-1)




