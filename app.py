import asyncio


async def main():
    from data import dp
    from handlers import user_blocked_bot, photo, echo
    from data import bot

    photo(dp)
    user_blocked_bot(dp)
    echo(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
