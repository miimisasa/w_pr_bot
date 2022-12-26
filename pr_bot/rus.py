from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from pr_bot.config import dp


def rus_lang():
    @dp.callback_query_handler(text='rus')
    async def rus(callback: types.CallbackQuery):
        markup_lang = InlineKeyboardMarkup(row_width=2)
        button_1 = InlineKeyboardButton(text='Список команд', callback_data='commands')
        button_2 = InlineKeyboardButton(text='Список услуг', callback_data='list')
        button_3 = InlineKeyboardButton(text='Наши контакты', callback_data='contacts')
        markup_lang.add(button_2, button_3, button_1)
        await callback.message.answer("Добро пожаловать! Что вас интересует? ", reply_markup=markup_lang)


@dp.callback_query_handler(text='commands')
async def command(callback: types.CallbackQuery):
    await callback.message.answer("Вам нужна помощь?\n"
                                  "/start - перезапуск бота\n"
                                  "/about - описание наших услуг\n")
    await callback.message.delete()

@dp.callback_query_handler(text='list')
async def lists(callback: types.CallbackQuery):
    markup_list = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='Травка', callback_data='meow')
    button_2 = InlineKeyboardButton(text='Ресторан', callback_data='food')
    button_3 = InlineKeyboardButton(text='Стрип', callback_data='sluts')
    markup_list.add(button_1, button_2, button_3)
    await callback.message.answer("Выберите, пожалуйста, интересующую Вас услугу и мы с радостью поможем Вам!",
                                  reply_markup=markup_list)
    await callback.message.delete()

@dp.callback_query_handler(text="contacts")
async def contact(callback: types.CallbackQuery):
    markup_contacts = InlineKeyboardMarkup()
    button_inst = InlineKeyboardButton(text="Instagram", url="https://instagram.com/mr.seriousblack?igshid=MDM4ZDc5MmU=")
    button_tg = InlineKeyboardButton(text = "Telegram", url="https://t.me/ArbatskiyArt")
    markup_contacts.add(button_inst, button_tg)
    await callback.message.answer("Для связи с нами вы можете перейти по ссылкам ниже :", reply_markup=markup_contacts)
