from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "➕ Kino qo'shish")
        ]
    ],
    resize_keyboard=True
)


user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "🔎 Kino qidirish")
        ]
    ],
    resize_keyboard=True
)


janr_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍿 Jangari"), KeyboardButton(text="😱 Dahshat")],
        [KeyboardButton(text="😂 Komediya"), KeyboardButton(text="❤️ Melodrama")],
        [KeyboardButton(text="🕵️ Fantastika"), KeyboardButton(text="🧐 Detektiv")],
        [KeyboardButton(text="🎞 Tarixiy"), KeyboardButton(text="🦁 Multfilm")],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)


language_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha"),
            KeyboardButton(text="🇷🇺 Русский"),
            KeyboardButton(text="🇺🇸 English")
        ],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)

kino_sifati_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎬 480p (Past)"),
            KeyboardButton(text="🎬 720p (HD)")
        ],
        [
            KeyboardButton(text="🎬 1080p (Full HD)"),
            KeyboardButton(text="💎 4K Ultra HD")
        ],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)