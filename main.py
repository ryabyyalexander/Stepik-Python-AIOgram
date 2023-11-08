if __name__ == "__main__":
    from data import dp, bot
    from handlers import is_admin, fsm_form, user_block_bot, close_bot_menu, id_media, edit_media, book, echo
    from keyboards import set_main_menu

    dp.startup.register(set_main_menu)
    dp.include_router(router=book.router)

    dp.include_router(router=close_bot_menu.router)
    dp.include_router(router=is_admin.router)
    dp.include_router(router=user_block_bot.router)
    dp.include_router(router=fsm_form.router)
    dp.include_router(router=id_media.router)
    dp.include_router(router=edit_media.router)
    dp.include_router(router=echo.router)

    dp.run_polling(bot)
