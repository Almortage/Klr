import random
from pyrogram import Client, filters, idle
from pyrogram import Client 
from source.info import (joinch)
from pyrogram import enums

hrooof = ["بجد ولله ،", 
"مين قالك ع الجمله دي",
"روق كد وركز معايا 😂",
"حسك بتغش من حد ياض ،",
"ولله بتغش مشلاعب معاك ",
"بطل غش حرام هه🙂",
"الكدب حرام ياخي اتقي الله ",
"احلف ؟",
"جدع ياض ،",
"مين مات ؟",
"ياه ع التركيز",
"كلامك عشره علي عشره ❤️",
"بمت بسغش بق 😂🙂"
"لو شوفتك بتكدب تني ههينك ،",
"احلا ظرطه دي ولا اي ،",
"لف ي علف وبس كدب بق ،",]


hroof = [" مدينة بحرف ع  ",
" حيوان ونبات بحرف خ  ", 
" اسم بحرف ح  ", 
" اسم ونبات بحرف م  ", 
" دولة عربية بحرف ق  ", 
" جماد بحرف ي  ", 
" نبات بحرف ج  ", 
" اسم بنت بحرف ع  ", 
" اسم ولد بحرف ع  ", 
" اسم بنت وولد بحرف ث  ", 
" جماد بحرف ج  ",
" حيوان بحرف ص  ",
" دولة بحرف س  ",
" نبات بحرف ج  ",
" مدينة بحرف ب  ",
" نبات بحرف ر  ",
" اسم بحرف ك  ",
" حيوان بحرف ظ  ",
" جماد بحرف ذ  ",
" مدينة بحرف و  ",
" اسم بحرف م  ",
" اسم بنت بحرف خ  ",
" اسم و نبات بحرف ر  ",
" نبات بحرف و  ",
" حيوان بحرف س  ",
" مدينة بحرف ك  ",
" اسم بنت بحرف ص  ",
" اسم ولد بحرف ق  ",
" نبات بحرف ز  ",
"  جماد بحرف ز  ",
"  مدينة بحرف ط  ",
"  جماد بحرف ن  ",
"  مدينة بحرف ف  ",
"  حيوان بحرف ض  ",
"  اسم بحرف ك  ",
"  نبات و حيوان و مدينة بحرف س  ", 
"  اسم بنت بحرف ج  ", 
"  مدينة بحرف ت  ", 
"  جماد بحرف ه  ", 
"  اسم بنت بحرف ر  ", 
" اسم ولد بحرف خ  ", 
" جماد بحرف ع  ",
" حيوان بحرف ح  ",
" نبات بحرف ف  ",
" اسم بنت بحرف غ  ",
" اسم ولد بحرف و  ",
" نبات بحرف ل  ",
"مدينة بحرف ع  ",
"دولة واسم بحرف ب  "]


@Client.on_message(filters.command(["ح", "حروف", "الحروف", "حرف"], ""))
async def booyt(client: Client, message):
   try:
    if not message.chat.type == enums.ChatType.PRIVATE:
       if await joinch(message):
            return
    bar = random.choice(hroof)
    barto = random.choice(hrooof)
    ask = await client.ask(message.chat.id, f"**{bar}**", filters=filters.user(message.from_user.id), reply_to_message_id=message.id, timeout=100)
    await ask.reply_text(f"**{barto}**")
   except:
       pass