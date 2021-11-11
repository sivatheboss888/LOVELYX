from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as love
from MashaRoBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/63ec234e1be1f16345e69.jpg"
@register(pattern=("/alive"))
async def awake(event):
  LOVELY = event.sender.first_name
  LOVELY = "**𝗪𝗛𝗢 𝗔𝗠 𝗜 🥺❓** \n\n"
  LOVELY += "**I'ᴍ Lᴏᴠᴇʟʏ💞, Yᴏᴜʀ Hᴇᴀʀᴛʙᴇᴀᴛ❤️🙈*\n\n"
  LOVELY += "**I'ᴍ Wᴏʀᴋɪɴɢ Oɴ Lᴏᴠᴇ 😜**\n\n"
  LOVELY += "**Mʏ Lᴏᴠᴇ 🥰 :**  [ 🇷 ØΜΔŇŦIĆ❤️ 🇸 ĦΔ¥ΔŘ 🇹 ỮŞĦΔŘ](t.me/TUSHAR204)\n\n"
  LOVELY += "**Aʙᴏᴜᴛ Mʏ Lᴏᴠᴇ 🤩 :** [「ƬƲֆӇƛƦ ✘ ԼƠꪜЄԼƳ」🇮🇳](t.me/ABOUTVEDMAT)\n\n"
  BUTTON = [[Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧🙂", "https://t.me/LOVELYAPPEAL"), Button.url("𝗨𝗣𝗗𝗔𝗧𝗘", "https://t.me/LOVELY_ROBOTS")]]
  await love.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)
