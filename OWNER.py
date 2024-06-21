import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["Almortagel_12"]
OWNER_NAME = "? ? ? ?? ?????????? ???????"
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE = getenv("MONGO_DB_URI", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/AlmortagelTech"
GROUP = "https://t.me/AlmortagelTech2"
VID_SO = "https://telegra.ph/file/bf1273e084a0fb135ab5a.jpg"
PHOTO = "https://telegra.ph/file/bf1273e084a0fb135ab5a.jpg"
LOGS = "jabababbab"
