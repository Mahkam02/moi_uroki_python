# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 22:33:21 2023

@author: Mahkam
"""
#1
def multiply(*numbers):
    m=1
    for i in numbers:
        m*=i
    return m
#2
def info_students(name, surname, **students):
    students['name']=name
    students['surname']=surname
    return students