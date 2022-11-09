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
                _reason = m.text.split(None, 1)[1] if len(m.command) > 1 else None
                time_afk = time.time()
                details = {
                          "type": "photo",
                          "reason": _reason if _reason else None,
                          "time": time_afk
                          }
            elif reply.sticker:
                if reply.sticker.is_animated:
                    _reason = m.text.split(None, 1)[1]
                    time_afk = time.time()
                    details = {
                          "type": "text",
                          "reason": _reason if _reason else None,
                          "time": time_afk
                          }
                else:
                    await _.download_media(reply, file_name=f"{user_id}.jpg")
                    _reason = m.text.split(None, 1)[1] if len(m.command) > 1 else None
                    time_afk = time.time()
                    details = {
                          "type": "photo",
                          "reason": _reason if _reason else None,
                          "time": time_afk
                          }
            elif reply.animation:
                _data = reply.animation.file_id
                _reason = m.text.split(None, 1)[1]
                time_afk = time.time()
                details = {
                          "type": "animation",
                          "reason": _reason if _reason else None,
                          "time": time_afk,
                          "data": _data
                          }
            else:
                _reason = m.text.split(None, 1)[1]
                time_afk = time.time()
                details = {
                          "type": "text",
                          "reason": _reason if _reason else None,
                          "time": time_afk
                          }
                 
        
