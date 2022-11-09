from config import API, TOKENS
from pyrogram import Client as Hades, idle
from pyrogram.filters import command as hade_cmd, new_chat_members
from Hades.afk import afk
from Hades.watcher import afk_reply_watcher, afk_watcher, welcome

hades = Hades(":Hades:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN)

@hades.on_message(hade_cmd(["afk"]) | hade_cmd("brb", ""))
async def afk_plug(_, m):
    await afk(_, m)

@hades.on_message(group=1)
async def watcher1(_, m):
    await afk_watcher(_, m)

@hades.on_message(group=2)
async def watcher2(_, m):
    await afk_reply_watcher(_, m)

@hades.on_message(group=3 & new_chat_members)
async def welcome_plug(_, m):
    await welcome(_, m)
