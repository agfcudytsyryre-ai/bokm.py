import os, shutil
for _f in os.listdir('.'):
    for _p in ('Plugins_', 'helpers_'):
        if _f.startswith(_p) and _f.endswith('.py'):
            _d = _p[:-1]
            os.makedirs(_d, exist_ok=True)
            shutil.copyfile(_f, os.path.join(_d, _f[len(_p):]))
import time, redis, os, json, re, requests, asyncio 
from pyrogram import *
r = redis.from_url(os.environ['REDIS_URL'], decode_responses=True)

to_config = """
import os, redis
r = redis.from_url(os.environ['REDIS_URL'], decode_responses=True)
"""

print('''
Loading…
█=▒▒▒▒▒▒▒▒▒''')
print('\n\n')

try:
  from information import *
  Dev_Blue = token.split(':')[0]
  r.set(f'{Dev_Blue}botowner', owner_id)
except Exception as e:
  with open ('information.py','w+') as www:
     token = input ('[+] Enter the bot token : ')
     Dev_Blue = token.split(':')[0]
     if not r.get(f'{Dev_Blue}botowner'):
       owner_id = int(input('[+] Enter SUDO ID : '))
       r.set(f'{Dev_Blue}botowner', owner_id)
     else:
        owner_id = int(r.get(f'{Dev_Blue}botowner'))
     text = 'token = "{}"\nowner_id = {}'
     www.write(text.format(token, owner_id))

    


if not r.get(f'{Dev_Blue}botowner'):
    owner_id = int(input('[+] Enter SUDO ID : '))
    r.set(f'{Dev_Blue}botowner', owner_id)
else:
    owner_id = int(r.get(f'{Dev_Blue}botowner'))
print('''
10% 
█=█=█▒▒▒▒▒▒▒ ''')

to_config += f"\ntoken = '{token}'"
to_config += f"\nDev_Blue = token.split(':')[0]"
to_config += f"\nsudo_id = {owner_id}"
username = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]
to_config += f"\nbotUsername = '{username}'"
to_config += "\nfrom kvsqlite.sync import Client as DB"
to_config += "\nytdb = DB('ytdb.sqlite')"
to_config += "\nsounddb = DB('sounddb.sqlite')"
to_config += "\nwsdb = DB('wsdb.sqlite')"

print('''
30% 
█=█=█=█=█▒▒▒▒▒ ''')
with open('config.py','w+') as w:
  w.write(to_config)
print('''
50% 
█=█=█=█=█=█=█▒▒▒ ''')
app = Client(f'{Dev_Blue}Blue', int(os.environ.get('API_ID', 28850159)), os.environ.get('API_HASH', '09a3e7d212b434aec973ad5ea10d8ec6'),
  bot_token=token,
    plugins={"root": "Plugins"},
  )
# userbot = Client('userbott', API_ID, API_HASH, session_string=os.environ.get('SESSION'))
  
if not r.get(f'{Dev_Blue}:botkey'):
    r.set(f'{Dev_Blue}:botkey', '⇜')

if not r.get(f'{Dev_Blue}botname'):
    r.set(f'{Dev_Blue}botname', 'Blue')

if not r.get(f'{Dev_Blue}botchannel'):
    r.set(f'{Dev_Blue}botname', 'ffll1bot')

def Find(text):
  m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(m,text)  
  return [x[0] for x in url]
  
# @app.on_message(filters.group & filters.regex("^انستا "), group=-1)
# async def instaDownlo(c,m):
#   if not r.get(f'{m.chat.id}:disableINSTA:{Dev_Blue}') and Find(m.text):
#     url = Find(m.text)[0]
#     rep = await m.reply("...")
#     await m.reply_chat_action(enums.ChatAction.TYPING)
#     msg = await userbot.send_message("instasavegrambot", url)
#     await rep.edit("Wait ...")
#     await asyncio.sleep(20)
#     await m.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
#     msg = await userbot.get_messages("instasavegrambot",msg.id+1)
#     await rep.delete()
#     if msg.media_group_id:
#        r.set("media:insta", f"{m.chat.id}&&&{m.id}", ex=10)
#        msg = await userbot.copy_media_group("iwwbot", "instasavegrambot",msg.id)
#     else:
#        msg = await msg.download("./")
#        try:
#           return await m.reply_video(msg)
#        except:
#           pass
#        try:
#           return await m.reply_animation(msg)
#        except:
#           pass
       
#        try:
#           return await m.reply_photo(msg)
#        except:
#           pass
       
#        try:
#           return await m.reply_document(msg)
#        except:
#           pass
#        os.remove(msg)
    
     
# @app.on_message(filters.private & filters.user(1920230442))
# async def mediagCopy(c,m):
#    if r.get("media:insta") and m.media_group_id:
#       chat_id = r.get("media:insta").split("&&&")[0]
#       id = r.get("media:insta").split("&&&")[1]
#       await c.copy_media_group(int(chat_id), m.from_user.id, m.id,reply_to_message_id=int(id))
#       r.delete("media:insta")
      

app.start()
# userbot.start()
print('''
[===========================]

█████═   ██         ██   ██   ██████
██    █    ██         ██   ██   ██
██████   ██         ██   ██   ██████
██    █    ██         ██   ██   ██
██████   ██████   █████    ██████

[===========================]

🔮 Your bot started successfully on Blue ☆ Source 🔮

•••••••• @M3D_l - @M3D_l •••••••••


''')
print('''

100% 
█=█=█=█=█=█=█=█=█=█''')
if r.get(f'DevGroup:{Dev_Blue}'):
  id = int(r.get(f'DevGroup:{Dev_Blue}'))
  try:
    app.send_message(id, "تم اتشغيل البوت بنجاح ✔️")
  except:
    pass
idle()
  
