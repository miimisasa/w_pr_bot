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
    bottom_commands = peewee.CharField()


db.create_tables([Data, Language])
lang = Language.create(lang='ru', hello='Добро пожаловать! Что вас интересует?', bottom_commands='Команды',
                       commands_answer='Вам нужна помощь?\n/start - перезапуск бота\n/about - описание наших услуг\n')


# lang = Language.create(lang='en', hello='Добро пожаловать! Что вас интересует?', bottom_commands='Команды')
# lang = Language.create(lang='tr', hello='Добро пожаловать! Что вас интересует?', bottom_commands='Команды')


def check_user(id):
    try:
        check = Data.get(Data.user == id).user
    except peewee.DoesNotExist:
        (Data.create(user=id, lang='False'))


def lang_update(id, lang):
    (Data.update({Data.lang: lang()}).where(Data.user == id).execute())


def ans_lang(id):
    text = Data.get(Data.user == id).lang
    return text


def ans_hello(lang):
    text = Language.get(Language.lang == lang()).hello
    return text


def answer_bottom_commands(lang):
    text = Language.get(Language.lang == lang()).bottom_commands
    return text


def ans_commands_answer(lang):
    text = Language.get(Language.lang == lang()).commands_answer
    return text
