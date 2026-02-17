from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from states import SearchFilm
from database import select_film

dp = Router()

@dp.message(F.text == "🔎 Kino qidirish")
async def k_q(message: types.Message, state: FSMContext):
    await message.answer("🆔 Kino kodini yuboring")
    await state.set_state(SearchFilm.code)

@dp.message(SearchFilm.code)
async def s_f(message: types.Message, state: FSMContext):
    code = message.text
    
    # Bazadan kinoni bir marta qidirib olamiz (await bilan)
    film = await select_film(code)
    
    if film is not None:
        # film[0] - id, film[1] - name, film[2] - year, va hokazo
        text = f"""
🎥 Kino kodi: {film[7]}
🎬 Nomi: {film[1]}
➖➖➖➖➖➖➖➖➖➖
📀 Sifati: {film[5]}
📅 Sanasi: {film[2]}-yil
🌍 Til: {film[4]}
🎥 Janr: {film[3]}
✉️ Qisqacha ma'lumot: {film[6]}
"""
        # Video yuborishda ham film[8] dagi file_id ishlatiladi
        await message.answer_video(video=film[8], caption=text)
    else:
        await message.answer(f"BU 🆔 {code} kodli kino mavjud emas!")
    
    await state.clear()