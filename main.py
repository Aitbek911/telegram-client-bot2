import os
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram import types
from aiogram import html

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())
router = Router()


@router.message(F.text, F.text.startswith("/start"))
async def cmd_start(message: Message):
    args = message.text.split(maxsplit=1)
    source = args[1] if len(args) > 1 else "без источника"
    user = message.from_user

    await message.answer(
        f"Сәлем, <b>{html.quote(user.full_name)}</b>!\n"
        f"Сен ботқа осы жерден келдің: <code>{source}</code>"
    )

    text = (
        f"<b>Жаңа пайдаланушы!</b>\n"
        f"Аты: {html.quote(user.full_name)}\n"
        f"Username: @{user.username}\n"
        f"ID: <code>{user.id}</code>\n"
        f"Келген жері: <code>{source}</code>"
    )
    await bot.send_message(ADMIN_ID, text)


dp.include_router(router)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.run_polling(bot)
