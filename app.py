from aiogram import Bot, Dispatcher
from data import TOKEN

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher()
from aiogram.types import Message

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )


dp.message.register(send_echo)


if __name__ == "__main__":
    dp.run_polling(bot)
