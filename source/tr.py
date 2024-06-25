import asyncio
import random
import datetime
from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from source.info import get_served_chats


MESSAGE = f"""- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه

وبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.

ارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️

معرف البوت 🎸 [ @{username} ]

➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤e 𝘤𝘩𝘢𝘵 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{username} \n\n-𝙳𝙴𝚅 ➤ @{OWNER}"""


BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("خدني لجروبك والنبي🥺♥",url=f"https://t.me/{app.username}?startgroup=True")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await Client.send_photo(chat_id, photo=photo, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(50000)  
        
asyncio.create_task(continuous_broadcast())
