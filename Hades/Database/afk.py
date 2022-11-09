from . import db

afkdb = db.afk

async def is_afk(user_id: int):
    x = await afkdb.find_one({"user_id": user_id})
    if not x:
        return False, {}
    return True, x["details"]

async def del_afk(user_id: int):
    x = await afkdb.find_one({"user_id": user_id})
    if x:
        return await afkdb.delete_one({"user_id": user_id})
    return

async def add_afk(user_id: int, details):
    x = await is_afk(user_id)
    if x:
        await del_afk(user_id)
    return await afkdb.insert_one({"user_id": user_id}, {"$set": {"details": details}})
    
async def afk_users():
    x = afkdb.find({"user_id": {"$gt": 0}})
    if not x:
        return []
    USERS = []
    for y in await x.to_list(length=1000000000):
        USERS.append(int(y))
    return USERS
    
