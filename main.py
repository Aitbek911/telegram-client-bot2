import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    args = message.get_args()
    source = args if args else "без источника"
    user = message.from_user

    await message.answer(f"Салем, {user.full_name}!\nТы пришёл из: {source}")

    text = (
        f"НОВЫЙ ПОЛЬЗОВАТЕЛЬ!\n"
        f"Имя: {user.full_name}\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}\n"
        f"Источник: {source}"
    )
    await bot.send_message(ADMIN_ID, text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
