from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)],
    [KeyboardButton(text=str(i)) for i in range(7, 9)]
]

# Создаем объект клавиатуры, добавляя в него кнопки
stepik = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)