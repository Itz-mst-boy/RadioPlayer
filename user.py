
from config import Config
from pyrogram import Client

REPLY_MESSAGE=Config.REPLY_MESSAGE

if REPLY_MESSAGE is not None:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH,
        plugins=dict(root="plugins.userbot")
        )
else:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH
        )
USER.start()
