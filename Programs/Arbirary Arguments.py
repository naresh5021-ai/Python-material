# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:02:05 2020

@author: NARESH
"""
def greet(*names):
    for name in names:
        print("Hello",name)     

greet("Monica","Luke","Steve","John")
