# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:55:28 2023

@author: User
"""
#1
dict_def={'items':'elementi', 'keys':'klyuchevie slova', 'values':'znacheniya',
          'sets':'mnojestva', 'dictionary':'slovar'
          }
for word, definition in sorted(dict_def.items()):
    print(f'{word}-{definition}')
#2
capitals={'Uzbekistan':'Tashkent',
          'Kazaxstan':'Astana',
          'Kirgiziya':'Bishkek',
          'Tadjikistan':'Dushanbe',
          'Turkmenistan':'Ashxabad'}
print('Countries:')
for country in sorted(capitals.keys()):
    print(country)
print('Capitals:')
for capital in sorted(capitals.values()):   
    print(capital)
#3
country1=input('Vvedite gosudarstvo:').title()
print(capitals.get(country1, 'Izvinite, u nas net etoy informacii.'))
#4
menu={'plov':30000,
      'manti':28000,
      'shurva':25000,
      'shashlik':12000,
      'xonim':25000,
      'somsa':15000,
      'pelmeni':24000,
      'chay':5000,
      'kofe':6000,
      'lepyoshka':7000}
zakaz=[]
zakaz.append(input('Zakajite 1-oe blyudo:').lower())
zakaz.append(input('Zakajite 2-oe blyudo:').lower())
zakaz.append(input('Zakajite 3-oe blyudo:').lower())
for meal in zakaz:
    if meal in menu:
        print(f'{meal} stoit {menu[meal]} sum.')
    else:
        print(f'Izvinite, u nas net {meal}.')