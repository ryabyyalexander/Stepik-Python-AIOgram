from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, ContentTypes

from handlers.report import kb
from keyboards.ikb import ikb, FIND_CAT, FIND_SIZE_J, FIND_SIZE, link
from loader import bot
from sql.db_m158 import add_users
from sql.product import find_prod_db
from states.states import State_load_prod, State_find_prod

findy = []
a = []


async def find(message: Message, state: FSMContext):
    try:
        x = await state.get_state()
        if x is not None:
            await state.finish()
        chat = message.chat.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username
        await add_users(chat, first_name, last_name, username)
        await State_find_prod.find_prod.set()
        async with state.proxy() as data:
            data['chat'] = chat
            data['first_name'] = first_name
        await message.answer(f"{first_name.upper()}, вибери параметр пошуку", reply_markup=ikb(FIND_CAT))
        await message.delete()
    except Exception as e:
        print(f"Сталася помилка: {e}")


async def find_size(call: CallbackQuery):
    try:
        descr = "о б е р и   н е о б х і д н и й   р о з м і р"
        global findy
        findy.append(call.data)
        if findy[0][:-3] == 'д ж и н с и' or findy[0][:-3] == 'ш о р т и':
            await call.message.edit_text(descr, reply_markup=ikb(FIND_SIZE_J, 5))
        else:
            await call.message.edit_text(descr, reply_markup=ikb(FIND_SIZE))
    except Exception as e:
        print(f"Произошла ошибка: {e}")


async def find_prod(call: CallbackQuery, state: FSMContext):
    try:
        global findy
        findy.append(call.data)
        async with state.proxy() as data:
            name = data['first_name']
        await call.message.edit_text(findy[0][:-3])
        prod = find_prod_db(findy[0][:-3], findy[1][:2])
        qnt = []
        if not prod:
            await call.message.edit_text(text=f'{name.upper()}, знайшлось - {len(prod)}')
            findy = []
            await state.finish()
        else:
            for i in range(len(prod)):
                photo_id = prod[i][-4]
                _link = prod[i][-3]
                if _link:
                    _link = _link
                else:
                    _link = 'lnk'
                _description = prod[i][0]
                _category = prod[i][1]
                _sub_category = prod[i][2]
                _country = prod[i][-2]
                _brand = prod[i][3]
                _size = prod[i][6]
                qnt.append(_size.count(call.data[:2]))
                _price = prod[i][-5]
                _sale = prod[i][5]
                _price_sale = int(prod[i][-5] * (100 - _sale) / 100)
                _seas = prod[i][4]
                _tam = prod[i][-1]
                if _tam == 1:
                    t = '™️'
                else:
                    t = '🌀'
                seas = ['🌦 ☀️ ВЕСНА - ЛІТО', '🌨 ❄️ ОСІНЬ - ЗИМА'][_seas]

                caption = f"{_description}\n\n"f"{_country}\n"\
                          f"- - - - - - - - - - - - - - - - - - - - -\n"\
                          f"{t}  {seas}\n\n"\
                          f"•  <b>{_brand}</b>\n\n"\
                          f"<code>{_size}</code>\n\n"\
                          f"<code>Ціна:</code>  <b>{_price}</b> - {_sale}%  ➔ {_price_sale}<code> у.о.</code>"

                async with state.proxy() as data:
                    chat = data['chat']
                    name = data['first_name']

                await bot.send_photo(chat, photo=photo_id, caption=caption, reply_markup=link(_link))
                # await call.message.answer(caption, reply_markup=link(_link))
            await call.message.edit_text(text=f'✔️   <b>в и к о н а н о</b>')
            await bot.send_message(chat, f"• <b>{name.upper()}</b>\n\n"
                                         f"знайшлось - <b>{len(prod)}</b> прод.\nу розмірі <b>{findy[1][:2]}</b>\n"
                                         f"у кількості - <b>{sum(qnt)}</b> шт.")
            await state.finish()
            findy = []
    except Exception as e:
        print(f"Сталася помилка: {e}")


async def echo(message: Message):
    await message.delete()


async def hello(message: Message, state: FSMContext):
    try:
        x = await state.get_state()
        if x is not None:
            await state.finish()
        chat = message.chat.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username
        await add_users(chat, first_name, last_name, username)
        await State_find_prod.find_prod.set()
        async with state.proxy() as data:
            data['chat'] = chat
            data['first_name'] = first_name
        await message.answer(f"{first_name.upper()}, вибери параметр пошуку", reply_markup=ikb(FIND_CAT))
        await message.delete()
    except Exception as e:
        print(f"Сталася помилка: {e}")

    await message.delete()


def register_find_cat(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(hello, commands=['start'], state=State_find_prod.find_prod)
    dp.register_message_handler(hello, commands=['start'], state=State_load_prod)

    dp.register_message_handler(find, commands=['find_product'])
    dp.register_message_handler(find, commands=['find_product'], state=State_find_prod)
    dp.register_message_handler(find, commands=['find_product'], state=State_load_prod)

    dp.register_callback_query_handler(find_size, Text(equals=FIND_CAT), state=State_find_prod)
    dp.register_callback_query_handler(find_prod, Text(equals=FIND_SIZE), state=State_find_prod)
    dp.register_callback_query_handler(find_prod, Text(equals=FIND_SIZE_J), state=State_find_prod)

    dp.register_message_handler(echo, )
    dp.register_message_handler(echo, content_types=ContentTypes.PHOTO)
    dp.register_message_handler(echo, content_types=ContentTypes.VIDEO)
    dp.register_message_handler(echo, content_types=ContentTypes.VOICE)

    dp.register_message_handler(echo, state=State_find_prod.find_prod)
    dp.register_message_handler(echo, content_types=ContentTypes.PHOTO, state=State_find_prod.find_prod)
    dp.register_message_handler(echo, content_types=ContentTypes.VIDEO, state=State_find_prod.find_prod)
    dp.register_message_handler(echo, content_types=ContentTypes.VOICE, state=State_find_prod.find_prod)
