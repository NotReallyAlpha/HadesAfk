from . import db

usersdb = db.users

async def add_user(user_id: int):
    x = await usersdb.find_one({"user_id": user_id})
    if not x:
        return await usersdb.insert_one({"user_id": user_id})
    return

async def get_users():
    x = usersdb.find({"user_id": {"$gt": 0}})
    if not x:
        return []
    USERS = []
    for y in await x.to_list(length=1000000000):
        USERS.append(int(y))
    return USERS
