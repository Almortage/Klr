from almortagel import Almortagel
from pyrogram import Client,filters,enums
import redis

r = redis.Redis(
  host='redis-17811.c323.us-east-1-2.ec2.cloud.redislabs.com',
  port=17811,
  password='y41sFD7N8cY5Ob2MGPZkGdrTndVFY92h')

sudo_id = 5089553588
bot_user = Almortagel.BOT_USER
via_user = Almortagel.VIA_USER
elhyba = bot_user
via = via_user
api_id = Almortagel.APP_ID
api_hash = Almortagel.API_HASH
session = Almortagel.SESSION
token = Almortagel.TG_BOT_TOKEN
sudo_command = [5089553588]
pm =  Almortagel.MENTION
mention = "5089553588"
plugins = dict(root="plugins")
app = Client(via,api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client(elhyba,api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
