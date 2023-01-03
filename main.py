from aiogram.utils import executor

import eng
import handlers
import rus
import tr
from config import *

handlers.register_handler(dp)

#rus.rus_lang()
#eng.eng_lang()
#tr.tr_lang()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
