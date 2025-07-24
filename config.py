# By [telegram username: @name_huh 
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7776292747:AAEEUaDwTbulwtILDYWCrmLpyiU8cmdida8")
APP_ID = int(os.environ.get("APP_ID", "23579843"))
API_HASH = os.environ.get("API_HASH", "813614877521e3b94bed3d1562192fdd")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "5548954124"))
PORT = os.environ.get("PORT", "8099")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://jeffyweekends:jeffyweekends@cluster0.ma61isx.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "furina")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @emitingstars_botz</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/emitingstars_botz'>Emitingstars botz</a></blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=https://t.me/name_huh>name</a>\n» Our Community: <a href=https://t.me/sanctuary_stardust>sanctuary stardust</a>\n» Anime Channel: <a href=https://t.me/sanctuary_stardust>Anime Stardust</a>\n» Ongoing Anime: <a href=https://t.me/sanctuary_stardust>Ongoing Stardust</a>\n» Developer: <a href=https://t.me/name_huh>name</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by name (@name_huh) to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/sanctuary_stardust'>sanctuary</a>
<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/emitingstars_botz'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/name_huh'>NAME HUH</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/sanctuary_stardust'> sanctuary </blockquote>"""

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/anime_stardust'>ᴀɴɪᴍᴇ </a>
<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/movies_stardust'>ᴍᴏᴠɪᴇ </a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/webseriez_stardust'>ᴡᴇʙsᴇʀɪᴇs </a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/culturedbeing'> cultured </a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/pornhwa_stardust'>ᴘᴏʀɴʜᴡᴀ </a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/sanctuary_stardust'> sanctuary </a>"""


#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ ! ee tu jaa ree !! "

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002764021488")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "5548954124").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(5548954124)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
