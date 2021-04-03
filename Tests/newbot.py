import telebot



from telebot import types

bot = telebot.TeleBot("1733383644:AAH2SXOV74Vihs7xKmAffERqlcTJBYqh-6k")


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,"hello")
    bot.send_message(message.chat.id, "blalbalbalbla????", reply_markup=keyboard1()) #привязка клавиатуры


def keyboard1():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Da")
    btn2 = types.KeyboardButton("no")
    markup.add(btn1, btn2)
    return markup

@bot.message_handler(content_types=["text"])
def buttonDa(message):
    if message.text=="Da":
        bot.send_message(message.chat.id,"okokok")
    else:
        message.text=="no"
        buttonNo(message)
        #bot.send_message(message.chat.id, "syper, kakoi?", reply_markup=keyboard2())

@bot.message_handler(commands=["no"])
def buttonNo(message):
    bot.send_message(message.chat.id, "blabla", reply_markup=keyboard2())




def keyboard2():
    markup=types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    btn1=types.KeyboardButton("raz")
    btn2=types.KeyboardButton("dva")
    btn3=types.KeyboardButton("tri")
    btn4=types.KeyboardButton("che")
    markup.add(btn1,btn2,btn3,btn4)
    return markup


@bot.message_handler(content_types=["text"])
def buttonNo1(message):
    if message.text=="raz":
        bot.send_message(message.chat.id,"okokok")
    else:
        message.text=="dva"
        buttonNoDva(message)

@bot.message_handler(commands=["dva"])
def buttonNoDva(message):
    bot.send_message(message.chat.id, "blablassSSs", reply_markup=keyboard3())


def keyboard3():
    markup=types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    btn1=types.KeyboardButton("raz")
    btn2=types.KeyboardButton("dva")
    btn3=types.KeyboardButton("trri")
    btn4=types.KeyboardButton("che")
    markup.add(btn1,btn2,btn3,btn4)
    return markup








bot.polling(none_stop=True)