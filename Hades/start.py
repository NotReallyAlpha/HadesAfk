TEXT = """Hey {}! I'm AFK Bot of Hades Network. 

Try: replying afk to some media or stickers or gifs to make it more reasonable !

"""

from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from .Database.users import add_user

LINK = "https://te.legra.ph/file/a2667ec3a9c9a986ae056.jpg"

async def start(_, m):
    await add_user
    l = await _.get_me()
    un = l.username
    name = m.from_user.first_name
    markup = IKM(
             [
             [
             IKB("➕ Add me to your group ➕", url=f"t.me/{un}?startgroup=True")
             ]
             ]
             )
    await m.reply_photo(LINK, caption=TEXT.format(name), reply_markup=markup)
    
