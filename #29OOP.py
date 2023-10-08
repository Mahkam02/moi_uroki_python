# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:50:59 2023

@author: User
"""

class Avto:
    def __init__(self, model, rang, korobka, narx):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narx=narx
        self.kilometr=0
    
    def get_info(self):
        return f"Avtomobil modeli {self.model}, rangi {self.rang}, {self.korobka} korobka, narxi {self.narx} dollar, {self.kilometr} kilometr yurgan."
    
    def update_km(self, kilometr):
        self.kilometr=kilometr
        
class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nomi=nomi
        self.manzili=manzili
        self.avto_soni=0
        self.soyuvdagi_avtolar=[]
    
    def add_avtolar(self, avto):
        self.soyuvdagi_avtolar.append(avto)
        self.avto_soni+=1
        
    def get_avto(self):
        return [avtolar.get_info() for avtolar in self.soyuvdagi_avtolar]
    
avto1=Avto('Gentra', 'qora', 'mexanik', 15000)
avto2=Avto('Cobalt', 'oq', 'avtomat', 12000)
avto1.update_km(2000)
print(avto1.get_info())
print(avto2.get_info())
avtosalon1=Avtosalon('Chevrolet', 'Tashkent')
avtosalon1.add_avtolar(avto1)
avtosalon1.add_avtolar(avto2)
print(avtosalon1.get_avto())

print()
print(dir(Avto))
print(avto1.__dict__)
print(dir(Avtosalon))
print(avtosalon1.__dict__)
print()
print(dir(str))
print(int.__dict__)