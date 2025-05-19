from datetime import datetime

from pyrogram.types import Message

from WinxMusic import app
from WinxMusic.core.call import Winx
from WinxMusic.utils import bot_sys_stats
from WinxMusic.utils.decorators.language import language
from WinxMusic.utils.inline import support_group_markup
from config import BANNED_USERS
from config.assets import PINK_STICKER_ID #disnicuk
from strings import command

@app.on_message(command("PING_COMMAND") & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_sticker(PING_STICKER_ID)

    start = datetime.now()
    pytgping = await Winx.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
#kintil
    await response.edit_text(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping,
        ),
        reply_markup=support_group_markup(_),
    )
