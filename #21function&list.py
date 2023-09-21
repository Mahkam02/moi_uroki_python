# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:57:53 2023

@author: Mahkam
"""

#1
def zag_bukvoy(teksti):
    for k in range(len(teksti)):
        teksti[k]=teksti[k].title()
    return teksti
imena0=['mahkam', 'shaxrux', 'dolgun', 'suhbat']
print(zag_bukvoy(imena0))
#2
def zag_bukvoy1(teksti):
    teksti1=teksti[:]
    for i in range(len(teksti1)):
        teksti1[i]=teksti1[i].title()
    return teksti1
imena=['mahkam', 'shaxrux', 'dolgun', 'suhbat']
imena1=zag_bukvoy1(imena)
print(imena)
print(imena1)
#3
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)