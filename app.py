if __name__ == "__main__":
    from data import bot
    from data import dp
    from handlers import register_start
    register_start(dp)
    dp.run_polling(bot)
