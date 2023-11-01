if __name__ == "__main__":
    from data import bot
    from data import dp
    from handlers import photo_register, register_start

    photo_register(dp)
    register_start(dp)

    dp.run_polling(bot)
