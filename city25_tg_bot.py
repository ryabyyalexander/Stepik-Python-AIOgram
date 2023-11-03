import asyncio


async def main():
    from data import dp
    from data import bot
    from routers import is_admin, echo, user_block_bot, photo

    dp.include_router(router=is_admin.router)
    dp.include_router(router=user_block_bot.router)
    dp.include_router(router=photo.router)
    dp.include_router(router=echo.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
