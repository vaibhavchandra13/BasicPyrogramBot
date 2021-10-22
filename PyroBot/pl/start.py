from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from PyroBot import excmd

MESSAGE = (
        'Hello there!\n'
        'I am a Simple Bot Build with Pyrogram and Python\n\n'
        'By [exploiterxD](https://github.com/exploiterxD)'
    )

KEYBOARD = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text='Github', url='github.com/exploiterxD')],
    [InlineKeyboardButton(text='Source Code', url='github.com/exploiterxD/BasicPyroBot')]]
)

@excmd.on_message(filters.text & filters.private & ~filters.bot)
async def start(sessionCli, message):
    await message.reply(
        text=MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=False
    )

