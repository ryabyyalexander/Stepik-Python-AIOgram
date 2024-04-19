if __name__ == "__main__":
    from data import dp, bot, on_startup, on_shutdown
    from handlers import fsm_form, user_block_bot, id_media, echo
    from keyboards import set_main_menu

    dp.startup.register(set_main_menu)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.include_router(router=user_block_bot.router)
    dp.include_router(router=fsm_form.router)
    dp.include_router(router=id_media.router)
    dp.include_router(router=echo.router)

    dp.run_polling(bot)
