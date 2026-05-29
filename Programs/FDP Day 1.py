# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:38:37 2020

@author: NARESH
"""

names=['KLH','UNIVERSITY','CSE','ECE','MBA','KLBBA']
print(names[-6][0:3])

a=[1,7,[2],3]
b=list(a)
a[2][0]=4
a[1]=34
print(a)

t=(3,8,9,7,6,2,1)
print(t[1:-1])

print(list(list("KLCSE")))

m=[[x,x+2] for x in range(0,3)]
print(m)

print("KLHLKLHHKLHKLH".count('KLH',0,7))

x=['KLCSE','KLAI']
for i in x:
    i.lower()
print(x)

#print(university=KLH)

print('KLUNIVERSITY'.partition('UN'))

a={1:'K',2:'L',3:'H',4:'C',5:'S',6:'E'}
b=a.copy()
b[2]='D'
print(a)