# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:27:29 2023

@author: User
"""
# #1
# import mod1
# print(mod1.multiply(25, 12))
# #2
# import mod1 as m1
# print(m1.multiply(25, 12))
#3
# from mod1 import multiply
# print(multiply(25, 12))
#4
# from mod1 import multiply as mul
# print(mul(25, 12))
#5
# from mod1 import*
# print(multiply(25, 12))
#6
# import math
# print(math.sqrt(196))
#7
import random as r
# print(r.randint(0, 156))
#8
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) 
# print(ism)
# print(r.choice(ism)) 
#9
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))
#10
x = list(range(11))
print(x)
r.shuffle(x)
print(x)