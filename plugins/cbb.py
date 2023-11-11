#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://t.me/moviekorner_1'>Click here</a>\n○Admin : <a href='https://t.me/vip_bro10'>Admin</a>\n○Group : <a href='https://t.me/moviekorner_1'>Group</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "premium":
        await query.message.delete()
        [[
            InlineKeyboardButton("1 Month", url="https://t.me/vip_bro1"), 
            InlineKeyboardButton("1 Weak", url="https://t.me/vip_bro1")
            ],[      
            InlineKeyboardButton("1 Day", url="https://t.me/vip_bro1"),
            InlineKeyboardButton("12 Hours", url="https://t.me/vip_bro1")
        ],[
            InlineKeyboardButton("Premium Buy Contact", url="https://t.me/vip_bro1")
        ]]
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
