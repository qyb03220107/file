#!/usr/bin/env  python
#-*- coding:utf-8 -*-
#Date : 2018-11-08
class SchoolMember:
    '''Represents school member.'''
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        print('Initialized School Merber: %s ', self.name)
    def tell(self):
        '''The my datails.'''
        print("Name : %s ,Age : %s" %  (self.name,self.age))
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print("Initialized Teacher: %s" % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print("Salary: %d" % self.salary)
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('Initialized Student: %s' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: %d' % self.marks)
t = Teacher('Shrividya',40,3000)
s = Student('Swaroop',22,75)
print # prints a blank line
members = [t,s]
for i in members:
    i.tell()
