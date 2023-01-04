from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

import telebot
import json
import requests

from telebot import types

# необходимые глобальные переменные
result = ''  # результат, приходящий через get-запрос, приведенный к словарю
len = 0  # количество найденных заведений
cnt = 0  # номер найденного заведения
msg = {  # сообщение, которые выводятся пользователю
    'start': 'Тут можно перекусить.. Что выберешь?)',
    'loc': 'Покажи на карте, где ты находишься\n',
    'call': 'Оо.. Есть еще места, где можно перекусить, можешь выбрать'
}


# функция определения геопозиции введенного пользователем адреса (в частности станции метро) с помощью 2gis
# выполнение запроса к Geocoder API 2gis (get-запрос: gis_geo) с ключом API_key_gis
def func_geo_gis(message):
    query = message.text
    r = requests.get(url=config.gis_geo, params={
        'q': query,
        'key': config.API_key_gis,
        'fields': 'items.point'
    })
    result = json.loads(r.text)
    point = str(result['result']['items'][0]['point']['lon']) + ',' + str(result['result']['items'][0]['point']['lat'])
    return point


# функция поиска по местам с помощью 2gis
# работает с помощью библиотеки requests, запросы отправляются и принимаются согласно документации API поиска по организациям
# выполнение запроса Places API 2gis (get-запрос: gis_search) с ключом API_key_gis
async def func_search_gis(bot, call, point):
    r = requests.get(url=config.gis_search, params={
        'q': call.data,
        'key': config.API_key_gis,
        'point': point,
        'type': 'branch',
        'fields': 'items.point,items.schedule',
        'radius': '100000000'
    })
    global result, cnt
    result = json.loads(r.text)
    cnt = 0
    await func_output_gis(bot, call)


# функция вывода на результатов поиска мест при реализации с помощью 2gis
async def func_output_gis(bot, call):
    if result['meta']['code'] == 200:
        global len
        len = result['result']['total']
        if len == 1:
            text1 = 'Я нашел ' + call.data + '! Но только ' + str(len) + ' ресторан'
        elif (len > 1 and len < 5):
            text1 = 'Я нашел ' + call.data + '! Даже ' + str(len) + ' ресторана'
        else:
            text1 = 'Я нашел ' + call.data + '! Целых ' + str(len) + ' ресторанов'
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(chat_id=call.message.chat.id, text=text1)

        keyboard = InlineKeyboardMarkup()
        if len > 1:
            button = InlineKeyboardButton(text='Хочу другое место', callback_data='var')
            keyboard.add(button)
        button1 = InlineKeyboardButton(text='McDonald’s', callback_data='McDonald’s')
        button2 = InlineKeyboardButton(text='KFC', callback_data='KFC')
        keyboard.add(button1, button2)
        button3 = InlineKeyboardButton(text='Subway', callback_data='Subway')
        button4 = InlineKeyboardButton(text='Burger King', callback_data='Burger King')
        keyboard.add(button3, button4)
        await bot.send_venue(chat_id=call.message.chat.id,
                       latitude=result['result']['items'][0]['point']['lat'],
                       longitude=result['result']['items'][0]['point']['lon'],
                       title=result['result']['items'][0]['name'],
                       address=result['result']['items'][0]['address_name'],
                       reply_markup=keyboard)
    else:
        text1 = 'Ресторанов ' + call.data + ' рядом нет..('
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(chat_id=call.message.chat.id, text=text1)
        await func_inline_button(bot, call.message.chat.id, msg['call'])


# функция смены найденной локации на другую
# происходит перебот элементов в списке с счетчиком cnt
async def func_var(bot, call):
    global cnt
    if cnt < len - 1:
        cnt = cnt + 1
    elif cnt == len - 1:
        cnt = 0
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Выбрать другое место', callback_data='var')
    keyboard.add(button)
    button1 = InlineKeyboardButton(text='McDonald’s', callback_data='McDonald’s')
    button2 = InlineKeyboardButton(text='KFC', callback_data='KFC')
    keyboard.add(button1, button2)
    button3 = InlineKeyboardButton(text='Subway', callback_data='Subway')
    button4 = InlineKeyboardButton(text='Burger King', callback_data='Burger King')
    keyboard.add(button3, button4)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_venue(chat_id=call.message.chat.id,
                   latitude=result['result']['items'][cnt]['point']['lat'],
                   longitude=result['result']['items'][cnt]['point']['lon'],
                   title=result['result']['items'][cnt]['name'],
                   address=result['result']['items'][cnt]['address_name'],
                   reply_markup=keyboard)


# функция создания inline клавиатуры
async def func_inline_button(bot, c_id, text):
    keyboard = InlineKeyboardMarkup(row_width=5)
    button1 = InlineKeyboardButton(text='McDonald’s', callback_data='McDonald’s')
    button2 = InlineKeyboardButton(text='KFC', callback_data='KFC')
    keyboard.add(button1, button2)
    button3 = InlineKeyboardButton(text='Subway', callback_data='Subway')
    button4 = InlineKeyboardButton(text='Burger King', callback_data='Burger King')
    keyboard.add(button3, button4)
    await bot.send_message(c_id, text, reply_markup=keyboard)
