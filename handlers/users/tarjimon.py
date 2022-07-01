from aiogram import types
from loader import dp
from deep_translator import GoogleTranslator
from states.languges import Tillar
from keyboards.inline.tillar import btn, btn_two
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CallbackQuery
@dp.message_handler(commands="tarjima", state=None)
async def test1(message: types.Message):
    await message.answer("Qaysi tilda ma'lumot kiritasiz, Iltimos tanlang", reply_markup=btn)
    await Tillar.in_lang.set()
@dp.callback_query_handler(Text(startswith="👍"), state=Tillar.in_lang)
async def test2(call: CallbackQuery, state: FSMContext):
    info = call.data
    info = info[1:]
    await state.update_data(
        {
            'in_lang': info
        }
    )
    await call.answer(cache_time=60)
    await call.message.answer("Qaysi tilda ma'lumot chiqsin, Iltimos tanlang!", reply_markup=btn_two)
    await call.message.delete()
    await Tillar.next()
@dp.callback_query_handler(Text(startswith="back"), state=Tillar.out_lang)
async def test5(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi tilda ma'lumot kiritasiz, Iltimos tanlang", reply_markup=btn)
    await call.message.delete()
    await  Tillar.in_lang.set()
@dp.callback_query_handler(Text(startswith="👎"), state=Tillar.out_lang)
async def test3(call: CallbackQuery, state: FSMContext):
    info = call.data
    info = info[1:]
    await state.update_data(
        {
            'out_lang': info
        }
    )
    await call.answer(cache_time=60)
    await call.message.answer("Tarjima qilish uchun matn kiriting")
    await call.message.delete()
    await Tillar.next()
@dp.message_handler(state=Tillar.text, content_types='text')
async def test4(message:types.Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {
            'text': text
        }
    )
    data = await state.get_data()
    result = GoogleTranslator(source=data["in_lang"], target=data["out_lang"]).translate(data["text"])
    await message.answer(result)
    await state.finish()

