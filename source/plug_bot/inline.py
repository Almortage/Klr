from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio
#سورس المرتجل بيمسي - @Almortagel_12


@bot.on_inline_query(filters.regex("^الاوامر$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("①",callback_data="help1"),
             InlineKeyboardButton("②",callback_data="help2"),
             InlineKeyboardButton("③",callback_data="help3"),
             InlineKeyboardButton("④",callback_data="help4"),
             ],
             [
             InlineKeyboardButton("⑤",callback_data="help5"),
             InlineKeyboardButton("⑥",callback_data="help6"),
             InlineKeyboardButton("⑦",callback_data="help7"),
             InlineKeyboardButton("⑧",callback_data="help8"),
             ],
             [
             InlineKeyboardButton("⑨",callback_data="help9"),
             InlineKeyboardButton("①⓪",callback_data="help10"),
             InlineKeyboardButton("①①",callback_data="help11"),
             ],
             [
             InlineKeyboardButton("قناة السورس .",url="https://t.me/AlmortagelTech"),
             ],
             [
             InlineKeyboardButton("مطور السورس .",url="https://t.me/Almortagel_12"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(
                    "• اهلا بك في اوامر اليوزر البوت\n• ① اوامر الخاص\n• ② اوامر القنوات والمجموعات \n• ③ اوامر اليوتيوب \n• ④ اوامر الاذاعه\n• ⑤ اوامر التسليه \n• ⑥ اوامر اضافيه\n• ⑦ اوامر المرح\n• ⑧ اوامر النسب\n• ⑨ اوامر الميمز\n• ⓪① اوامر الميمز2\n• ①① اوامر الميمز3"
                ),
                url="https://t.me/AlmortagelTech",
                description="SoUrCe 𝗔𝗹𝗺𝗼𝗿𝘁𝗮𝗴𝗲𝗹",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )
