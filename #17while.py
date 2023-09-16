# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:22:25 2023

@author: Mahkam
"""
#1
question='what book do you like?'
question+='(if you want to stop print "stop")'+'\n>>>'
fbook=''
while fbook!='stop':
    fbook=input(question)
    if fbook!='stop':
        print(f'you like the book "{fbook}"')
#2.1
print('Cena bileta')
question1='\nSkolko vam let? (Chtobi ostanovit napishite "exit" ili "quit")\n>>>'
while True:
    vozrast=input(question1)
    if vozrast=='exit' or vozrast=='quit':
        print('Spasibo!')
        break
    elif int(vozrast)<7:
        print(f"Cena bileta vam 2000sum")
    elif 7<=int(vozrast)<18:
        print(f"Cena bileta vam 3000sum")
    elif 18<=int(vozrast)<65:
        print(f"Cena bileta vam 10000sum")
    elif int(vozrast)>=65:
        print(f"Bilet vam BESPLATNO")
#2.2
print('Cena bileta')
question1='\nSkolko vam let? (Chtobi ostanovit napishite "exit" ili "quit")\n>>>'
flag=True
while flag!=False:
    vozrast=input(question1)
    if vozrast=='exit' or vozrast=='quit':
        print('Spasibo!')
        flag=False
    elif int(vozrast)<7:
        print(f"Cena bileta vam 2000sum")
    elif 7<=int(vozrast)<18:
        print(f"Cena bileta vam 3000sum")
    elif 18<=int(vozrast)<65:
        print(f"Cena bileta vam 10000sum")
    elif int(vozrast)>=65:
        print(f"Bilet vam BESPLATNO")
#3
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")