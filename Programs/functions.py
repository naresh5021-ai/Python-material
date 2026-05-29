# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:10:57 2020

@author: NARESH
"""
def hello():
    print('Hello to function')
hello()

def hello(name):
    print('Hello '+name+' Welcome to function')
name=input('Enter your Name')
hello(name)


def add():
    a=1
    b=2
    print(a+b)
add()

def add(a,b):
    print(a+b)
add(2,3)


def add(a,b):
    return(a+b)
c=add(3,4)
print(c)

def add():
    a=4
    b=5
    return(a+b)
c=add()
print(c)

