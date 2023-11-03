from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from data.lexicon import city25
print(city25)
c25 = [KeyboardButton(text=i) for i in city25]

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
builder.row(*c25)
builder.row(contact_btn, geo_btn, poll_btn)
builder.adjust(2,2,3)

special_button: ReplyKeyboardMarkup = builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='ryabyy.alexander@gmail.com'
)
