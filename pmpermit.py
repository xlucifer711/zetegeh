import asyncio
from pyrogram import Client
from helpers.filters import command
from config import SUDO_USERS, BOT_NAME as bn, BOT_USERNAME as lel, PMPERMIT, OWNER_USERNAME
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                f"ʜᴇʏ {message.from_user.mention()},\nᴛʜɪs ɪs [{bn}](t.me/{lel}) ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴅᴏɴ'ᴛ ᴛʀʏ ᴛᴏ sᴘᴀᴍ ʜᴇʀᴇ ᴇʟsᴇ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ꜰᴜ*ᴋᴇᴅ ʙʏ [𝑺𝑼𝑶𝑹𝑪𝑬 𝑩𝑬𝑴𝑩𝑶](t.me/B_e_m_0).\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 🐥 ¦ ᵇᵒᵗ ᵇᵉᵐᵇᵒ ", url=f"https://t.me/{lel}"
                    ),
                    InlineKeyboardButton(
                        " 🦦 ¦ جـروب الدعم ", url="https://t.me/{SUPPORT_GROUP}"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " 𓂄𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝙵𝚁𝙰𝚆𝙽𓆪𓂁 ", url=f"https://t.me/G_php"
                    )]
            ]
        ),

    )
            return


@Client.on_message(filters.command(["pm", "pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("**✅ ᴘᴍ-ᴘᴇʀᴍɪᴛ ᴛᴜʀɴᴇᴅ ᴏɴ...**")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("**❎ ᴘᴍ-ᴘᴇʀᴍɪᴛ ᴛᴜʀɴᴇᴅ ᴏғғ...**")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**✅ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ ᴅᴜᴇ ᴛᴏ ᴏᴜᴛɢᴏɪɴɢ ᴍᴇssᴀɢᴇ...**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", ["!", ".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**✅ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ...**")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", ["!", ".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("**❎ ᴅɪs-ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ...**")
        return
    message.continue_propagation()
