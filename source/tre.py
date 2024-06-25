import asyncio
import random
from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@Client.on_message(filters.command(["بلوك"], ""))
async def banall_command(client, message):
    print("الحصول على أعضاء من {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("طردته {} من {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("لم استطيع حظر : {} \n مـن : {}".format(i.user.id, e))