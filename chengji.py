# -*- coding:utf-8 -*-
subject=("python语言","MySQL数据库","Linux")
stbject = ("小王","小红")
sum = 0
for name in stbject:
    sum = 0
    print ("{}的考试成绩".format(name))
    for i in subject:
        while 1 :
            print("请输入{}成绩：".format(i))
            score = int(input())
            if score < 0 or score > 100:
                print("请重新输入成绩")
                continue
            break
        sum += int(score)
        avg = sum/len(subject)
    print("{}同学的成绩为：{}".format(name,avg))
print ("完成")