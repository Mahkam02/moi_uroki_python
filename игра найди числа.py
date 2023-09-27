# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:48:57 2023

@author: User
"""

# Игра "Найди задуманное число"
import random as r

while True:
    print('Давайте поиграем в игру "Найти задуманное число"')
    print('\nЯ задумал одно число от 1 до 10. Сможете найти???')
    n1=r.randint(1, 10)
    kol_popitok=0
    while True:
        n11=int(input('>>>'))
        kol_popitok+=1
        if n11>n1:
            print(f'Неправильно. Моё задуманное число меньше {n11}')
        elif n11<n1:
            print(f'Неправильно. Моё задуманное число больше {n11}')
        elif n11==n1:
            print('Правильно, поздравляю!!!')
            print(f"Я задумал число {n11}")
            print(f"Количество ваших попыток {kol_popitok}")
            break
    
    print("\nА теперь вы подумайте одно число от 1 до 10. Я попытаюсь найти его.") 
    gotov=input("Если подумали нажмите любую букву на клавивтуре. >>>")
    if gotov:
        n21=r.randint(1, 10)
        kol_popitok1=1
        while True: 
            print(f'Вы подумали число {n21}')
            otv=input("(Если правильно пишите 'T', если моё число меньше '-', если моё число больше '+')>>>")
            if otv=="+":
                n21=r.randint(1, n21-1)
                kol_popitok1+=1
            elif otv=="-":
                n21=r.randint(n21+1, 10)
                kol_popitok1+=1
            elif otv=="T":
                print(f"Я нашёл ваше число за {kol_popitok1} попытки.")
                break
    
    print(f"\nКоличество ваших попыток {kol_popitok}")
    print(f"Я нашёл ваше число за {kol_popitok1} попытки.")
    if kol_popitok>kol_popitok1:
        print('Я выиграл. Вы проиграли.')
    elif kol_popitok<kol_popitok1:
        print('Вы выиграли. Поздравляю!!!')
    elif kol_popitok==kol_popitok1:
        print('Ничья.')
    otv1=input('Хотите ещё раз поиграть? (да\нет) >>>') 
    if otv1=='да':
        continue
    elif otv1=='нет':
        print("\nСпасибо за игру!!!")
        break