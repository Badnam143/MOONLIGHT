from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝄟‌≛⃝🥀𝙰𝙳𝙳 𝙼𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿𝚂᭄𓆪ꪾ🥀",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
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
                text="𝄟‌≛⃝🥀𝙰𝙳𝙳 𝙼𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿𝚂᭄𓆪ꪾ🥀",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✭𝙷𝙴𝙻𝙿 ♡︎ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂✭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="⎯꯭‌⎯꯭‌𝄟‌≛⃝🥀𝆺꯭𝅥𝚂𝚄𝙿𝙿𝙾𝚁𝚃✭", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="⎯꯭‌𝄟‌≛⃝🥀𝆺꯭𝅥𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁✭", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="⎯꯭‌𝆺꯭𝅥ᴿᴱᴾᴼ .𓈀✔", callback_data="badnam_ji"
            )
        ],
     ]
    return buttons
