# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""ā¼ Helloowww š {message.from_user.first_name}! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\nā¼ Do you want me to play music in your Telegram groups'voice chats? Please click the " cĻŠ¼Š¼Ī±Ī·ās " button below to know how you can use me.\n\nā¼ Use the buttons below to know more about me ā¤ļøš„\n\nā¼ Contact my owner [š„šššš - šÆššššŖš„](https://t.me/FallenAngel_xD)\n\nA project by @FallenAngel_xD""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "š cĻŠ¼Š¼Ī±Ī·ās š", url="https://telegra.ph/%F0%9D%95%90%F0%9D%96%94%F0%9D%96%9A%F0%9D%96%97---%F0%9D%95%AF%F0%9D%96%86%F0%9D%96%89%F0%9D%96%89%F0%9D%95%AA-%EA%97%84-04-26")
                  ],[
                    InlineKeyboardButton(
                        "ā¤ļø Ī±Š²ĻĻŃ Š¼Īµ ā¤ļø", url="https://t.me/AboutOxy"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "š„ Š¼ŅÆ ĻĻĪ·ĪµŃ š„", url="https://t.me/FallenAngel_xD"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ā¼ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š„ Š¼ŅÆ ĻĻĪ·ĪµŃ š„", url="https://t.me/FallenAngel_xD")
                ]
            ]
        )
   )

