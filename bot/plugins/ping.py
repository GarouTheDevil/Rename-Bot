# (c) @AbirHasan2005

from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("**Not For You")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="**Hi, I am Rename Bot**",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("Settings",
                                      callback_data="showSettings")
        ]])
    )


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("Not For You")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="**• Renames Without Downloading File**\n"
             "**• Use** /rename Cammand **To Rename**\n"
             "**• Use** /set_thumbnail **To Set A Thumbnail**\n"
             "**• Use** /show_thumbnail **To View Thumbnail**",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("Settings",
                                      callback_data="showSettings")]])
    )
