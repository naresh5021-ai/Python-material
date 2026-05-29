# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:40:59 2020

@author: NARESH
"""


n=int(input('Enter a number'))
p=n
s=0
while(n!=0):
    r=n%10
    s=(s*10)+r
    n=n//10
    print(s)
print('Reverse of {0} is {1}'.format(p,s))
