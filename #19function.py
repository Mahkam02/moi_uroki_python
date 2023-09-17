# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:42:03 2023

@author: User
"""
#1
def opr_vozrast(imya, god_rojdeniya):
    """funkciya, opredelyayushaya vash vozrast"""
    print(f"{imya.title()}, vash vozrast: ", 2023-int(god_rojdeniya))
#2
def opr_kv_kub(chislo):
    """funkciya, opredelyayushaya kvadrat i kub chisla"""
    print(f'kvadrat chisla {chislo} raven: ', int(chislo)**2)
    print(f'kub chisla {chislo} raven: ', int(chislo)**3)
#3
def chetn_nechetn(chislo1):
    """funkciya opredelyayushaya chetnost chisla"""
    print(f'chislo {chislo1}', end=" ")
    print('chetnoe') if chislo1%2==0  else print('nechetnoe')
#4
def opr_bolshoe(n1, n2):
    """funkciya opredelyayushaya bolshoe chislo iz dvux"""
    if n1>n2:
        print(n1, "bolshe chem", n2)
    elif n1<n2:
        print(n2, "bolshe chem", n1)
    else:
        print(f'chisla {n1} i {n2} ravni')
#5
def vozv_stepen(a, b):
    """funkciya opredelyayushaya a v stepeni b"""
    print(f'{a} v seteni {b} raven', a**b)
#6
def vozv_stepen2(a, b=2):
    """funkciya opredelyayushaya a v stepeni b"""
    print(f'{a} v seteni {b} raven', a**b)
#7
def opr_delimost(n):
    """funkciya opredelyayushaya delimost chisla n ot 2 do 10"""
    for i in range(2, 11):
        if n%i==0:
            print(f'chislo {n} delitsya na {i} bez ostatka')
        else:
            print(f'chislo {n} ne delitsya na {i} bez ostatka')