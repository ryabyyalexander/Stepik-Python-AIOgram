if __name__ == "__main__":
    from data import bot
    from data import dp
    from handlers import user_blocked_bot, photo, echo

    photo(dp)
    user_blocked_bot(dp)
    echo(dp)

    dp.run_polling(bot)
