from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ChatMemberStatus, ChatMemberStatus


iddof = []
@Client.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "")& filters.group)
async def iddlock(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("**الامر معطل من قبل .**")
      iddof.append(message.chat.id)
      return await message.reply_text("**تم تعطيل الايدي بنجاح .**")
   else:
      return await message.reply_text("**عذرا عزيزي هذا الامر للادمن الجروب فقط .**")

@Client.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "")& filters.group)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("**الايدي مفعل من قبل .**")
      iddof.remove(message.chat.id)
      return await message.reply_text("**تم تفعيل الايدي بنجاح .**")
   else:
      return await message.reply_text("**عذرا عزيزي هذا الامر للادمن الجروب فقط .**")

@Client.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
       if message.chat.id in iddof:
         return await message.reply_text("**تم تعطيل امر الايدي من قبل المشرفين .**")
       user = await client.get_chat(message.from_user.id)
       user_id = user.id
       username = user.username
       first_name = user.first_name
       bioo = user.bio
       photo = user.photo.big_file_id
       photo = await client.download_media(photo)
       if not id.get(message.from_user.id):
         id[user.id] = []
       idd = len(id[user.id])
       await message.reply_photo(photo=photo, caption=f"**name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bioo}**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")],]),)
            


id = {}
@app.on_callback_query(filters.regex("heart"))  
async def heart(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("heart", "")  
    username = int(callback_request)
    usr = await client.get_chat(username)
    if not query.from_user.mention in id[usr.id]:
         id[usr.id].append(query.from_user.mention)
    else:
         id[usr.id].remove(query.from_user.mention)
    idd = len(id[usr.id])
    await query.edit_message_text(f"**name : {usr.first_name}\nid : {usr.id}\nuser : [@{usr.username}]\nbio : {usr.bio}**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{usr.id}")]]))




@Client.on_message(filters.text)
async def almortagel(client, message):
   if message.text == "😒":
       await message.reply_text(f"عدل وشك ونت بتكلمني 😒🙄")
   elif message.text == "💋":
       await message.reply_text(f" نا عايز مح انا كمان 🥺💔")
   elif message.text ==  "😭":
       await message.reply_text(f"بتعيط تيب لي طيب 😥")
   elif message.text == "🥺":
       await message.reply_text(f"متزعلش بحبك 😻🤍")
   elif message.text == "😂":
       await message.reply_text(f"ضحكتك عثل زيكك ينوحيي 🌝❤️")
   elif message.text == "🤔":
       await message.reply_text(f"بتفكر في اي 🤔")
   elif message.text == "🌚":
       await message.reply_text(f"القمر ده شبهك 🙂❤️")
   elif message.text == "نعم":
       await message.reply_text(f" نعم الله عليك 🌚❤️")
   elif "." in message.text:
       await message.reply_text(f"صلي علي النبي وتبسم ✨♥")
   elif message.text == "سلام":
       await message.reply_text(f" مع الف سلامه يقلبي متجيش تاني 😹💔🎶")
   elif message.text == "🙄":
       await message.reply_text(f" نزل عينك تحت كدا علشان هتخاد علي قفاك 😒❤️")
   elif message.text == "برايفت":
       await message.reply_text(f"خدوني معاكم برايفت والنبي 🥺💔")
   elif message.text == "بف":
       await message.reply_text(f"خدوني معاكم بف والنبي 🥺💔")
   elif message.text == "السلام عليكم":
       await message.reply_text(f"وعليكم السلام 🌝💜")
   elif message.text == "هاي":
       await message.reply_text(f"هآي تع اشب شااي • 😹💔")        
   elif message.text == "محح":
       await message.reply_text(f" محات حياتي يروحي 🌝❤️")
   elif message.text == "بحبك":
       await message.reply_text(f"وانا كمان بعشقك يا روحي 🤗🥰")
   elif message.text == "الحمدلله":
       await message.reply_text(f"دايما ياحبيبي 🌝❤️")
   elif message.text == "هشش":
       await message.reply_text(f" بنهش كتاكيت احنا هنا ولا اي ??😹")        
   elif message.text == "هلا":
       await message.reply_text(f" هلا بيك ياروحي 👋")
   elif message.text == "بف":
       await message.reply_text(f"وحيات امك ياكبتن خدوني معاكو بيف 🥺💔")
   elif message.text == "خاص":
       await message.reply_text(f"ونجيب اشخاص 😂👻")
   elif message.text == "بخير":
       await message.reply_text(f"انت الخير يعمري 🌝❤️")        
   elif message.text == "اه":
       await message.reply_text(f" اه اي يا قدع عيب 😹💔")
   elif message.text == "حصل":
       await message.reply_text(f"خخخ امال 😹")        
   elif message.text == "تع":
       await message.reply_text(f"لا عيب بتكسف 😹💔")
   elif message.text == "منور":
       await message.reply_text(f" ده نورك ي قلبي 🌝💙")        
   elif message.text == "ويت":
       await message.reply_text(f" اي الثقافه دي 😒😹")
   elif message.text == "خخخ":
       await message.reply_text(f" اهدا يوحش ميصحش كدا 😒?")        
   elif message.text == "باي":
       await message.reply_text(f"ع فين لوين رايح وسايبنى 🥺💔")
   elif message.text == "شكرا":
       await message.reply_text(f"العفو ياروحي 🙈🌝")        
   elif message.text == "حلوه":
       await message.reply_text(f" انت الي حلو ياقمر 🤤🌝")
   elif message.text == "بموت":
       await message.reply_text(f"موت بعيد م ناقصين مصايب 😑😂")        
   elif message.text == "تيب":
       await message.reply_text(f"فرح خالتك قريب 😹💋💃🏻")
   elif message.text == "اي":
       await message.reply_text(f"جتك اوهه م سامع ولا ايي 😹👻")        
   elif message.text == "حاضر":
       await message.reply_text(f"حضرلك الخير يارب 🙂❤️")
   elif message.text == "سي في":
       await message.reply_text(f"كفيه شقط سيب حاجه لغيرك 😎😂")        
   elif message.text == "جيت":
       await message.reply_text(f"لف ورجع تانى مشحوار 😂🚶‍♂👻")
   elif message.text == "بخ":
       await message.reply_text(f"يوه خضتني ياسمك اي 🥺💔")        
   elif message.text == "خلاص":
       await message.reply_text(f"خلصتت روحكك يبعيد 😹💔")
   elif message.text == "حبيبي":
       await message.reply_text(f"اوه ياه 🌝😂")
   elif message.text == "تمام":
       await message.reply_text(f"امك اسمها احلام 😹😹")
