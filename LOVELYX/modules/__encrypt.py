from LOVELYX import telethn as tbot
import os
from LOVELYX.events import register
import secureme

@register(pattern="^/encrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          cmd = lel.text
    else:
          cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)

@register(pattern="^/decrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          ok = lel.text
    else:
          ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)


__mod_name__ = "Sᴇᴄᴜʀᴇ🔒"

__help__ = """
 ➲ /encrypt*:* Encrypts The Given Text
 ➲ /decrypt*:* Decrypts Previously Ecrypted Text

📢𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 *:- @TEAM_LOV3LY ❤️‍🔥*
"""
