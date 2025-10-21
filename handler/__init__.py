from aiogram import Router
from handler import start, about_us


def setup_message_router():
    router = Router()
    router.include_router(start.router)
    router.include_router(about_us.router)
    return router