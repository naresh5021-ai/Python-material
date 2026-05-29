# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:30:42 2020

@author: NARESH
"""


n=int(input('Enter a number'))
a=0
b=1
print(a)
print(b)
while(n-2!=0):
    c=a+b
    print(c)
    a=b
    b=c
    n=n-1
