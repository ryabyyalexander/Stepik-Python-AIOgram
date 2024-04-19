from aiogram.dispatcher.filters.state import State, StatesGroup


class State_load_prod(StatesGroup):
    load = State()


class State_find_prod(StatesGroup):
    find_prod = State()
