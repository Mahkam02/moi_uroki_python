# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:50:20 2023

@author: User
"""

from transliterate import to_latin, to_cyrillic
import telebot

TOKEN="6485678461:AAEVKJ-7K7-39APsvmTs7NHmiABtCBgOWTs"
bot=telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    otvet="Ассалому алайкум. Добро пожаловать! Xush kelibsiz!"
    otvet+="\nMatn kiriting:"
    otvet+="\nВведите текст:"
    bot.reply_to(message, otvet)

@bot.message_handler(func=lambda message: True)
def kir_lot(message):
    msg=message.text
    otv=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, otv(msg))

bot.infinity_polling()

# tekst=input('Matn kiriting:')

# if tekst.isascii():
#     print(to_cyrillic(tekst))
# else:
#     print(to_latin(tekst))