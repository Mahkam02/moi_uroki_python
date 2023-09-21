# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:36:53 2023

@author: Mahkam
"""
#1
def klient(name, surname, year_of_birth, place_of_birth, email, number=''):
    if number:
        klient1={'name':name,
                'surname':surname,
                'year_of_birth':year_of_birth,
                'place_of_birth':place_of_birth,
                'email':email,
                'number':number}
    else:
        klient1={'name':name,
                'surname':surname,
                'year_of_birth':year_of_birth,
                'place_of_birth':place_of_birth,
                'email':email}
    return klient1
#2
print('Vivod info o klientax:')
klienti=[]
while True:
    name=input('Vvedite imya klienta: >>>')
    surname=input('Vvedite familiyu klienta: >>>')
    year_of_birth=int(input('Vvedite god rojdeniye klienta: >>>'))
    place_of_birth=input('Vvedite mesto rojdeniya klienta: >>>')
    email=input('Vvedite email klienta: >>>')
    number=input('Vvedite nomer tel klienta: >>>')
    klienti.append(klient(name, surname, year_of_birth, place_of_birth, email, number))
    again=input('Do you want to continue append "klients"(yes/no)')
    if again=='no':
        break
print('\nKlienti:')
for k in klienti:
    if 'number' in k.keys():
        print(f"klient {k['name']}. Vozrast {2023-k['year_of_birth']}. Nomer:{k['number']}")
    else:
        print(f"klient {k['name']}. Vozrast {2023-k['year_of_birth']}. Nomer:neizvestno")
#3
def bolshiy(a1, a2, a3):
    b=a1
    if a2>b:
        b=a2
    if a3>b:
        b=a3
    return b
#4
def krug(r):
    from math import pi
    krug1={'radius':r,
            'diametr':2*r,
            'perimetr':2*pi*r,
            'ploshad':pi*r**2}
    return krug1
#5
def prostie_chisla(n1, n2):
    a=[]
    for i in range(n1, n2+1):
        flag=True
        for j in range(2, int(n2**0.5)+1):
            if (i%j==0 and i!=2) or i==1:
                flag=False
                break
        if flag:
            a.append(i)
    return a
#6
def fibbonachi(n):
    f=[]
    if n==1:
        f.append(1)
    if n>=2:
        f.extend([1, 1])
    for i in range(n-2):
        f1=f[i]
        f2=f[i+1]
        f3=f1+f2
        f.append(f3)
    return a
