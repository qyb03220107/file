#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Date 2018-11-18
#File: 文件输入/输出的介绍
poem='''\
Program the work is done 
if you wanna make your work also fun;
     use Python
     
     nihao
'''
f = open('poem.txt','w') # 文件写入poem.txt文件里面
f.write(poem)
f.close()

f = open('poem.txt','rt')
while True:
    line = f.readline()  #获取文件的  行数
    if len(line) == 0:
        break
    print(line,end="") #解决输出有空行