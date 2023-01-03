from aiogram import types

import functions
from config import *
import sql_data as sq, keyboards as kb
point = ''


def register_handler(dp: dp):
    dp.message_handler(commands=['start'])


@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    user_id = m.from_user.id
    sq.check_user(user_id)
    await bot.send_message(m.chat.id, "Welcome! You can choose the language : ", reply_markup=kb.inline_kb_markup)


@dp.callback_query_handler(text='ru')
async def lang_ru(c: types.CallbackQuery):
    user_id = c.from_user.id
    sq.lang_update(user_id, 'ru')
    lang = sq.ans_lang(user_id)
    hello = sq.ans_hello(lang)
    await c.message.answer(hello, reply_markup=kb.inline_kb(user_id, lang))


@dp.callback_query_handler(text='en')
async def lang_ru(c: types.CallbackQuery):
    user_id = c.from_user.id
    sq.lang_update(user_id, 'en')
    lang = sq.ans_lang(user_id)
    hello = sq.ans_hello(lang)
    await c.message.answer(hello, reply_markup=kb.inline_kb(user_id, lang))


@dp.callback_query_handler(text='tr')
async def lang_ru(c: types.CallbackQuery):
    user_id = c.from_user.id
    sq.lang_update(user_id, 'tr')
    lang = sq.ans_lang(user_id)
    hello = sq.ans_hello(lang)
    await c.message.answer(hello, reply_markup=kb.inline_kb(user_id, lang))


@dp.callback_query_handler(text='commands')
async def command(c: types.CallbackQuery):
    user_id = c.from_user.id
    lang = sq.ans_lang(user_id)
    commands_answer = sq.ans_commands_answer(lang)
    await c.message.answer(commands_answer)
    await c.message.delete()


@dp.callback_query_handler(text='services')
async def services(c: types.CallbackQuery):
    user_id = c.from_user.id
    lang = sq.ans_lang(user_id)
    services_answer = sq.ans_services_answer(lang)
    await c.message.answer(services_answer, reply_markup=kb.inline_kb_services(user_id,lang))


@dp.callback_query_handler(text='contacts')
async def contacts(c: types.CallbackQuery):
    user_id = c.from_user.id
    lang = sq.ans_lang(user_id)
    contacts_answer = sq.ans_contacts_answer(lang)
    await c.message.answer(contacts_answer, reply_markup=kb.inline_kb_contacts_markup)


@dp.message_handler(content_types=['location'])
async def location(c: types.Message):
    global point
    point = str(c.location.longitude) + ',' + str(c.location.latitude)
    await functions.func_inline_button(bot, c.chat.id, functions.msg['start'])


@dp.message_handler(text='meow')
async def get_location(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(text='Отправить местоположение', request_location=True)
    keyboard.add(button)
    await bot.send_message(message.chat.id, text='Покажи на карте, где ты находишься', reply_markup=keyboard)

# функция обработки inline кнопок
    # запускает функцию поиска по организациям
    # вызывает функцию создания inline клавиатуры
@dp.callback_query_handler(lambda call: True)
async def func_call(call:types.CallbackQuery):
    if point == '':
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(chat_id=call.message.chat.id, text=functions.msg['loc'])
    elif (call.data == 'McDonald’s' or call.data == 'KFC' or call.data == 'Subway' or call.data == 'Burger King'):
        await functions.func_search_gis(bot, call, point)
    elif call.data == 'var':
        await functions.func_var(bot, call)

# функция обработки текста
    # определяет геопозицию введенного пользователем адреса (в частности станции метро)
    # вызывает функцию создания inline клавиатуры
@dp.message_handler(content_types=['text'])
async def func_text(message):
    global point
    point = functions.func_geo_gis(message)
    await functions.func_inline_button(bot, message.chat.id, functions.msg['start'])