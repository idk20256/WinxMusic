import config
from WinxMusic.core.bot import WinxBot
from WinxMusic.core.dir import dirr
from WinxMusic.core.git import git
from WinxMusic.core.userbot import Userbot
from WinxMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Pyrogram Client

app = WinxBot(
    "WinxMusic",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    sleep_threshold=240,
    max_concurrent_transmissions=5,
    workers=50,
)

userbot = Userbot()

# Directories
dirr()

# Check Git Updates
# git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

from .platforms import PlaTForms

Platform = PlaTForms()
HELPABLE = {}
