from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import *


def eng_lang():
    @dp.callback_query_handler(text='eng')
    async def eng(callback: types.CallbackQuery):
        markup_lang_eng = InlineKeyboardMarkup(row_width=2)
        button_1 = InlineKeyboardButton(text='List of services', callback_data='commands_eng')
        button_2 = InlineKeyboardButton(text='List of commands', callback_data='list_eng')
        button_3 = InlineKeyboardButton(text='Our contacts', callback_data='contacts_eng')
        markup_lang_eng.add(button_2, button_3, button_1)
        await callback.message.answer("Welcome! What are you interested in?", reply_markup=markup_lang_eng)


@dp.callback_query_handler(text='commands_eng')
async def command_eng(callback: types.CallbackQuery):
    await callback.message.answer("You need help?\n"
                                  "/start - restarting bot\n"
                                  "/about - description of our services\n")
    await callback.message.delete()


@dp.callback_query_handler(text='list_eng')
async def lists_eng(callback: types.CallbackQuery):
    markup_list_eng = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='Drugs', callback_data='meow_eng')
    button_2 = InlineKeyboardButton(text='Restaurant', callback_data='food_eng')
    button_3 = InlineKeyboardButton(text='Strip Club', callback_data='sluts_eng')
    markup_list_eng.add(button_1, button_2, button_3)
    await callback.message.answer("Please choose the service you are interested in and we will be happy to help you!",
                                  reply_markup=markup_list_eng)
    await callback.message.delete()


@dp.callback_query_handler(text="contacts_eng")
async def contact_eng(callback: types.CallbackQuery):
    markup_contacts_eng = InlineKeyboardMarkup()
    button_inst = InlineKeyboardButton(text="Instagram",
                                       url="https://instagram.com/mr.seriousblack?igshid=MDM4ZDc5MmU=")
    button_tg = InlineKeyboardButton(text="Telegram", url="https://t.me/ArbatskiyArt")
    markup_contacts_eng.add(button_inst, button_tg)
    await callback.message.answer("To contact us, you can follow the links below :", reply_markup=markup_contacts_eng)
