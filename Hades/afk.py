import time

async def afk(_, m):
    if not m.from_user:
        return
    user_id = m.from_user.id
    reply = m.reply_to_message
    try:
        if reply:
            if reply.photo:
                await _.download_media(reply, file_name=f"{user_id}.jpg")
                reason = m.text.split(None, 1)[1] if len(m.command) > 1 else None
                time_afk = time.time()
                 
        
