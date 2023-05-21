from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url="https://t.me/Mistyopmusic_bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                url="https://t.me/mrs_yamraj",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/Mistyopmusic_bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ", url="https://t.me/mrs_yamraj",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣ sᴜᴩᴩᴏʀᴛ ❣", url="https://t.me/best_friends_chattung_grup",
            ),
            InlineKeyboardButton(
                text="🥀 ᴍᴀɪɴᴛᴀɪɴᴇʀ 🥀", url="https://t.me/mrs_yamraj",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ sᴏᴜʀᴄᴇ ✨", url="https://t.me/mrs_yamraj",
            )
        ],
     ]
    return buttons
