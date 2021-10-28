# - *- coding: utf- 8 - *-
#import configen


import telebot
#import random
import requests
from telebot import types
from bs4 import BeautifulSoup
import os
import ctypes
from threading import Thread
import schedule
import time




#TOKKEN = "1283231020:AAFi8lJdbMA2HVyrU2OoKdTbIUBH87Az2-c"
TOKKEN = "1483662270:AAEawyO4uHxiZS4xb3jxGeRV_Z9GTxFzz6E"
rool = 0
bot = telebot.TeleBot(TOKKEN)


Headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }


mark = types.ReplyKeyboardMarkup(one_time_keyboard=True)
item = types.KeyboardButton('Тетрадь')
item2 = types.KeyboardButton('Учебник')
mark.add(item,item2)
hideboard = types.ReplyKeyboardRemove()

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Словарь2")
item2 = types.KeyboardButton("Словарь1")
item3 = types.KeyboardButton("/Phy")
item4 = types.KeyboardButton("/Geometry")
item5 = types.KeyboardButton("/Chemestry")
item6=types.KeyboardButton('/English')
item7= types.KeyboardButton('/Russian')
#markup.add(item2)
#markup.add(item1)
markup.add(item3)
markup.add(item4)
markup.add(item5)
markup.add(item6)
markup.add(item7)




@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')


    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!\nЯ - {1.first_name},!\nЯ скидываю дз так то \nЮзай меня полностью\nКомманды:\nPhy - решебник по физике\nGeometry - решебник по геометрии\nChemestry - решение примеров по химии\nEnglish(bETA)-для решения английского языка в тетради\nRussian-для решение заданий по русскому языку'.format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['Phy'])
def Phy(message):

    try:
        msg = bot.send_message(message.chat.id, 'Введите номер')
        bot.register_next_step_handler(msg,Phyy)


    except:
        bot.send_message(message.chat.id,'Секундочку...')
        time.sleep(3)
        msg = bot.send_message(message.chat.id, 'Введите номер')
        bot.register_next_step_handler(msg, Phyy)



def Phyy(message):
    
    number = message.text
    link = f'https://reshak.ru/reshebniki/fizika/10/rimkevich10-11/images1/{number}.png'
    #link = 'https://reshak.ru/reshebniki/fizika/10/rimkevich10-11/images1/'+number+'.png'
    response = requests.get(link)
   # img_option = open("Otvet" + '.jpg', 'wb')
   # img_option.write(response.content)
   # img_option.close()
    if response.status_code==200:

        bot.send_photo(message.chat.id, photo=link)
    else:
        bot.send_message(message.chat.id,'Задания не существует или ссылка не валидная')


@bot.message_handler(commands=['Geometry'])
def Ohy(message):
    try:
        msg = bot.send_message(message.chat.id, 'Введите номер')
        bot.register_next_step_handler(msg,Geo)
    except:
        bot.send_message(message.chat.id, 'Секундочку...')
        time.sleep(3)
        msg = bot.send_message(message.chat.id, 'Введите номер')
        bot.register_next_step_handler(msg, Geo)
def Geo(message):
    number = message.text
    link1 = f'https://reshak.ru/reshebniki/geometriya/10/atanasyan10-11/{number}.png'
    #link1 = 'https://reshak.ru/reshebniki/geometriya/10/atanasyan10-11/'+number+'.png'
    response = requests.get(link1)
    #img_option = open("Otvet" + '.jpg', 'wb')
    #img_option.write(response.content)
    #img_option.close()
    if response.status_code==200:
        bot.send_photo(message.chat.id, photo=link1)
    else:
        bot.send_message(message.chat.id, 'Задания не существует или ссылка не валидная')


@bot.message_handler(commands=['Chemestry'])
def Cmhy(message):
    try:
        msg = bot.send_message(message.chat.id,'Введите формулу без пробелов')
        bot.register_next_step_handler(msg,Chem)
    except:
        bot.send_message(message.chat.id, 'Секундочку...')
        time.sleep(3)
        msg = bot.send_message(message.chat.id, 'Введите формулу без пробелов')
        bot.register_next_step_handler(msg, Chem)

def Chem(message):
    number = message.text
    URL='https://chemiday.com/search/?q='+number
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    response = requests.get(URL,headers = Headers)
    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_='searchresults')
        gg = []
        # print(items)
        # for item in items:
        # compes.append(item.find('img').get('src'))
        # print(compes[0])
        for item in items:
            gg.append(item.find('img').get('src'))

        # print(gg)
        for g in gg[0:3]:
            Url = 'https://chemiday.com/' + str(g)

            bot.send_photo(message.chat.id, photo=Url)
    else:
        bot.send_message(message.chat.id, "Формулы нет")


@bot.message_handler(commands=['wallpapers'])
def wallpapers(message):
    msg = bot.send_message(message.chat.id, 'Отправте ссылку на картинку или саму картинку')
    bot.register_next_step_handler(msg, next_wallpaper)

@bot.message_handler(content_types=["photo"])
def next_wallpaper(message):
    #if 'http:' in message.text:
        #link = message.text
        #response = requests.get(link)
        #img_option = open("image" + '.jpg', 'wb')
        #img_option.write(response.content)
        #img_option.close()
        #path = os.path.abspath("image.jpg")
        #ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

    #else:
    try:
        file6 = message.photo[-1].file_id
        file6 = bot.get_file(file6)
        dfile = bot.download_file(file6.file_path)
        with open("image.jpg", "wb") as img:
            img.write(dfile)
        path = os.path.abspath("image.jpg")
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
        bot.send_message(message.chat.id, 'обои установленны')
    except: next_wallpaper1(message)




def next_wallpaper1(message):
    if 'https:' or 'http:' in message.text:
        link = message.text
        response = requests.get(link)
        if response.status_code ==200:
            img_option = open("image" + '.jpg', 'wb')
            img_option.write(response.content)
            img_option.close()
            path = os.path.abspath("image.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
            bot.send_message(message.chat.id, 'обои установленны')
        else:
            print(message.chat.id,'Ссылка не валидная')



@bot.message_handler(commands=['English'])
def EngCheck(message):
    try:

        #mark = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        #item = types.KeyboardMarkup('Тетрадь')
        #item2 = types.KeyboardMarkup('Учебник')
        #mark.add(item,item2)
        msg = bot.send_message(message.chat.id, 'Тетрадь или учебник', reply_markup=mark)
        bot.register_next_step_handler(msg, Eng)

    except:




        bot.send_message(message.chat.id, 'Секундочку...')
        time.sleep(3)
        #mark = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        #item = types.KeyboardMarkup('Тетрадь')
        #item2 = types.KeyboardMarkup('Учебник')
        #mark.add(item, item2)


        msg = bot.send_message(message.chat.id, 'Тетрадь или учебник',reply_markup=mark)
        bot.register_next_step_handler(msg, Eng)


def Eng(message,):
    global chec
    chec = message.text
    print(chec)


    try:
        msg = bot.send_message( message.chat.id,'Введите номер параграфа', reply_markup=hideboard)
        bot.register_next_step_handler(msg, English)
    except:
        bot.send_message(message.chat.id, 'Секундочку...')
        time.sleep(3)
        msg = bot.send_message(message.chat.id, 'Введите номер параграфа', reply_markup=hideboard)
        bot.register_next_step_handler(msg, English)



def English(message):
    try:
        global J1
        J1 = message.text
        msg = bot.send_message(message.chat.id, "Введите номер раздела")
        bot.register_next_step_handler(msg, English2)
    except:
        print('Problem')

def English2(message):
    try:
        global J2
        J2 = message.text


        msg = bot.send_message(message.chat.id, "Введите номер задания", reply_markup=markup)
        bot.register_next_step_handler(msg, English3)
    except:
        print('Problem')

def English3(message):
    J3 = message.text
    if chec =='Тетрадь':
        link_search = f'https://gdz.ru/class-11/english/verbickaya-forward-workbook/{J1}-{J2}-u-{J3}/'
    elif chec == 'Учебник':
        link_search=f'https://gdz.ru/class-11/english/verbickaya-forward/1-1-u-3/'

    response = requests.get(link_search, headers=Headers)
    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_='with-overtask')
        gg = []
        for item in items:
            gg.append(item.find('img').get('src'))
        for g in gg:
            url = "https:" + str(g)
            bot.send_photo(message.chat.id, photo=url)
    else:
        bot.send_message(message.chat.id, 'Задания нет или ссылка не валидна')



@bot.message_handler(commands=['Russian'])
def Rus(message):
    try:
        msg = bot.send_message(message.chat.id, 'Введите номер задания')
        bot.register_next_step_handler(msg, Russian)
    except:
        bot.send_message(message.chat.id, 'Секундочку...')
        time.sleep(3)
        msg = bot.send_message(message.chat.id, 'Введите номер задания')
        bot.register_next_step_handler(msg, Russian)

def Russian(message):

    gg = message.text
    link = f'https://pomogalka.me/img/10-11-klass-golcova/{gg}.png'
    response = requests.get(link)
    if response.status_code==200:
        bot.send_photo(message.chat.id, photo=link)
    else:
        bot.send_message(message.chat.id,'Задания не существует или ссылка не валидная')

@bot.message_handler(commands=["quizletparse"])
def reurl(message):
    msg = bot.send_message(message.chat.id, "Введите ссылку для парса")
    bot.register_next_step_handler(msg, quizletpar)
def quizletpar(message):
    try:
        def save():
            with open('юнит девять.txt', 'a', encoding='utf8') as file:
                file.write(f'{comp["title"]} => {comp["price"]}\n')

        def parse():
            URL = message.text


            Headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
            }
            response = requests.get(URL, headers=Headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.findAll('div', class_='SetPageTerms-term')
            comps = []

            for item in items:
                comps.append({
                    'title': item.find('span', class_='TermText notranslate lang-en').get_text(strip=True),
                    'price': item.find('span', class_='TermText notranslate lang-ru').get_text(strip=True)
                })
            global comp
            for comp in comps:
                print(f'{comp["title"]} => {comp["price"]}')
                save()
        parse()
    except:
        bot.send_message(message.chat.id, "Что то пошло не так повтори")



@bot.message_handler(content_types=['text'])
def lox(message):

    if message.chat.type == "private":

        if message.text == "Ты потрясающий":

            bot.send_message(message.chat.id, 'Ты потрясающий')






        elif message.text == "Словарь2":

            file = open('Словарик2.txt', encoding='utf8')
            fileR = file.read()
            file.close()

            bot.send_message(message.chat.id, fileR)

        elif message.text =='Словарь1':
            file1 = open('wow.txt', encoding='utf8')
            fileB = file1.read()
            file1.close()
            bot.send_message(message.chat.id, fileB)
        elif message.text=='Словарь3':
            file3 = open('Словарик3.txt', encoding='utf8')
            fileC = file3.read()
            file3.close()
            bot.send_message(message.chat.id, fileC)
        elif message.text=='семь':
            file3 = open('юнит семь.txt', encoding='utf8')
            fileC = file3.read()
            file3.close()
            bot.send_message(message.chat.id, fileC)
        elif message.text =='восемь':
            file4 = open('восемь.txt', encoding='utf8')
            fileD = file4.read()
            file4.close()
            bot.send_message(message.chat.id, fileD)
        elif message.text == "девять":
            file5 = open('юнит девять.txt', encoding='utf8')
            fileG = file5.read()
            file5.close()
            bot.send_message(message.chat.id, fileG)
        else:
            bot.send_message(message.chat.id, "IDI NAHUI")

        #elif message.text =='Физика':

            #bot.send_message(message.chat.id,'Vvedite nomer')



    #number = message.text
    #link = f'https://reshak.ru/reshebniki/fizika/10/rimkevich10-11/images1/{number}.png'
    #response = requests.get(link)
    #img_option = open("Otvet" + '.jpg', 'wb')
    #img_option.write(response.content)
    #img_option.close()

    #bot.send_photo(message.chat.id, photo=link)









bot.polling(none_stop=True)