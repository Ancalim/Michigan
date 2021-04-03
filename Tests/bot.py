import telebot



from telebot import types

bot = telebot.TeleBot("1733383644:AAH2SXOV74Vihs7xKmAffERqlcTJBYqh-6k")


@bot.message_handler(commands=['start'])    #Приветственное сообщение при активации бота кнопкой "Старт". на строке 15 сам текст+ привязка клавиатуры
def send_welcome(message):
    sticker= open("C:\sticks\sticker3.webp", "rb")
    bot.send_sticker(message.chat.id,sticker)    #Указываем путь на стикер и выводим при start'e
    bot.send_message(message.chat.id, "Привет! Меня зовут Катя и я рада приветствововать Вас! Я телеграм бот компании CakePPSpb. ", reply_markup=keyboard_welcome())
    bot.send_message(message.chat.id, "Подскажите, вы уже выбрали десерт?")
    #keyboard

def keyboard_welcome():   #Вызов клавиатуры и описание кнопок
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    btn1=types.KeyboardButton("Да")
    btn2=types.KeyboardButton("Нет")
    markup.add(btn1,btn2)
    return markup

@bot.message_handler(content_types=['text'])  #Включаем оператор условия с определением выбора ответа, который прислал пользователь.
def order1(message):
    if message.text=="Да":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Черника", callback_data="good",url="https://www.edimdoma.ru/retsepty/73267-tort-muss-chernichnyy-kapriz")
        item2 = types.InlineKeyboardButton("Медовик", callback_data="good", url="https://cookpad.com/ru/recipes/4364656-tort-miedovyi-pukh-ili-miedovik")
        item3 = types.InlineKeyboardButton("Клубника", callback_data="good",url="https://eda.ru/recepty/vypechka-deserty/tort-klubnika-so-slivkami-45079")
        item4 = types.InlineKeyboardButton("Шоколад", callback_data="good",url="https://1000.menu/cooking/36007-prostoi-i-vkusnyi-shokoladnyi-tort")

        markup.add(item1,item2,item3,item4)
        bot.send_message(message.chat.id, "Супер! Выбирайте!",reply_markup=markup)  #Дальше нужно описание десертов или привязка к странице сайта
        bot.send_message(message.chat.id, "После оплаты десерта, наш оператор свяжется с Вами для подтверждения выбранной позиции.  Для возврата на главное меню, воспользуйтесь командой '/start'")

    elif message.text=="Нет":
        refuse1(message)    #Если что, ставим переменную order_refuse=

@bot.message_handler(commands=['Нет'])
def refuse1(message):
    bot.send_message(message.chat.id,"Что вы хотели бы уточнить?",reply_markup=keyboard_refuse1())



def keyboard_refuse1():   #Вызов клавиатуры и описание кнопок
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    btn1=types.KeyboardButton("Связь с оператором")
    btn2=types.KeyboardButton("Состав десертов")
    btn3=types.KeyboardButton("Ассортимент")
    markup.add(btn1,btn2,btn3)
    return markup

@bot.message_handler(commands="Ассортимент")
def raz(message):
    bot.send_message(message.text.id,"asdddd")
















@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Понадобилась помощь? Я помогу! Что именно вы хотите спросить?")

bot.polling(none_stop=True)






#  photo=open("C:\sticks\chernika.jpeg", "rb")
#  bot.send_photo(message.chat.id,photo)
#  bot.send_message(message.chat.id,"Торт 'Черника'")
#  photo = open("C:\sticks\medovik.jpeg", "rb")
#  bot.send_photo(message.chat.id, photo)
#  bot.send_message(message.chat.id,"Торт 'Медовик'")
#  photo = open("C:\sticks\klybnika.jpeg", "rb")
#  bot.send_photo(message.chat.id, photo)
#  bot.send_message(message.chat.id,"Торт 'Клубника'")
#  photo = open("C:\sticks\shoko.jpeg", "rb")
#  bot.send_photo(message.chat.id, photo)
#  bot.send_message(message.chat.id,"Торт 'Шоколад'")