from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ContentTypes, CallbackQuery
from keyboards.ikb import CATEGORY, SIZE, SIZE_J, JERSEY, JEANS, BRAND, ikb_load
from loader import bot
from sql.product import create_product
from sql.save_content import save_all_img, get_img, get_desc, save_desc
from states.states import State_load_prod, State_find_prod

_category = ''
_sub_category = ''
_size = []
_brand = ''


async def load_prod(message: Message, state: FSMContext):
    x = await state.get_state()
    if x is not None:
        await state.finish()
    await State_load_prod.load.set()
    async with state.proxy() as data:
        data['chat'] = message.chat.id
        data['first_name'] = message.from_user.first_name
    await message.answer(
        f"{data['first_name'].upper()}, <code>щоб додати продукт, спочатку</code> <b>обов'язково</b> "
        f"<code>додайте фотографію</code>")
    await message.delete()


async def jersey(call: CallbackQuery):
    await call.message.edit_text(call.data, reply_markup=ikb_load(JERSEY, 4))
    await call.answer(call.data)
    global _category
    _category = call.data


async def jeans(call: CallbackQuery):
    await call.message.edit_text(call.data, reply_markup=ikb_load(BRAND[:2]))
    await call.answer(call.data)
    global _category
    _category = call.data


async def jacket(call: CallbackQuery):
    await call.message.edit_text(call.data, reply_markup=ikb_load(BRAND[2:9]))
    await call.answer(call.data)
    global _category
    _category = call.data


async def sub_cat_jersey(call: CallbackQuery):
    await call.message.edit_text(call.data, reply_markup=ikb_load(BRAND[7:], n=2))
    await call.answer(call.data)
    global _sub_category
    _sub_category = call.data


async def brand_jeans(call: CallbackQuery):
    await call.message.edit_text(call.data, reply_markup=ikb_load(BRAND[:2]))
    await call.answer(call.data)
    global _sub_category
    _sub_category = call.data


k = True


async def size(call: CallbackQuery):
    await call.message.edit_text(f'\n•  •  •   в и б е р и   р о з м е р и   •  •  •\n\n{call.data}',
                                 reply_markup=ikb_load(SIZE, 4, ok=True))
    await call.answer(call.data)
    global _size
    global k
    global _brand
    if k:
        _brand = call.data
        k = False
    else:
        _size.append(call.data)


async def size_jeans(call: CallbackQuery):
    await call.message.edit_text(f'\n•  •  •   в и б е р и   р о з м е р и   •  •  •\n\n{call.data}',
                                 reply_markup=ikb_load(SIZE_J, 5, ok=True))
    await call.answer(call.data)
    global _size
    global k
    global _brand
    if k:
        _brand = call.data
        k = False
    else:
        _size.append(call.data)


async def load_photo(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['chat'] = int(message.chat.id)
        data['first_name'] = message.from_user.first_name
    photo = message.photo[-1]
    save_all_img(photo.file_id)
    await message.answer('➕ В яку категорію додаті?', reply_markup=ikb_load(CATEGORY))
    await message.delete()


async def load_description(message: Message, state: FSMContext):
    if message.text not in ['/start', '/find_product']:
        save_desc(message.text)
    else:
        save_desc('н е м а є   о п и с у')
        await state.finish()
    await message.delete()


async def h_create_product(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        chat = data['chat']
        first_name = data['first_name']
    _pos_pic = get_img()
    _description = get_desc()
    if _description == '':
        _description = 'н е м а є   о п и с у'
    global _category
    global _sub_category
    global _brand
    global _size
    global k

    await call.message.edit_text(f'{first_name.upper()},  д о д а н о')

    _size = [x.split(' - ')[0] for x in _size]
    _size = sorted(_size)

    prod = (_pos_pic, _description, _category, _sub_category, _brand, ' | '.join(_size))
    create_product(prod)

    if _sub_category == '':
        caption = f"{_description}\n\n•  {_category}\n•  {_brand}\n{' | '.join(_size)}\n•  {len(_size)} шт.\n"
    else:
        caption = f"""{_description}\n\n•  {_category}\n•  {_sub_category}\n•  {_brand}\n{' | '.join(_size)}\n
        •  {len(_size)} шт.\n"""

    await bot.send_photo(chat, photo=_pos_pic, caption=caption)

    _category = ''
    _sub_category = ''
    _size = []
    _description = save_desc('')
    k = True


def register_new_card(dp: Dispatcher):
    dp.register_message_handler(load_prod, commands=['l'])
    dp.register_message_handler(load_prod, commands=['l'], state=State_load_prod)
    dp.register_message_handler(load_prod, commands=['l'], state=State_find_prod)

    dp.register_message_handler(load_photo, content_types=ContentTypes.PHOTO, state=State_load_prod)
    dp.register_message_handler(load_description, state=State_load_prod)

    dp.register_callback_query_handler(jacket, Text(equals=CATEGORY[:1]), state=State_load_prod)
    dp.register_callback_query_handler(jeans, Text(equals=CATEGORY[1:2]), state=State_load_prod)
    dp.register_callback_query_handler(jersey, Text(equals=CATEGORY[2:]), state=State_load_prod)

    dp.register_callback_query_handler(sub_cat_jersey, Text(equals=JERSEY), state=State_load_prod)
    dp.register_callback_query_handler(brand_jeans, Text(equals=JEANS), state=State_load_prod)

    dp.register_callback_query_handler(size, Text(equals=BRAND[2:]), state=State_load_prod)
    dp.register_callback_query_handler(size_jeans, Text(equals=BRAND[:2]), state=State_load_prod)

    dp.register_callback_query_handler(size, Text(equals=SIZE), state=State_load_prod)
    dp.register_callback_query_handler(size_jeans, Text(equals=SIZE_J), state=State_load_prod)

    dp.register_callback_query_handler(h_create_product, text='д о д а н о', state=State_load_prod)
