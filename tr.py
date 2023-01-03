from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import dp


def tr_lang():
    @dp.callback_query_handler(text='tr')
    async def tr(callback: types.CallbackQuery):
        markup_lang_tr = InlineKeyboardMarkup(row_width=2)
        button_1 = InlineKeyboardButton(text='Hizmetlerin listesi', callback_data='commands_tr')
        button_2 = InlineKeyboardButton(text='Komutların listesi', callback_data='list_tr')
        button_3 = InlineKeyboardButton(text='İletişim bilgilerimiz', callback_data='contacts_tr')
        markup_lang_tr.add(button_2, button_3, button_1)
        await callback.message.answer("Hoş geldin! İlginizi çeken nedir?", reply_markup=markup_lang_tr)


@dp.callback_query_handler(text='commands_tr')
async def command_tr(callback: types.CallbackQuery):
    await callback.message.answer("Yardıma mı ihtiyacın var?\n"
                                  "/start - her ikisini de yeniden başlatma\n"
                                  "/about - hizmetlerimizin tanımı\n")
    await callback.message.delete()


@dp.callback_query_handler(text='list_tr')
async def lists_tr(callback: types.CallbackQuery):
    markup_list_tr = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='İlaçlar', callback_data='meow_tr')
    button_2 = InlineKeyboardButton(text='Restorant', callback_data='food_tr')
    button_3 = InlineKeyboardButton(text='Striptiz Kulübü', callback_data='sluts_tr')
    markup_list_tr.add(button_1, button_2, button_3)
    await callback.message.answer("Lütfen ilgilendiğiniz hizmeti seçin ve size yardımcı olmaktan memnuniyet duyarız!",
                                  reply_markup=markup_list_tr)
    await callback.message.delete()


@dp.callback_query_handler(text="contacts_tr")
async def contact_tr(callback: types.CallbackQuery):
    markup_contacts_tr = InlineKeyboardMarkup()
    button_inst = InlineKeyboardButton(text="Instagram",
                                       url="https://instagram.com/mr.seriousblack?igshid=MDM4ZDc5MmU=")
    button_tg = InlineKeyboardButton(text="Telegram", url="https://t.me/ArbatskiyArt")
    markup_contacts_tr.add(button_inst, button_tg)
    await callback.message.answer("Bizimle iletişime geçmek için aşağıdaki linkleri takip edebilirsiniz :", reply_markup=markup_contacts_tr)
