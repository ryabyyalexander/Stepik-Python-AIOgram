import asyncio
import logging


# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    from data import dp
    from data import bot
    from routers import is_admin, echo, user_block_bot, photo, close_bot_menu, user_handlers, other_handlers
    from keyboards import set_main_menu_book

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    dp.startup.register(set_main_menu_book)

    dp.include_router(router=close_bot_menu.router)
    dp.include_router(router=is_admin.router)
    dp.include_router(router=user_block_bot.router)

    dp.include_router(user_handlers.router)

    dp.include_router(router=photo.router)
    dp.include_router(router=echo.router)



    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
