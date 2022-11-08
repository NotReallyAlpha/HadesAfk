from os import environ as e

class API:
    API_ID = e["API_ID"]
    API_HASH = e["API_HASH"]

class TOKENS:
    BOT_TOKEN = e["BOT_TOKEN"]

class DB:
    MONGO_DB_URL = e["MONGO_DB_URL"]

class DEV:
    SUDO_USERS_STR = e["SUDO_USERS"].split()
    SUDO_USERS = []
    for x in SUDO_USERS_STR:
        SUDO_USERS.append(int(x))
