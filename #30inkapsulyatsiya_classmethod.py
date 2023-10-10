# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:34:41 2023

@author: User
"""

from uuid import uuid4

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni=0
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil
        self.__id=uuid4()
        Shaxs.__odamlar_soni+=1

    @classmethod 
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
    
    def get_passport(self):
        return self.__passport
    
    def get_id(self):
        return self.__id
    
    def set_passport(self, yangi_passport):
        self.__passport=yangi_passport
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni=0
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = idraqam
        self.fanlar=[]
        self.bosqich = 1
        Talaba.__talabalar_soni+=1
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
    
    def get_idraqam(self):
        return self.__idraqam
    
    def yangi_id(self, yangi_id):
        self.__idraqam=yangi_id
        
    def fanga_yozil(self, fan1):
        self.fanlar.append(fan1)
        
    def remove_fan(self, fan2):
        if fan2 in self.fanlar:
            self.fanlar.remove(fan2)
        else:
            print("Siz bu fanga yozilmagansiz")
        
        
inson = Shaxs("Hasan","Alimov","FB001122",1995)
talaba = Talaba("Valijon","Aliyev","FA112299",2000, "0000012")

print(f"ID: {inson.get_id()}")
print(inson.get_passport())
inson.set_passport("FA1254638")
print(f"Yangi passport nomeri {inson.get_passport()}")