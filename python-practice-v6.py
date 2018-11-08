#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Create class file
#Date: 2018-11-08
# Total population statistics
class Person:
    ''' Represents person.'''
    population = 0
    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name = name
        print('Initializing %s'% self.name)
        Person.population += 1
    def __del__(self):
        '''I am dying.'''
        print('%s says bye.' % self.name)
        Person.population -= 1
        if Person.population == 0:
            print("I am the last one.")
        else:
            print("There are still %d pepople left." % Person.population)
    def sayHi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print("Hi, my name is %s." % self.name)
    def howMary(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print("I am the only person here")
        else:
            print("We have %d person here." % Person.population)
swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMary()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMary()
swaroop.sayHi()
swaroop.howMary()