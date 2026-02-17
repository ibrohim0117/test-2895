import asyncio
import os
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from buttons import user_menu, admin_menu
from database import create_table, insert_user
from admin import dp as admin_router
from users import dp as user_router

from aiogram.types import ReplyKeyboardRemove

TOKEN = "7833766047:AAEyx3YaT3urp6UKM-LJMT4VTMsaxqS_4IY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

ADMINS = [1038185913, ]


@dp.message(Command('start'))
async def start(message: types.Message):
    try:
        await insert_user(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            user_id=message.from_user.id
        )
    except:
        pass


    if message.from_user.id in ADMINS:
        await message.answer("Xush kelibsiz admin", reply_markup=admin_menu)
    else:
        await message.answer("Salom xush kelibsiz!", reply_markup=user_menu)



async def main():
    await create_table()   
    print("Bot ishga tushdi...")
    dp.include_router(admin_router)
    dp.include_router(user_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

