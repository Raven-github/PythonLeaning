# -*- coding: utf-8 -*-

import csv

filename = 'C:/Users/Raven/Desktop/煤炭期刊/2017.csv'
file_chonfu='F:/学习/Python/py/Data/chongfu_2017.csv'
file_english='F:/学习/Python/py/Data/english_2017.csv'
file_all='F:/学习/Python/py/Data/all_2017.csv'
s=[]            #没有去重
sets=set()      #去重之后
english=[]      #有多少英文文献
chongfu=[]      #重复文献
setsAll=[]      #去除英文和重复的文献后
with open(filename) as f:
    reader = csv.reader(f)
    lists=list(reader)
    #去掉第一条
    lists.pop(0)
    for item in lists :
        s.append(item[4])
        sets.add(item[4])
        #找到英文期刊
        if "英文" in item[0]:
            english.append(item[4])
s.sort()

#找到重复的
for x in range(1,s.__len__()):
    if s[x]==s[x-1]:
        chongfu.append(s[x])

#去掉重复的和英文的
for item in sets:
    if item in chongfu or item in english:
        pass
    else:
        setsAll.append(item)
# with open(file_chonfu,"w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["name", "quote", "download"])
#     for item in chongfu:
#         writer.writerow([item,0,0])
# with open(file_english,"w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["name", "quote", "download"])
#     for item in english:
#         writer.writerow([item,0,0])
# with open(file_all,"w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["name", "quote", "download"])
#     for item in setsAll:
#         writer.writerow([item,0,0])

print("\n总的篇名为："+str(s.__len__())+"条\n")
print(s)
print("-------------------------------------------------------------------------------------------------------------------")
print("\n\n重复的篇名如下：共有"+str(chongfu.__len__())+"条\n")
print(chongfu)
print("-------------------------------------------------------------------------------------------------------------------")
print("\n\n英文篇名如下：共有"+str(english.__len__())+"条\n")
print(english)
print("-------------------------------------------------------------------------------------------------------------------")
print("\n\n去掉英文和重复篇名后：共有"+str(setsAll.__len__())+"条\n")
print(setsAll)
print("-------------------------------------------------------------------------------------------------------------------")
