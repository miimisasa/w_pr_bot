import peewee

db = peewee.SqliteDatabase('data/data.db')


class Base(peewee.Model):
    class Meta:
        database = db


class Data(Base):
    user = peewee.CharField(primary_key=True)
    lang = peewee.CharField()


class Language(Base):
    lang = peewee.CharField(primary_key=True)
    hello = peewee.CharField()
    commands_answer = peewee.CharField()
    commands = peewee.CharField()
    services = peewee.CharField()
    contacts = peewee.CharField()
    services_answer = peewee.CharField()
    contacts_answer = peewee.CharField()
    meow = peewee.CharField()
    food = peewee.CharField()
    sluts = peewee.CharField()
    meow_answer = peewee.CharField()

# db.create_tables([Data, Language])
# lang = Language.create(lang='ru', hello='Добро пожаловать! Что вас интересует?',
#                        commands_answer='Вам нужна помощь?\n/start - перезапуск бота\n/about - описание наших услуг\n',
#                        commands='Список команд', services='Список услуг', contacts='Наши контакты',
#                        services_answer='Выберите, пожалуйста, интересующую Вас услугу и мы с радостью поможем Вам!',
#                        contacts_answer='Для связи с нами вы можете перейти по ссылкам ниже:', meow = 'Наркотики', food = 'Ресторан', sluts = 'Притон', meow_answer = 'Пришли свою геопозицию')
# lang = Language.create(lang='en', hello='Welcome! What are you interested in?',
#                        commands_answer='You need help?\n/start - restarting bot\n/about - description of our services\n',
#                        commands='List of commands', services='List of services', contacts='Our contacts',
#                        services_answer='Please choose the service you are interested in and we will be happy to help you!',
#                        contacts_answer='To contact us, you can follow the links below :', meow = 'Drugs', food = 'Restaurant', sluts = 'Sluts', meow_answer = 'Send your geoposition')

def check_user(id):
    try:
        check = Data.get(Data.user == id).user
    except peewee.DoesNotExist:
        (Data.create(user=id, lang='False'))


def lang_update(id, lang):
    (Data.update({Data.lang: lang}).where(Data.user == id).execute())


def ans_lang(id):
    text = Data.get(Data.user == id).lang
    return text


def ans_hello(lang):
    text = Language.get(Language.lang == lang).hello
    return text


def ans_commands(lang):
    text = Language.get(Language.lang == lang).commands
    return text

def ans_commands_answer(lang):
    text = Language.get(Language.lang == lang).commands_answer
    return text

def ans_services(lang):
    text = Language.get(Language.lang == lang).services
    return text

def ans_contacts(lang):
    text = Language.get(Language.lang == lang).contacts
    return text

def ans_services_answer(lang):
    text = Language.get(Language.lang == lang).services_answer
    return text

def ans_contacts_answer(lang):
    text = Language.get(Language.lang == lang).contacts_answer
    return text

def ans_meow(lang):
    text = Language.get(Language.lang == lang).meow
    return text

def ans_food(lang):
    text = Language.get(Language.lang == lang).food
    return text

def ans_sluts(lang):
    text = Language.get(Language.lang == lang).sluts
    return text

def ans_meow_answer(lang):
    text = Language.get(Language.lang == lang).meow_answer
    return text
