from Hades.Database.afk import is_afk, del_afk
import time 
from .helpers import get_readable_time

uname = None
async def afk_watcher(_, m):
    global uname 
    if not uname:
        uname = (await _.get_me()).username
    if not m.from_user:
        return
    if m.text.split()[0].lower() in ["/afk", f"/afk@{uname}", "brb"]:
        return
    user_id = m.from_user.id
    first_name = m.from_user.first_name
    afk, details = await is_afk(user_id)
    if afk:
        type = details["type"]
        if type == "photo":
            final_time = get_readable_time(details["time"] - time.time())
            reason = details["reason"]
            txt += f"**{first_name}** is back online and was away for {final_time}"
            txt += " "
            txt += f"\n\n**Reason** : `{reason}`" if reason else ""
            await m.reply_photo(f"downloads/{user_id}.jpg", caption=txt)
            await del_afk(user_id)
        elif type == "animation":
            final_time = get_readable_time(details["time"] - time.time())
            reason = details["reason"]
            txt += f"**{first_name}** is back online and was away for {final_time}"
            txt += " "
            txt += f"\n\n**Reason** : `{reason}`" if reason else ""
            await m.reply_animation(details["data"], caption=txt)
            await del_afk(user_id)
        elif type == "text":
            final_time = get_readable_time(details["time"] - time.time())
            reason = details["reason"]
            txt += f"**{first_name}** is back online and was away for {final_time}"
            txt += " "
            txt += f"\n\n**Reason** : `{reason}`" if reason else ""
            await m.reply(txt)
            await del_afk(user_id)

async def afk_reply_watcher(_, m):
    if not m.from_user:
        return
    reply_id = m.reply_to_message.from_user.id
    afk, details = await is_afk(reply_id)
    if afk:
        type = details["type"]
        if type == "photo":
            final_time = get_readable_time(details["time"] - time.time())
            reason = details["reason"]
            txt += f"**{first_name}** is AFK Since {final_time}"
            txt += " "
            txt += f"\n\n**Reason** : `{reason}`" if reason else ""
            await m.reply_photo(f"downloads/{user_id}.jpg", caption=txt)
        elif type == "animation":
            final_time = get_readable_time(details["time"] - time.time())
            reason = details["reason"]
            txt += f"**{first_name}** is AFK Since {final_time}"
            txt += " "
            txt += f"\n\n**Reason** : `{reason}`" if reason else ""
            await m.reply_animation(details["data"], caption=txt)
        elif type == "text":
            final_time = get_readable_time(details["time"] - time.time())
            reason = details["reason"]
            txt += f"**{first_name}** is AFK Since {final_time}"
            txt += " "
            txt += f"\n\n**Reason** : `{reason}`" if reason else ""
            await m.reply(txt)

    if m.text:
        spl = m.text.split()
        uns = []
        for s in spl:
            if s[0] == "@":
                uns.append(s)
        if not uns:
            return
        for un in uns:
            id = (await _.get_users(un)).id
            afk, details = await is_afk(id)
            if afk:
                type = details["type"]
            if type == "photo":
                final_time = get_readable_time(details["time"] - time.time())
                reason = details["reason"]
                txt += f"**{first_name}** is AFK since {final_time}"
                txt += " "
                txt += f"\n\n**Reason** : `{reason}`" if reason else ""
                await m.reply_photo(f"downloads/{user_id}.jpg", caption=txt)
            elif type == "animation":
                final_time = get_readable_time(details["time"] - time.time())
                reason = details["reason"]
                txt += f"**{first_name}** is AFK since {final_time}"
                txt += " "
                txt += f"\n\n**Reason** : `{reason}`" if reason else ""
                await m.reply_animation(details["data"], caption=txt)
            elif type == "text":
                final_time = get_readable_time(details["time"] - time.time())
                reason = details["reason"]
                txt += f"**{first_name}** is AFK since {final_time}"
                txt += " "
                txt += f"\n\n**Reason** : `{reason}`" if reason else ""
                await m.reply(txt)

PIC = "https://te.legra.ph/file/ba980e91c447df3bbedfe.jpg"

async def welcome(_, m):
    chat_id = m.chat.id
    await add_chat(chat_id)
    get = (await _.get_me())
    men = get.mention
    bot_id = get.id
    for x in m.new_chat_members:
        try:
            if x.id == bot_id:
                await m.reply_photo(PIC, caption=f"Thanks for having me in {m.chat.title}\n\n{men} is alive !\n\nFor queries : @Asynchorous")
        except:
            pass 

    
            
        
           
