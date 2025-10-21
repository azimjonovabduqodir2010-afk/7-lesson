from aiogram import types, Router, F
from aiogram.types import FSInputFile
from keyboard.default_keyboard import main_keyboard

router = Router()


@router.message(F.text == "💬 Qayta aloqa")
async def send_message(message: types.Message):
    await message.answer(text="Bu erga yozing, biz albatta javob beramiz.",)

