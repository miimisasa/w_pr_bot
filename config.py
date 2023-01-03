from aiogram import Bot, Dispatcher

TOKEN_API = "5722453612:AAGduwqDuXdHETxAnPIjEe-6Lfr7_fYFRtc"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
admin_id = 418840255  # ИД админа (узнать можно в боте @username_to_id_bot )



API_key_search = '6845c310-b63f-4e65-a41e-9fd3566761df'                                                 # API-ключ поиска по организациям для Яндекс
yandex_search = 'https://search-maps.yandex.ru/v1/'                 # сайт Яндекс, в котором ведется поиск по организациям

API_key_geo = '2a30dea5-84dd-4d48-b2d0-2053490ff700'                                                    # API-ключ HTTP геокодер
yandex_geo = 'https://geocode-maps.yandex.ru/1.x'                   # сайт Яндекс для запроса на геокодирование

API_key_gis = ''                                                    # API-ключ для 2gis
gis_search = 'https://catalog.api.2gis.com/3.0/items'               # get-запрос для Places API
gis_geo = 'https://catalog.api.2gis.com/3.0/items/geocode'          # get-запрос для Geocoder API