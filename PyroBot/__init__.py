from pyrogram import Client
from pyromod import listen
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Session
API_ID = API_ID = int(os.getenv("API_ID"))
API_HASH = API_HASH = os.getenv("API_HASH")
BOT_TOKEN = API_HASH = os.getenv("BOT_TOKEN")

# Client
excmd = Client(
    'exploiterxD',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(
        root='PyroBot.pl'
    )
)
