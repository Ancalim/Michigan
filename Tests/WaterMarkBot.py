from PIL import Image, ImageEnhance
import telebot
import os
import time


def read_file(file_name):     #Функция служит для того, что бы не палить токен бота, а читать токен из файла, который храниться в файле на локальной машине.  Личные данные лучше хранить в переменном окружении, надо про это посмотреть видео
    with open(file_name, "r") as file:
        return file.read()

def add_watermark_imp(image,watermark,opacity=1,wm_imterval=0):    #Функция непосредственного создания watermark'a  Библиотека PIL/  Код функции не обьясняют =((((
    if opacity<1:
        if watermark.mode !="RGBA":
            watermark=watermark.convert("RGBA")
        else:
            watermark=watermark.copy()
        alpha=watermark.split()[3]
        alpha=ImageEnchance.Brightness(alpha).enhance(opacity)
        watermark.putalpha(alpha)
    layer=Image.new("RGBA", image.size, (0,0,0,0))
    layer.paste(watermark, (0,0))
    return Image.composite(layer,image,layer)


def add_watermark(image_path,watermark_path):  #Аргументы это 2 пути к изображению и watermark'y
    img=Image.open(image_path) #С помощью библиотеки PIL мы открываем изображение
    watermark = Image.open(watermark_path)  #И так же с PIL мы открываем Watermark
    watermark=watermark.resize((100,100),Image.ANTIALIAS)   #Указываем размеры watermark'a
    result=add_watermark_imp(img,watermark)  #Вызываем дополнительную функцию по добавлению водного знака, тем самым у нас получается новый объект result
    new_path=image_path+"_"+".png"  #Новое имя нашей картинки
    result.save(new_path) #Сохраняем туда же
    return new_path

def clear_content(chat_id):
    try:
        for img in images[chat_id]:  #Поочередно получаем картинки из нашего словаря и удаляем их из нашей папки
            os.remove(img)
    except Exception as e:   #Если чтото пошло не так, то делаем паузу 3 секунды и запускаем функцию заново
        time.sleep(3)
        clear_content(chat_id)
    images[chat_id]=[]


bot = telebot.TeleBot(read_file("token.ini"))
images=dict()

@bot.message_handler(content_types=["text"])
def start(message):
    if message.text=="/go":
        bot.send_message(message.from_user.id, "Submit two photos to add a watermark."+" The first picture is the image itself, and the second will be a watermark")
        bot.register_next_step_handler(message, handle_docs_photo)
    else:
        bot.send_message(message.from_user.id,"To start use command '/go'")

@bot.message_handler(content_types=["photo"])  #Функция срабатывает когда пользователь присылает нам фотографию.
def handle_docs_photo(message):
    print(message.photo[:-2])
    images[str(message.chat.id)]=[]     #Заполняем словарь, в качестве key используем id пользователя. value = пустой список
    try:
        file_info=bot.get_file(message.photo[len(message.photo)-1].file_id)      #Мы пытаемся получить с помощью стандартной функиции get_file  id последней картинки из нашего диалога.   Информация в API
        downloaded_file=bot.download_file(file_info.file_path)   #Скачиваем этот файл с помощью стандартной функции библиотеки
        src = "tmp/" +file_info.file_path    #Указываем куда будет сохраняться картинка (папка tmp в папке проекта) Расширение и вид файла не меняется.

        with open(src,"wb") as new_file:
            new_file.write(downloaded_file)  #Записываем содержимое файла. Тем самым записываем к себе на комп этот файл.

        bot.reply_to(message, "Photo added!")
        images[str(message.chat.id)].append(src)    #Обновляем словарь. Теперь в нем есть key=id пользователя и value как список с картинкой, пока только 1ой
    except Exception as e:
        bot.reply_to(message,e) #Если, что-то не так, то присылаем ошибку

    time.sleep(3)   #Тормозим на 3 секунды
    print('img: ', images)    #xz
    reply_img = ""
    if (len(images[str(message.chat.id)]) == 2):       #Если длинна нашего словаря равно 2 (то есть 2 картинки)
        reply_img=add_watermark(images[str(message.chat.id)][1],images[str(message.chat.id)][0])    #добавляет watermark[1] из словаря images на нашу картинку[0] из словаря images
        images[str(message.chat.id)].append(reply_img)
        bot.send_photo(message.chat.id,open(reply_img, "rb"))   #Возвращаем обратно готовый результат
        clear_content(str(message.chat.id))   #Чистим после отправки наш словарь

bot.polling(none_stop=True, interval=0)



