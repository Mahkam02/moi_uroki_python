# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 23:26:32 2023

@author: User
"""

class User:
    def __init__(self, ism, f_ismi, email, t_yil):
        self.ism=ism
        self.f_ismi=f_ismi
        self.email=email
        self.t_yil=t_yil
    
    def get_info(self):
        return f"Ismim {self.ism}, Foydalanuvchi ismi {self.f_ismi}, email adresim {self.email}, {self.t_yil}chi yilda tug\'ilganman"
    
    def get_ism(self):
        return self.ism
    
    def get_age(self, yil):
        return yil-self.t_yil

user1=User('Maksim', 'Maks007', 'maks@mail.ru', 2000)
user2=User('Rasul', 'Rako', 'rasul@mail.ru', 2002)
user3=User('Nurik', 'Nur', 'nur1k@mail.ru', 2004)

print(user1.ism)
print(user2.f_ismi)
print(user3.email)

print(user1.get_info())
print(user2.get_ism())
print(user3.get_age(2023))        