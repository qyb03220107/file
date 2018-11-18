#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Filename  python-practive
#Version V5
#Date 2018-11-07
class Persion:
      def __init__(self,name):
            self.name = name
      def sayHi(self):
            print("Hello,how are you?",self.name)
p = Persion('Swaroop')
p.sayHi()
