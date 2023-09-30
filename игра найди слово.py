# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 00:19:48 2023

@author: User
"""

from words import rus_words
import random as r

def play():
    while True:
        slovo=rus_words[r.randint(0, 103)].upper()
        print('Давайте поиграем в игру "Найди слово"')
        print(f"Я подумал слово из {len(slovo)} букв. Сможете ли его найти???")
        bukvi=list()
        kol_pop=0
        slovo1="-"*len(slovo)
        print(slovo1)
        while True:
            bukva=input('\nВведите одну букву или полностью слово:').upper()
            kol_pop+=1
            if bukva not in bukvi and len(bukva)==1:
                bukvi.extend(bukva)
                for i in range(len(slovo)):
                    if len(bukva)==1 and bukva==slovo[i]:
                        print(f"Буква {bukva} правильно!")
                        if i!=len(slovo):
                            slovo1=slovo1[:i]+bukva+slovo1[i+1:]
                        else:
                            slovo1=slovo1[:i]+bukva
                if bukva not in slovo:
                    print("Такой буквы нет.")
            elif 1<len(bukva)<len(slovo) or len(bukva)>len(slovo):
                print('Введите ОДНУ БУКВУ или ПОЛНОСТЬЮ СЛОВО!!!')
            elif bukva in bukvi:
                print(f"Вы раньше ввели букву {bukva}. Введите другую букву.")
            print(slovo1)
            print("Введенные вами буквы: ", end="")
            for j in bukvi:
                print(j, end='')
            print()
            if len(bukva)==len(slovo) and bukva!=slovo:
                print("Неправильно. Попробуйте еще раз.")
            elif bukva==slovo or slovo1==slovo:
                print(f"\nПоздравляю!!! Вы нашли слово {slovo} за {kol_pop} попыток.")
                break
        otv=input("Хотите поиграть еще раз???(да/нет)")
        print()
        if otv=="нет":
            print('\nСпасибо за игру.')
            break

play()