# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:46:04 2023

@author: User
"""

#Lambda funksiyasi

# lambda argument: ifoda

# import math
# uzunlik=lambda pi, r: 2*pi*r
# print(uzunlik(math.pi, 10))

# def daraja(n):
#     return lambda x: x**n
# kvadrat=daraja(2)
# kub=daraja(3)
# print(kvadrat(15), kub(45))

#Map funksiyasi

# from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)

# kvadratlar=list(map(lambda x: x**2, range(11)))
# print(kvadratlar)

# a=[1, 5, 9]
# b=[4, 7, 3]
# a_plyus_b=list(map(lambda x, y: x+y, a, b))
# print(a_plyus_b)

# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))

#Filter funksiyasi

# import random as r
# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x%2==0
# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random as r
# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
# juft_sonlar = list(filter(lambda son: son%2==0,sonlar))
# print(sonlar)
# print(juft_sonlar)

# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

# mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)

# print(list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar)))