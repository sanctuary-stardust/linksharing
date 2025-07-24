# By arka [telegram username: @name_huh]   
import os
import asyncio
from config import *
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, ChatAdminRequired, RPCError
from database.database import set_approval_off, is_approval_off, add_admin, remove_admin, list_admins

@Client.on_message(filters.command("addadmin") & filters.user(OWNER_ID))
async def add_admin_command(client, message: Message):
    if len(message.command) != 2 or not message.command[1].isdigit():
        return await message.reply_text("Usage: <code>/addadmin {user_id}</code>")
    user_id = int(message.command[1])
    success = await add_admin(user_id)
    if success:
        await message.reply_text(f"✅ User <code>{user_id}</code> added as admin.")
    else:
        await message.reply_text(f"❌ Failed to add admin <code>{user_id}</code>.")

@Client.on_message(filters.command("deladmin") & filters.user(OWNER_ID))
async def del_admin_command(client, message: Message):
    if len(message.command) != 2 or not message.command[1].isdigit():
        return await message.reply_text("Usage: <code>/deladmin {user_id}</code>")
    user_id = int(message.command[1])
    success = await remove_admin(user_id)
    if success:
        await message.reply_text(f"✅ User <code>{user_id}</code> removed from admins.")
    else:
        await message.reply_text(f"❌ Failed to remove admin <code>{user_id}</code>.")

@Client.on_message(filters.command("admins") & filters.user(OWNER_ID))
async def list_admins_command(client, message: Message):
    admins = await list_admins()
    if not admins:
        return await message.reply_text("No admins found.")
    text = "<b>Admin User IDs:</b>\n" + "\n".join([f"<code>{uid}</code>" for uid in admins])
    await message.reply_text(text)


from pyrogram import filters
from pyrogram.types import Message
from database.database import add_forced_channel, remove_forced_channel, get_forced_channels

@bot.on_message(filters.command("addfsub") & filters.user(ADMINS))
async def add_fsub(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /addfsub <channel_id>")
    cid = message.command[1]
    add_forced_channel(cid)
    await message.reply(f"✅ Added `{cid}` to forced sub list.")

@bot.on_message(filters.command("removefsub") & filters.user(ADMINS))
async def remove_fsub(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /removefsub <channel_id>")
    cid = message.command[1]
    remove_forced_channel(cid)
    await message.reply(f"🗑 Removed `{cid}` from forced sub list.")

@bot.on_message(filters.command("listfsub") & filters.user(ADMINS))
async def list_fsub(_, message: Message):
    cids = get_forced_channels()
    if not cids:
        return await message.reply("No forced sub channels.")
    await message.reply("**Forced Subscription Channels:**\n" + "\n".join(f"`{cid}`" for cid in cids))
