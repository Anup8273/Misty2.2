from pyrogram.types import InlineKeyboardButton
import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥀 sᴜᴩᴩᴏʀᴛ 🥀", url="https://t.me/best_friends_chatting_grup",
            ),
            InlineKeyboardButton(
                text="  𝒐𝒘𝒏𝒆𝒓  ", url="https://t.me/mrs_yamraj"
            ),
        ],
    ]
    return buttons
