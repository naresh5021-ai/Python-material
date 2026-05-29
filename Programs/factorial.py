# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:09:28 2020

@author: NARESH
"""
n=int(input('Enter a number: '))
i=1
s=1
for i in range(1,n+1):
   s=s*i
#print(s)
print('Factorial of {0} is {1}'.format(n,s))


