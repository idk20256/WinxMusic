from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def play_logs(message: Message, streamtype: str):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "🔒 Grup Privat"

        logger_text = f"""
🎵 Log Pemutaran - {app.mention} 🎵

📌 ID Chat: {message.chat.id}
🏷️ Nama Chat: {message.chat.title}
🔗 Nama Pengguna Chat: {chatusername}

👤 ID Pengguna: {message.from_user.id}
📛 Nama: {message.from_user.mention}
📱 Nama Pengguna: @{message.from_user.username}

🔍 Permintaan: {message.text.split(None, 1)[1]}
🎧 Jenis Streaming: {streamtype}"""

        # Membuat tombol
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=f"👤 Lihat Pengguna: {message.from_user.first_name}",
                        user_id=message.from_user.id
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="👥 Grup yang Memutar Musik",
                        url=f"https://t.me/{message.chat.username}" if message.chat.username else None  # Tautan ke grup
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=f"🎧 Jenis Pemutaran: {streamtype.capitalize()}",
                        callback_data=f"streamtype_{streamtype}"  # Tipe streaming sebagai data callback
                    )
                ]
            ]
        )

        # Mengirim log dengan tombol
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    reply_markup=buttons,  # Menambahkan tombol
                    disable_web_page_preview=True,
                )
            except Exception:
                pass
        return
