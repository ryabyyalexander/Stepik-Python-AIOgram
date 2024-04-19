from handlers.find_category import register_find_cat
from handlers.load_prod_on_db import register_new_card
from handlers.report import register_report

if __name__ == '__main__':
    from loader import on_startup, on_shutdown
    from aiogram import executor
    from loader import dp
    register_report(dp)
    register_new_card(dp)
    register_find_cat(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
