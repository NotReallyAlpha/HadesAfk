from config import API, TOKENS
from pyrogram import Client as Hades, idle
from pyrogram.filters import command as hade_cmd

hades = Hades(":Hades:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN)

