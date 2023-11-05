import asyncio


# Функция конфигурирования и запуска бота
async def main():
    from data import dp, bot, on_startup
    from handlers import is_admin, echo, user_block_bot, media, close_bot_menu
    from keyboards import set_main_menu_book

    dp.startup.register(set_main_menu_book)
    dp.startup.register(on_startup)

    dp.include_router(router=close_bot_menu.router)
    dp.include_router(router=is_admin.router)
    dp.include_router(router=user_block_bot.router)
    dp.include_router(router=media.router)
    dp.include_router(router=echo.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
