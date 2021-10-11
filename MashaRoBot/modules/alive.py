from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as tbot
from MashaRoBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/63ec234e1be1f16345e69.jpg"
@register(pattern=("/alive"))
async def awake(event):
  LOVELY = event.sender.first_name
  LOVELY = "**♡ I,m Lovely💕** \n\n"
  LOVELY += "**♡ I'm Working with awesome speed**\n\n"
  LOVELY += "**♡ Lovely : 2.0 LATEST**\n\n"
  LOVELY += "**♡ My Creator :** [𝗧𝗨𝗦𝗛𝗔𝗥😍](t.me/Tushar204)\n\n"
  LOVELY += "**♡ Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓🙂", "https://t.me/LOVELYAPPEAL"), Button.url("𝐔𝐏𝐃𝐀𝐓𝐄", "https://t.me/LOVELY_ROBOTS")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)
