from aiogram import types, Router, F
from aiogram.types import FSInputFile
from keyboard.default_keyboard import main_keyboard, tilar_keyboard

router = Router()


@router.message(F.text == "🇺🇿/🇷🇺 Tilni o'zgartirish")
async def send_message(message: types.Message):
    await message.answer(text="🇺🇿/🇷🇺 ",
                         reply_markup=tilar_keyboard())

