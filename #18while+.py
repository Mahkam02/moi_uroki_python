# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:24:00 2023

@author: User
"""
#1
print('Pokupaem producti!')
korzina=[]
while True:
    vopros='Chto vi xotite kupit?\n>>>'
    vopros1='Xotite eshyo chto-nibud? (da/net)\n>>>'
    product=input(vopros)
    korzina.append(product)
    otvet=input(vopros1)
    if otvet=='net':
        print('Spasibo!')
        break
print(f'Vi zakazali:')
for i in korzina:
    print(i)
#2
print("Dobavlyaem ceni dlya tovarov!")
ceni={}
while True:
    tovar=input('Vedite nazvaniye tovara: >>>')
    cena=input(f'Vvedite cenu tovara {tovar} (sum): >>>')
    ceni[tovar]=cena
    otv=input('Xotite eshyo dobavit tovari? (da/net) >>>')
    if otv=='net':
        print("Spasibo!")
        break
for tovar1, cena1 in ceni.items():
    print(f"Cena tovara '{tovar1}' {cena1} sum.")
#3
while korzina:
    zakaz=korzina.pop()
    if zakaz in ceni.keys():
        print(f"{zakaz} stoit {ceni[zakaz]}")
    else:
        print(f'Izvinite u nas net producta {zakaz}.')