from aiogram.dispatcher.filters.state import StatesGroup, State
class Tillar(StatesGroup):
    in_lang = State()
    out_lang = State()
    text = State()