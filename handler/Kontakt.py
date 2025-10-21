from aiogram import types, Router, F
from aiogram.types import FSInputFile
from keyboard.default_keyboard import main_keyboard

router = Router()
photo = "https://havasfood.uz/wp-content/uploads/2020/12/untitled-2-1.jpg"

@router.message(F.text == "📞 Kontaktlar")
async def send_message(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""🤝Для связи:
☎️Контакты +998 71 205 95 95
📩Электронная почта havas_uz@mail.ru""")