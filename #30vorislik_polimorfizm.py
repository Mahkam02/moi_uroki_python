# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:43:37 2023

@author: Mahkam
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

inson = Shaxs("Hasan","Alimov","FB001122",1995)

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.fanlar=[]
        self.bosqich = 1
        
    def fanga_yozil(self, fan1):
        self.fanlar.append(fan1)
        
    def remove_fan(self, fan2):
        if fan2 in self.fanlar:
            self.fanlar.remove(fan2)
        else:
            print("Siz bu fanga yozilmagansiz")
        
talaba = Talaba("Valijon","Aliyev","FA112299",2000, "0000012")

class Fan:
    def __init__(self, nomi):
        self.nomi=nomi
    
matem=Fan("Matematika")
fizika=Fan("Fizika")
ximiya=Fan("Ximiya")

talaba.fanga_yozil(matem)
talaba.fanga_yozil(ximiya)
talaba.fanga_yozil(fizika)

talaba.remove_fan(matem)

class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, fan, stajyil):
        super().__init__(ism, familiya, passport, tyil)
        self.fan=fan
        self.stajyil=stajyil
        
    def get_staj(self):
        return f"Professor {self.ism} {self.familiya} {self.stajyil} yillik stajga ega"
    
    def get_info(self):
        return f"Professor {self.ism} {self.familiya} {self.tyil}-yili tug'ilgan, {self.fan} fani bo'yicha {self.stajyil} yillik stajga ega"
        
prof1=Professor('Ali', 'Valiyev', 'FA1234567', 1970, "fizika", 30)    
print(prof1.get_staj())
print(prof1.get_info())
   
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, email, til):
        super().__init__(ism, familiya, passport, tyil)
        self.email=email
        self.til=til
        
    def get_email(self):
        return f"Foydalanuvchi {self.ism} emaili: {self.email}"
    
    def get_til(self):
        return f"Foydalanuvchi {self.ism} {self.til} tilini o'rganmoqchi"
        
    def get_info(self):
        return f"Foydalanuvchi {self.ism} {self.familiya} {self.til} tilini o'rganmoqchi, {self.tyil} yili tug'ilgan"
    
foydalanuvchi1=Foydalanuvchi("Sarvar", "Shamsiyev", "AB1597532", 2001, "sarvar@mail.ru", "Python") 
print(foydalanuvchi1.get_info())

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, email, til):
        super().__init__(ism, familiya, passport, tyil, email, til)
    
    def ban_user(self):
        print("Foydalanuvchi bloklandi")
        
admin1=Admin("Nurbek", "Alimov", "AB1234569", 1999, "nur@mail.ru", "Java")
admin1.ban_user()