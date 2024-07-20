from pyrogram import __version__, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from config import OWNER_ID

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    message = query.message
    
    if message is None:
        print("Received callback query without a message")
        return
    
    if data == "about":
        try:
            await message.edit_text(
                text=f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n"
                     f"○ Language : <code>Python3</code>\n"
                     f"○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n"
                     f"○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n"
                     f"○ Channel : @CodeXBotz\n"
                     f"○ Support Group : @CodeXBotzSupport</b>",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔒 Close", callback_data="close")
                        ]
                    ]
                )
            )
        except Exception as e:
            print(f"Failed to edit message: {e}")
    elif data == "close":
        try:
            await message.delete()
            if message.reply_to_message:
                await message.reply_to_message.delete()
        except Exception as e:
            print(f"Failed to delete message or reply: {e}")
