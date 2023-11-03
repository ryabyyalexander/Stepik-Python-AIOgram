from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создаем список списков с кнопками
keyboard: list[KeyboardButton] = [
    KeyboardButton(text=str(i)) for i in range(1,9)]

# Инициализируем билдер
builder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
poll_btn = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)

# Добавляем кнопки в билдер
builder.row(contact_btn, geo_btn, poll_btn, width=1)
builder.row(*keyboard, width=8)

builder.adjust(2, 1, 8)

special_button: ReplyKeyboardMarkup = builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Нажмите кнопку'
)
