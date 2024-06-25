import asyncio
import random
from pyrogram import Client, filters
from pyrogram import Client as app
import random
from config import *
from pyrogram import Client, filters
from pyrogramessage.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogramessage.enums import ChatMemberStatus


forward = []
cursing = []
mute = []

@Client.on_message(filters.command(["قفل الدردشه"], ""))
def of_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions())
  message.reply(f"• تم قفل الدردشه\n• بواسطة : {mention}",quote=True)
  return

@Client.on_message(filters.command(["فتح الدردشه"], ""))
def on_chat(client, message):
  idchat = message.chat.id
  mention = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  client.set_chat_permissions(idchat, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
  message.reply(f"• تم فتح الدردشه\n• بواسطة : {mention}",quote=True)
  return

@Client.on_message(filters.command(["قفل السب"], ""))
def of_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.append(idchat)
  message.reply(f"• تم قفل السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@Client.on_message(filters.command(["فتح السب"], ""))
def on_cursing(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.remove(idchat)
  message.reply(f"• تم فتح السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@Client.on_message(filters.command(["قفل التوجيه"], ""))
def of_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.append(idchat)
  message.reply(f"• تم قفل التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@Client.on_message(filters.command(["فتح التوجيه"], ""))
def on_forward(client, message):
  idchat = message.chat.id
  name = message.from_user.mention
  a = client.get_chat_member(message.chat.id, message.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not message.from_user.id == OWNER:
    return message.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.remove(idchat)
  message.reply(f"• تم فتح التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@Client.on_message(filters.text & filters.group)
def msg(client, message):
  text = message.text
  idchat = message.chat.id

  if message.from_user.id in mute:
    message.delete()

  insults = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
  if str(text) in insults:
    if idchat in cursing:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع الشتائم ⚡ .
"""
         message.reply(Text,quote=True)

  if message.forward_date:
    if idchat in forward:
      a = client.get_chat_member(idchat, message.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.from_user.id == OWNER:
         message.delete()
         mute.append(message.from_user.id)
         Text =f"""
♪ عذرا {message.from_user.mention} ⚡ .
♪ ممنوع التوجيه هنا ⚡ .
"""
         message.reply(Text,quote=True)
