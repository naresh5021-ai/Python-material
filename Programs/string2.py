# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:10:48 2020

@author: NARESH
"""
str1='Naresh Kumar'
str2=str1[1:4]
print(str2)
print(str1[1:5])
print(str1[:])
print(str1[-1])
print(str1[-1:])
print(str1[-5:])
print(str1[:-5])
a='Python Program'
print(a[0])
#a[0]='p'
a=90
st1="green"  
st2="black"
print("Is both Equal:", st1==st2)  
print("Is str1> str2:", st1>st2)  
print("Is str1< str2:", st1<st2)
print("My name is {0} and i secured {1} marks in python".format(str1,a))

#str=input("Enter any string:")  
str='Naresh kumar'
print("String Capitalized:", str.capitalize())  
print("String lower case:", str.lower())  
print("String upper case:", str.upper())  
print("String title case:", str.title())  
print("String swap case:", str.swapcase())
print("String replace case:",str.replace("python","python programming"))
