from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.database import get_forced_channels
from pyrogram.errors import UserNotParticipant

async def check_all_channels(bot, user_id):
    not_joined = []

    for channel_id in get_forced_channels():
        try:
            member = await bot.get_chat_member(int(channel_id), user_id)
            if member.status in ["left", "kicked"]:
                not_joined.append(int(channel_id))
        except UserNotParticipant:
            not_joined.append(int(channel_id))
        except Exception as e:
            print(f"Error checking {channel_id}: {e}")
            not_joined.append(int(channel_id))

    return not_joined

async def send_force_sub_message(bot, message, user_id):
    not_joined = await check_all_channels(bot, user_id)

    if not not_joined:
        return False

    buttons = []
    for cid in not_joined:
        try:
            chat = await bot.get_chat(cid)
            title = chat.title
            invite = f"https://t.me/{chat.username}" if chat.username else (await bot.create_chat_invite_link(cid)).invite_link
            buttons.append([InlineKeyboardButton(f"Join {title}", url=invite)])
        except Exception as e:
            print(f"Error generating button for {cid}: {e}")

    buttons.append([InlineKeyboardButton("✅ Joined", callback_data="refresh_fsub")])
    await message.reply(
        "🚫 You must join the channels below to use this bot:",
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )
    return True
