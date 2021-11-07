import requests
from pyrogram import Client
import io
import os
from pyrogram import filters
import asyncio
from pyrogram.types import Chat, User
from typing import ClassVar, Optional
from pyrogram.types import Message
from typing import Sequence


@Client.on_message(filters.command('bin'))
async def bincheck(client: Client, message: Message):
    try:
        binn = message_.text.split(" ", 1)
        bin = text[1]
        resp = requests.get("https://bin-check-dr4g.herokuapp.com/api/"+bin)
        requests_json = resp.json()
        r = requests_json['data']
        results = f"""Bin: r['bin'],
            Vendor: r['vendor'],
            Type: r['type'],
            Level: r['level'],
            Bank: r['bank'],
            Country: r['country']""" 
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐰𝐞𝐧𝐭 𝐰𝐫𝐨𝐧𝐠 𝐋𝐎𝐋...😶")
