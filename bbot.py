import telebot
from random import randint
from telebot import types

bot = telebot.TeleBot('5330503333:AAFGPo7lVaZVTZY7nEO2xWkfHkepbN5VdDY')


@bot.message_handler(commands=['start'])
def huy(message):
    bot.send_message(message.chat.id, 'добро пожаловать в автоферму =)')


@bot.message_handler(commands=['bebra'])
def button_message(message):
    keyb = types.InlineKeyboardMarkup()
    k1 = types.InlineKeyboardButton(
        text='автоферма в вк', url='vk.com/avtoferma')
    keyb.add(k1)
    k2 = types.InlineKeyboardButton(
        text='автоферма в телеграме!!!!', url='t.me/avtobebra')
    keyb.add(k2)
    bot.send_message(message.chat.id, 'z', reply_markup=keyb)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'qwe':
        bot.send_message(message.chat.id, 'Спасибо =)')
    elif "бот" in message.text:
        if "иди нахуй" in message.text:
            bot.send_message(message.chat.id, 'Сам иди нахуй, чурка')
        elif "или" in message.text:
            list = message.text.split()
            a = ""
            b = ""
            for i in range(len(list)):
                if list[i] == "или":
                    a = list[i-1]
                    b = list[i+1]
            if randint(0,1) == 0:
                bot.send_message(message.chat.id, a)
            else:
                bot.send_message(message.chat.id, b)
    elif message.text == 'автоферма в вк':
        bot.send_message(message.chat.id, 'vk.com/avtoferma')
    elif message.text == 'автоферма в телеграме!!!!':
        bot.send_message(message.chat.id, 't.me/avtobebra')
    elif 'дс' in message.text:
        bot.send_message(message.chat.id, 'ща зайду')


bot.get_updates()

bot.infinity_polling()
