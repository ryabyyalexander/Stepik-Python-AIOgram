from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Router

from data import BOOK

router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(BOOK[message.text])
    # if message.from_user.id not in users_db:
    #     users_db[message.from_user.id] = deepcopy(user_dict_template)
    await message.delete()


# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(BOOK[message.text])
    await message.delete()


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )
