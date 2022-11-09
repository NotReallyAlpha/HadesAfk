from Hades.Database.afk import is_afk, del_afk

async def afk_watcher(_, m):
    if not m.from_user:
        return
    user_id = m.from_user.id
    afk, details = await is_afk(user_id)
    if afk:
        type = details["type"]
        if type == "photo":
           
