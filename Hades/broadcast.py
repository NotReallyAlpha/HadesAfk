import asyncio 

from .Database.chats import get_chats
from pyrogram.errors import FloodWait

async def broadcast(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    pinned = 0
    chats = await get_chats()
    for i in chats:
        try:
            if message.reply_to_message:
                ok = await _.forward_messages(i, y, x)
                sent += 1
                try:
                    await _.pin_chat_message(i, ok.message_id)
                    pinned += 1
                except:
                    continue 
            else:
                ok = await _.send_message(i, query)
                sent += 1
                try:
                    await _.pin_chat_message(i, ok.message_id)
                    pinned += 1
                except:
                    continue
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await message.reply_text(
            f"**Broadcasted Message In {sent} Chats and pinned in {str(pinned)} Chats**"
        )
    except:
        pass
