from aiogram import types

from config import *
import sql_data as sq, keyboards as kb


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
    await c.message.answer(hello, reply_markup=kb.inline_welcome_markup)


@dp.callback_query_handler(text='en')
async def lang_ru(c: types.CallbackQuery):
    user_id = c.from_user.id
    sq.lang_update(user_id, 'en')
    lang = sq.ans_lang(user_id)
    hello = sq.ans_hello(lang)
    await c.message.answer(hello, reply_markup=kb.inline_welcome_markup)


@dp.callback_query_handler(text='tr')
async def lang_ru(c: types.CallbackQuery):
    user_id = c.from_user.id
    sq.lang_update(user_id, 'tr')
    lang = sq.ans_lang(user_id)
    hello = sq.ans_hello(lang)
    await c.message.answer(hello, reply_markup=kb.inline_welcome_markup)


# @dp.callback_query_handler(text='commands')
# async def command(c: types.CallbackQuery):
#     user_id = c.from_user.id
#     lang = sq.ans_lang(user_id)
#     commands_answer = sq.ans_commands_answer(lang)
#     await c.message.answer(commands_answer)
#     await c.message.delete()
