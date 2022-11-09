from . import db

afkdb = db.afk

async def add_afk(user_id: int, reason):
