import surrogates as surrogates
from aiogram.utils import executor

from config import bot
from pr_bot import eng
from pr_bot import rus
from pr_bot import tr
from tr import *

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
"""


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_eng = InlineKeyboardButton(text=surrogates.decode('\ud83c\uddfa\ud83c\uddf8') + "English",
                                      callback_data="eng")
    button_tr = InlineKeyboardButton(text=surrogates.decode('\ud83c\uddf7\ud83c\uddfa') + "Russian",
                                     callback_data="rus")
    button_rus = InlineKeyboardButton(text=surrogates.decode('\ud83c\uddf9\ud83c\uddf7') + "Turkish",
                                      callback_data="tr")
    markup.add(button_eng, button_rus, button_tr)
    await bot.send_message(message.chat.id, "Welcome! You can choose the language : ", reply_markup=markup)

rus.rus_lang()
eng.eng_lang()
tr.tr_lang()

if __name__ == "__main__":
    executor.start_polling(dp)
