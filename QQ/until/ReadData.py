# !/usr/bin/python
# -*-coding:utf-8-*-
with open(file=r"D:\QQ\data\数据.txt",mode="r",encoding="utf-8") as fb:
    data=fb.read().split(";")
s=[]
for i  in  data:
   k=i.replace("\n","").split(",")
   print(k)
   s.append(tuple(k))
print(s)







