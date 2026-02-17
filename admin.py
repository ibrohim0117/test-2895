from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from states import AddFilm
from database import insert_kino
from buttons import language_menu, kino_sifati_menu, janr_menu, user_menu


dp = Router()

ADMINS = [1038185913, ]

@dp.message(F.text == "➕ Kino qo'shish")
async def k_q(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("✍🏻 Kino nomini yozing")
        await state.set_state(AddFilm.name)

@dp.message(AddFilm.name)
async def a_n(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("🥳 Kino chiqarilgan yilni yozing")
    await state.set_state(AddFilm.year)

@dp.message(AddFilm.year)
async def a_y(message: types.Message, state: FSMContext):
    await state.update_data(year=message.text)
    await message.answer("🎥 Kino janrini yuboring", reply_markup=janr_menu)
    await state.set_state(AddFilm.janr)

@dp.message(AddFilm.janr)
async def a_j(message: types.Message, state: FSMContext):
    await state.update_data(janr=message.text)
    await message.answer("🇺🇿 Kino chiqarilgan tilini yuboring", reply_markup=language_menu)
    await state.set_state(AddFilm.language)

@dp.message(AddFilm.language)
async def a_l(message: types.Message, state: FSMContext):
    await state.update_data(language=message.text)
    await message.answer("🎞️ Kino yuklangan sifatni yozing", reply_markup=kino_sifati_menu)
    await state.set_state(AddFilm.sifati)

@dp.message(AddFilm.sifati)
async def a_s(message: types.Message, state: FSMContext):
    await state.update_data(sifati=message.text)
    await message.answer("✉️ Kino haqida qisqacha ma'lumot yozing", reply_markup=ReplyKeyboardRemove())
    await state.set_state(AddFilm.about)

@dp.message(AddFilm.about)
async def a_a(message: types.Message, state: FSMContext):
    await state.update_data(about=message.text)
    await message.answer("🆔 Kino uchun code yozing")
    await state.set_state(AddFilm.kino_code)

@dp.message(AddFilm.kino_code)
async def a_k(message: types.Message, state: FSMContext):
    await state.update_data(kino_code=message.text)
    await message.answer("🎬 Kinoni o'zini (video fayl) yuboring")
    await state.set_state(AddFilm.kino_file_id)

@dp.message(AddFilm.kino_file_id, F.video)
async def a_i(message: types.Message, state: FSMContext):
    # Video file_id sini saqlaymiz
    await state.update_data(kino_file_id=message.video.file_id)
    
    # Barcha ma'lumotlarni yig'ib olamiz
    data = await state.get_data()
    
    # Bazaga yozish (await bilan)
    await insert_kino(
        name=data.get('name'),
        year=data.get('year'),
        janr=data.get('janr'),
        language=data.get('language'),
        sifati=data.get('sifati'),
        about=data.get('about'),
        kino_code=data.get('kino_code'),
        kino_file_id=data.get('kino_file_id')
    )
    
    text = f"""
✅ Kino muvaffaqiyatli qo'shildi!

🎥 Kino kodi: {data.get('kino_code')}
🎬 Nomi: {data.get('name')}
➖➖➖➖➖➖➖➖➖➖
📀 Sifati: {data.get('sifati')}
📅 Sanasi: {data.get('year')}-yil
🌍 Tili: {data.get('language')}
🎥 Janr: {data.get('janr')}
✉️ Qisqacha ma'lumot: {data.get('about')}
"""
    await message.answer_video(video=data.get('kino_file_id'), caption=text, reply_markup=user_menu)
    await state.clear()