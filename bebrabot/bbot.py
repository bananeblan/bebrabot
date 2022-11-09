import telebot
from telebot import types

bot = telebot.TeleBot('5330503333:AAFGPo7lVaZVTZY7nEO2xWkfHkepbN5VdDY')


@bot.message_handler(commands=['start'])
def huy(message):
    bot.send_message(message.chat.id, 'добро пожаловать в автоферму =)')


@bot.message_handler(commands=['bebra'])
def button_message(message):
    keyb = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    k1 = types.KeyboardButton('автоферма в вк')
    k2 = types.KeyboardButton('автоферма в телеграме!!!!')
    keyb.add(k1, k2)
    bot.send_message(message.chat.id, 'z', reply_markup=keyb)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'qwe':
        bot.send_message(message.chat.id, 'Спасибо =)')
    elif message.text == 'автоферма в вк':
        bot.send_message(message.chat.id, 'vk.com/avtoferma')
    elif message.text == 'автоферма в телеграме!!!!':
        bot.send_message(message.chat.id, 't.me/avtobebra')
    else:
        bot.send_message(message.chat.id, 'принимаем только бебры')


bot.get_updates()

bot.infinity_polling()
