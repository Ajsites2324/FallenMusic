import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💔 ʜᴇʏ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}), ᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs...

ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ʜᴀɴᴅʟᴇʀs : ( `/ . • $ ^ ~ + * ? /aj` )
┏━━━━━━━━━━━━━━┓
┣★ ᴏᴡɴᴇʀ:[ᴀᴊᴇᴇᴛ](https://t.me/papa_bol_sakteho)
┣★ ᴏᴡɴᴇʀ ɢꜰ:[ᴘᴀʀᴋ ʏᴜᴋᴜ](https://t.me/parkjiminparkyuku)
┣★ ꜱᴜᴘᴘᴏʀᴛ:[ᴀᴊ ɴᴇᴛᴡᴏʀᴋ](https://t.me/tpn_chatroom)
┣★ ᴀʙᴏᴜᴛ :[ʙᴀʙʏ](https://t.me/about_ajeet)
┣★ ᴄʜᴀɴɴᴇʟ:[ᴀᴊ ꜱᴇʀᴠᴇʀ](https://t.me/the_professor_network)
┗━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴍᴀꜱᴛᴇʀ](t.me/papa_bol_sakteho) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ​ 🥺", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "💔 ᴏᴡɴᴇʀ 💔", url=f"https://t.me/papa_bol_sakteho"
                    ),
                    InlineKeyboardButton(
                        "🍒 sᴜᴘᴘᴏʀᴛ 🍒", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔎 ɪɴʟɪɴᴇ 🔎", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "🤯 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​ 🤯", url="https://t.me/about_ajeet"
                    )]
            ]
       ),
    )

