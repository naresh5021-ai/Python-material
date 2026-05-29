# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:40:59 2020

@author: NARESH
"""


n=int(input('Enter a number: '))
p=n
s=0
while(n!=0):
    r=n%10
    s=s+(r*r*r)
    n=n//10
if p==s:
    print('The number is Armstrong')
else:
    print('The number is Not Armstrong')
          
