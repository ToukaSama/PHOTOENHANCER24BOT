#Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ
from __future__ import unicode_literals
import os, asyncio, time, random 
import requests, wget, math
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from PIL import Image, ImageEnhance, ImageOps
from pyrogram import Client, filters, enums
from sh_bots.font_list import Fonts
from pyrogram.types import *
from telegraph import upload_file
from pyrogram.enums import ChatAction
from pyrogram.errors import UserNotParticipant, UserBannedInChannel 
from lexica import AsyncClient
from utils import getFile
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
import cv2
import numpy as np
from PIL import Image, ImageDraw


INFO_TXT = """
🕵🏻 **User Info:**
🆔 **ID**: `{id}`
🌐 **DC**: `{dc}` 
👤 **First Name**: `{n}`
🔘 **Username**: `@{u}`
"""
  
# Store the photos temporarily in a dictionary
photo_dict = {}

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24

# Retrieve your Telegram API credentials and bot token
API_ID = int(os.environ.get("API_ID", "10811400"))
API_HASH = os.environ.get("API_HASH", "191bf5ae7a6c39771e7b13cf4ffd1279")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6409704598:AAGB9Yl8c1x7QQUEiBCs5SWeEZ-mvGsj8fs")
ADMIN = int(os.environ.get("ADMIN", "6756856101"))
RemoveBG_API = os.environ.get("RemoveBG_API", "24Lc9RTfcMEXPx1Y7MU89afF")
FSUB_CHANNEL = os.environ.get("FSUB_CHANNEL", "Sunrises24botupdates")
SUNRISES_PIC = os.environ.get("SUNRISES_PIC", "https://graph.org/file/38539dde74f07062c775d.jpg") #Telegraph link Start Pic 

API = "https://apis.xditya.me/lyrics?song="

START_TEXT = """
Hᴇʟʟᴏ Mᴀᴡᴀ ❤️ Wᴇʟᴄᴏᴍᴇ! Sᴇɴᴅ ᴍᴇ ᴀɴ ɪᴍᴀɢᴇ ᴀɴᴅ ᴄʜᴏᴏꜱᴇ ᴀɴ ᴀᴄᴛɪᴏɴ.
"""

# Initialize the Pyrogram client
app = Client(
    "image_editor_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):       
    if FSUB_CHANNEL:
        try:
            # Check if the user is banned
            user = await client.get_chat_member(FSUB_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await message.reply_text("Sᴏʀʀʏ, Yᴏᴜ ᴀʀᴇ **B ᴀ ɴ ɴ ᴇ ᴅ**")
                return
        except UserNotParticipant:
            # If the user is not a participant, prompt them to join
            await message.reply_text(
                text="**❤️ Pʟᴇᴀꜱᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Bᴇғᴏʀᴇ Uꜱɪɴɢ Mᴇ ❤️**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="➕ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ ➕", url=f"https://t.me/{FSUB_CHANNEL}")]
                ])
            )
            return
        else:
            # If the user is not banned and is a participant, send the start message with the start pic
            start_text = START_TEXT.format(message.from_user.first_name) if hasattr(message, "message_id") else START_TEXT
            await message.reply_photo(
                photo=SUNRISES_PIC,
                caption=start_text,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻", url=f"https://t.me/Sunrises_24"),
                         InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ 📢", url="https://t.me/Sunrises24BotUpdates")],
                        [InlineKeyboardButton("Support ❤️‍🔥", url="https://t.me/Sunrises24botSupport"),
                         InlineKeyboardButton("Cʜᴀɴɴᴇʟ 🎞️", url="https://t.me/sunriseseditsoffical6")]
                    ]
                ),
                reply_to_message_id=getattr(message, "message_id", None)
            )
            return

print("Bot Started!🦋 © t.me/Sunrises_24")

# Function to handle /help command
@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = """
    <b>Hᴇʟʟᴏ Mᴀᴡᴀ ❤️
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.

🦋 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Photo 🖼️

/giveaway - 𝐺𝑖𝑣𝑒𝑎𝑤𝑎𝑦 𝐼𝑛 𝐺𝑟𝑜𝑢𝑝 𝑂𝑛𝑙𝑦 [𝐴𝐷𝑀𝐼𝑁]
/collage - 𝑆𝑒𝑛𝑑 10 𝑃ℎ𝑜𝑡𝑜𝑠 𝑇𝑜 𝑚𝑎𝑘𝑒 𝑐𝑜𝑙𝑙𝑎𝑔𝑒 𝑖𝑛 𝑐𝑜𝑙𝑢𝑚𝑛𝑠
/portrait - 𝐶𝑜𝑛𝑣𝑒𝑟𝑡 𝑖𝑚𝑎𝑔𝑒 𝑡𝑜 𝑃𝑜𝑟𝑡𝑟𝑎𝑖𝑡
/grayscale - 𝐶𝑜𝑛𝑣𝑒𝑟𝑡 𝑖𝑚𝑎𝑔𝑒 𝑡𝑜 𝑔𝑟𝑎𝑦𝑠𝑐𝑎𝑙𝑒
/enhance - 𝐸𝑛ℎ𝑎𝑛𝑐𝑒 𝑖𝑚𝑎𝑔𝑒
/changecolor - 𝐶ℎ𝑎𝑛𝑔𝑒 𝑃ℎ𝑜𝑡𝑜 𝐶𝑜𝑙𝑜𝑟
/resizephoto - 𝑇𝑜 𝑎𝑑𝑗𝑢𝑠𝑡 𝑡ℎ𝑒 𝑑𝑖𝑚𝑒𝑛𝑠𝑖𝑜𝑛𝑠 𝑜𝑓 𝑎𝑛 𝑖𝑚𝑎𝑔𝑒
/removebgsticker -  𝑇𝑜 𝑟𝑒𝑚𝑜𝑣𝑒 𝑡ℎ𝑒 𝑏𝑎𝑐𝑘𝑔𝑟𝑜𝑢𝑛𝑑 𝑓𝑟𝑜𝑚 𝑎𝑛 𝑆𝑡𝑖𝑐𝑘𝑒𝑟
/removebgplain -  𝑇𝑜 𝑟𝑒𝑚𝑜𝑣𝑒 𝑡ℎ𝑒 𝑏𝑎𝑐𝑘𝑔𝑟𝑜𝑢𝑛𝑑 𝑓𝑟𝑜𝑚 𝑎𝑛 𝑃𝑙𝑎𝑖𝑛 𝑖𝑚𝑎𝑔𝑒
/removebgwhite -  𝑇𝑜 𝑟𝑒𝑚𝑜𝑣𝑒 𝑡ℎ𝑒 𝑏𝑎𝑐𝑘𝑔𝑟𝑜𝑢𝑛𝑑 𝑓𝑟𝑜𝑚 𝑎𝑛 𝑊ℎ𝑖𝑡𝑒 𝑖𝑚𝑎𝑔𝑒
/telegraph - 𝑇𝑜 𝑔𝑒𝑡 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑝ℎ 𝐿𝑖𝑛𝑘 🔗
/about - 𝐿𝑒𝑎𝑟𝑛 𝑚𝑜𝑟𝑒 𝑎𝑏𝑜𝑢𝑡 𝑡ℎ𝑖𝑠 𝑏𝑜𝑡

◉Iᴅ Oʀ Iɴғᴏ
/info - 𝑇𝑜 𝐾𝑛𝑜𝑤 𝑡ℎ𝑒 𝑈𝑠𝑒𝑟 𝐼𝑛𝑓𝑜 𝐵𝑦 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 🆔

◉ ғᴏɴᴛ 
/font - 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑤𝑖𝑡ℎ 𝑡𝑒𝑥𝑡 𝑡𝑜 𝐹𝑜𝑛𝑡 🔠
Enter Any Text Eg:- /font [text]

◉ YᴏᴜTᴜʙᴇ
/song - 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 𝑌𝑜𝑢𝑟 𝑆𝑜𝑛𝑔 𝐹𝑟𝑜𝑚 𝑌𝑜𝑢𝑇𝑢𝑏𝑒 🎵
/video - 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 𝑌𝑜𝑢𝑟 𝑉𝑖𝑑𝑒𝑜 𝑆𝑜𝑛𝑔 𝐹𝑟𝑜𝑚 𝑌𝑜𝑢𝑇𝑢𝑏𝑒 🎞️

◉ Lʏʀɪᴄs 
/lyrics - 𝑇𝑜 𝑔𝑒𝑡 𝑙𝑦𝑟𝑖𝑐𝑠 𝑜𝑓 𝑠𝑜𝑛𝑔𝑠 📝🎶

◉ Rᴇᴘᴏ🖇️
/repo - 𝑇𝑜 𝑠𝑒𝑎𝑟𝑐ℎ 𝑟𝑒𝑝𝑜 𝑓𝑟𝑜𝑚 𝐺𝑖𝑡𝐻𝑢𝑏 🖇️

 💭This bot is designed to apply filters to images.
 
🔱 𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 : <a href='https://t.me/Sunrises_24'>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™</a></b>
    
   """
    await message.reply_text(help_text)
    
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Function to handle /about command
@app.on_message(filters.command("about"))
async def about_command(client, message):
    about_text = """
<b>✯ Mʏ Nᴀᴍᴇ :  <a href=https://t.me/PHOTOENHANCER24BOT>🦋Pʜᴏᴛᴏ Eɴʜᴀɴᴄᴇʀ 𝟸𝟺 Bᴏᴛ🦋</a></b></b>
<b>✯ Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻 : <a href=https://t.me/Sunrises_24>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™ ✨</a></b>
<b>✯ Uᴘᴅᴀᴛᴇs 📢 : <a href=https://t.me/Sunrises24BotUpdates>𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢</a></b>
<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs 📊 : ᴠ2 [Sᴛᴀʙʟᴇ]</b>
    """
    await message.reply_text(about_text)

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#Ping
@app.on_message(filters.command("ping"))
async def ping(client, message):
    start_t = time.time()
    rm = await message.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!📍\n{time_taken_s:.3f} ms")
    
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24   
#Function to handle /grayscale command
@app.on_message(filters.command("grayscale"))
async def grayscale_command(client, message):
    if message.reply_to_message:
        photo = await message.reply_to_message.download()
        grayscale_image = convert_to_grayscale(photo)
        grayscale_image_path = "grayscale_" + str(message.chat.id) + ".png"
        grayscale_image.save(grayscale_image_path)
        await message.reply_photo(
            photo=grayscale_image_path,
            caption="Grayscale filter applied!"
        )
        os.remove(grayscale_image_path)
    else:
        await message.reply_text("Please reply to an image to apply the grayscale filter.")

# Function to convert image to grayscale
def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    return grayscale_image

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Function to handle /enhance command
@app.on_message(filters.command("enhance"))
async def enhance_command(client, message):
    if message.reply_to_message:
        photo = await message.reply_to_message.download()
        enhanced_image = enhance_image(photo)
        enhanced_image_path = "enhanced_" + str(message.chat.id) + ".png"
        enhanced_image.save(enhanced_image_path)
        await message.reply_photo(
            photo=enhanced_image_path,
            caption="Enhanced image!"
        )
        os.remove(enhanced_image_path)
    else:
        await message.reply_text("Please reply to an image to apply enhancement.")
        
# Function to enhance an image
def enhance_image(image_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(1.5)  # Adjust enhancement factor as needed
    return enhanced_image
    
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Function to handle /changecolor command
@app.on_message(filters.command("changecolor"))
async def changecolor_command(client, message):
   if message.reply_to_message:
       photo = await message.reply_to_message.download()
       new_color = change_color(photo)
       new_color_path = "new_color_" + str(message.chat.id) + ".png"
       new_color.save(new_color_path)
       await message.reply_photo(
           photo=new_color_path,
           caption="Photo color changed!"
       )
       os.remove(new_color_path)
   else:
       await message.reply_text("Please reply to an image to apply Photo Colour.")
        
# Function to change Photo color
def change_color(image_path, new_color=(255, 0, 0)):
    image = Image.open(image_path)
    # Assuming the shirt is red, changing the color to a new_color
    image = ImageOps.colorize(image.convert('L'), black="black", white=new_color)
    return image

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Function to Telegraph 
@app.on_message(filters.command("telegraph") & filters.private)
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("Rᴇᴘʟʏ Tᴏ Pʜᴏᴛᴏ ᴏʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ 𝟻 MB")
    if not ( replied.photo or replied.video ):
        return await update.reply_text("Pʟᴇᴀꜱᴇ Rᴇᴘʟʏ Wɪᴛʜ A Vᴀʟɪᴅ Mᴇᴅɪᴀ")
    text = await update.reply_text("<code>Dᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛᴏ Hᴀʀꜱʜᴀ'ꜱ  Sᴇʀᴠᴇʀ...</code>", disable_web_page_preview=True)   
    media = await replied.download()   
    await text.edit_text("<code>Dᴏᴡɴʟᴏᴀᴅɪɴɢ Cᴏᴍᴘʟᴇᴛᴇᴅ Nᴏᴡ I Aᴍ Uᴘʟᴏᴀᴅɪɴɢ ᴛᴇʟᴇɢʀᴀᴘʜ Lɪɴᴋ...</code>", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        return await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)          
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"<b>Link :-</b>\n\n<code>https://graph.org{response[0]}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="Oᴘᴇɴ Lɪɴᴋ 🔗", url=f"https://graph.org{response[0]}"),
            InlineKeyboardButton(text="Sʜᴀʀᴇ Lɪɴᴋ", url=f"https://telegram.me/share/url?url=https://graph.org{response[0]}")            
            ]]
        )
    )


@app.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = await message.reply(f"**ѕєαrchíng чσur ѕσng...!\n {query}**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        performer = f"[Sᴜɴʀɪꜱᴇꜱ™]" 
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
    except Exception as e:
        print(str(e))
        return await m.edit("**𝙵𝙾𝚄𝙽𝙳 𝙽𝙾𝚃𝙷𝙸𝙽𝙶 𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝚃𝙷𝙴 𝚂𝙿𝙴𝙻𝙻𝙸𝙽𝙶 𝙾𝚁 𝙲𝙷𝙴𝙲𝙺 𝚃𝙷𝙴 𝙻𝙸𝙽𝙺**")
                
    await m.edit("**Dᴏᴡɴʟᴏᴀᴅɪɴɢ Yᴏᴜʀ Sᴏɴɢ Fʀᴏᴍ YᴏᴜTᴜʙᴇ 🎵!**")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        cap = "**BY›› [Sᴜɴʀɪꜱᴇꜱ™](https://t.me/sunrises24botupdates)**"
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        await message.reply_audio(
            audio_file,
            caption=cap,            
            quote=False,
            title=title,
            duration=dur,
            performer=performer,
            thumb=thumb_name
        )            
        await m.delete()
    except Exception as e:
        await m.edit("**🚫 𝙴𝚁𝚁𝙾𝚁 🚫**")
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

def get_text(message: Message) -> [None,str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


@app.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)
    pablo = await client.send_message(message.chat.id, f"**Dᴏᴡɴʟᴏᴀᴅɪɴɢ Yᴏᴜʀ Vɪᴅᴇᴏ Sᴏɴɢ Fʀᴏᴍ YᴏᴜTᴜʙᴇ 🎞️** `{urlissed}`")
    if not urlissed:
        return await pablo.edit("Invalid Command Syntax Please Check help Menu To Know More!")     
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        return await pablo.edit_text(f"**𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚊𝚒𝚕𝚎𝚍 𝙿𝚕𝚎𝚊𝚜𝚎 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗..♥️** \n**Error :** `{str(e)}`")       
    
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""**𝚃𝙸𝚃𝙻𝙴 :** [{thum}]({mo})\n**𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :** {message.from_user.mention}"""

    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,        
        reply_to_message_id=message.id 
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Function to Repo
@app.on_message(filters.command("repo"))
async def repo(client, message):
    if len(message.command) > 1:
        query = ' '.join(message.command[1:])
        response = requests.get(f"https://api.github.com/search/repositories?q={query}")
        if response.status_code == 200:
            data = response.json()
            if data['total_count'] > 0:
                repo = data['items'][0] 
                reply = f"**{repo['name']}**\n\n" \
                        f"**📝 ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:** <code>{repo['description']}</code>\n" \
                        f"**🔗 ᴜʀʟ:** {repo['html_url']}\n" \
                        f"**🌟 sᴛᴀʀs:** <code>{repo['stargazers_count']}</code>\n" \
                        f"**🪝 ғᴏʀᴋs:** <code>{repo['forks_count']}</code>"

                await message.reply_text(reply)
            else:
                await message.reply_text("ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ.")
        else:
            await message.reply_text("ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ.")
    else:
        await message.reply_text("ᴜsᴀɢᴇ: /repo {repo_name}")

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Function to handle /resizephoto command
@app.on_message(filters.command("resizephoto"))
async def resize_photo_command(client, message):
    if message.reply_to_message:
        photo = await message.reply_to_message.download()
        resized_image = resize_photo(photo)
        resized_image_path = "resized_" + str(message.chat.id) + ".png"
        resized_image.save(resized_image_path)
        await message.reply_photo(
            photo=resized_image_path,
            caption="Resized image!"
        )
        os.remove(resized_image_path)
    else:
        await message.reply_text("Please reply to an image to resize.")

# Function to resize an image
def resize_photo(image_path):
    image = Image.open(image_path)
    resized_image = ImageOps.fit(image, (300, 300))  # Adjust the size as needed
    return resized_image

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Define the command to retrieve lyrics
@app.on_message(filters.command("lyrics"))
async def sng(client, message):
        if not message.reply_to_message:
          await message.reply_text("Please reply to a message")
        else:          
          mee = await message.reply_text("`Searching 🔎`")
          song = message.reply_to_message.text
          chat_id = message.from_user.id
          rpl = lyrics(song)
          await mee.delete()
          try:
            await mee.delete()
            await client.send_message(chat_id, text = rpl, reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs ", url = f"t.me/Sunrises24BotUpdates")]]))
          except Exception as e:                            
             await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"t.me/Sunrises24BotUpdates")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Sᴜᴄᴄᴇꜱꜰᴜʟʟy Exᴛʀᴀᴄᴛᴇᴅ Lyɪʀɪᴄꜱ Oꜰ {song}**\n\n'
        text += f'`{fin["lyrics"]}`'
        text += f'\n\n\n**Made By Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ**'
        return text

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Define the command to  Removebgsticker 
@app.on_message(filters.command("removebgsticker"))
async def removebg_sticker(client, message):
    try:
        if not (RemoveBG_API == ""):
            userid = str(message.chat.id)
            if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                os.makedirs(f"./DOWNLOADS/{userid}")
            download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
            edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "nobgsticker.webp"
            if not message.reply_to_message.empty:
                msg = await message.reply_to_message.reply_text(
                    "<b>𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝙼𝙰𝙶𝙴....</b>", quote=True
                )
                await client.download_media(
                    message=message.reply_to_message, file_name=download_location
                )
                await msg.edit("<b>𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝙼𝙰𝙶𝙴....</b>")

                response = requests.post(
                    "https://api.remove.bg/v1.0/removebg",
                    files={"image_file": open(download_location, "rb")},
                    data={"size": "auto"},
                    headers={"X-Api-Key": RemoveBG_API},
                )
                if response.status_code == 200:
                    with open(f"{edit_img_loc}", "wb") as out:
                        out.write(response.content)
                else:
                    await message.reply_to_message.reply_text(
                        "Check if your api is correct", quote=True
                    )
                    return

                await message.reply_chat_action(ChatAction.UPLOAD_PHOTO)
                await message.reply_to_message.reply_sticker(edit_img_loc, quote=True)
                await msg.delete()
            else:
                await message.reply_text("Why did you delete that??")
            try:
                shutil.rmtree(f"./DOWNLOADS/{userid}")
            except Exception:
                pass
        else:
            await message.reply_to_message.reply_text(
                "Get the api from https://www.remove.bg/b/background-removal-api and add in Config Var",
                quote=True,
                disable_web_page_preview=True,
            )
    except Exception as e:
        print("removebg_sticker-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return


#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Define the command to  RemovebgPlain
@app.on_message(filters.command("removebgplain"))                
async def removebg_plain(client, message):
    try:
        if not (RemoveBG_API == ""):
            userid = str(message.chat.id)
            if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                os.makedirs(f"./DOWNLOADS/{userid}")
            download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
            edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "nobgplain.png"
            if not message.reply_to_message.empty:
                msg = await message.reply_to_message.reply_text(
                    "<b>𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝙼𝙰𝙶𝙴....</b>", quote=True
                )
                await client.download_media(
                    message=message.reply_to_message, file_name=download_location
                )
                await msg.edit("<b>𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝙼𝙰𝙶𝙴....</b>")

                response = requests.post(
                    "https://api.remove.bg/v1.0/removebg",
                    files={"image_file": open(download_location, "rb")},
                    data={"size": "auto"},
                    headers={"X-Api-Key": RemoveBG_API},
                )
                if response.status_code == 200:
                    with open(f"{edit_img_loc}", "wb") as out:
                        out.write(response.content)
                else:
                    await message.reply_to_message.reply_text(
                        "Check if your api is correct", quote=True
                    )
                    return

                await message.reply_chat_action(ChatAction.UPLOAD_DOCUMENT)
                await message.reply_to_message.reply_document(edit_img_loc, quote=True)
                await msg.delete()
            else:
                await message.reply_text("Why did you delete that??")
            try:
                shutil.rmtree(f"./DOWNLOADS/{userid}")
            except Exception:
                pass
        else:
            await message.reply_to_message.reply_text(
                "Get the api from https://www.remove.bg/b/background-removal-api and add in Config Var",
                quote=True,
                disable_web_page_preview=True,
            )
    except Exception as e:
        print("removebg_plain-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return
                
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Define the command to  RemovebgWhite
@app.on_message(filters.command("removebgwhite"))
async def removebg_white(client, message):
    try:
        if not (RemoveBG_API == ""):
            userid = str(message.chat.id)
            if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                os.makedirs(f"./DOWNLOADS/{userid}")
            download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
            edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "nobgwhite.png"
            if not message.reply_to_message.empty:
                msg = await message.reply_to_message.reply_text(
                    "<b>𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝙼𝙰𝙶𝙴....</b>", quote=True
                )
                await client.download_media(
                    message=message.reply_to_message, file_name=download_location
                )
                await msg.edit("<b>𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝙼𝙰𝙶𝙴....</b>")

                response = requests.post(
                    "https://api.remove.bg/v1.0/removebg",
                    files={"image_file": open(download_location, "rb")},
                    data={"size": "auto"},
                    headers={"X-Api-Key": RemoveBG_API},
                )
                if response.status_code == 200:
                    with open(f"{edit_img_loc}", "wb") as out:
                        out.write(response.content)
                else:
                    await message.reply_to_message.reply_text(
                        "Check if your api is correct", quote=True
                    )
                    return

                await message.reply_chat_action(ChatAction.UPLOAD_PHOTO)
                await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
                await msg.delete()
            else:
                await message.reply_text("Why did you delete that??")
            try:
                shutil.rmtree(f"./DOWNLOADS/{userid}")
            except Exception:
                pass
        else:
            await message.reply_to_message.reply_text(
                "Get the api from https://www.remove.bg/b/background-removal-api and add in Config Var",
                quote=True,
                disable_web_page_preview=True,
            )
    except Exception as e:
        print("removebg_white-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return
                
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
# Define the command to  Fonts
@app.on_message(filters.private & filters.command(["font"]))
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛', callback_data='style+typewriter'),
        InlineKeyboardButton('𝕆𝕦𝕥𝕝𝕚𝕟𝕖', callback_data='style+outline'),
        InlineKeyboardButton('𝐒𝐞𝐫𝐢𝐟', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('𝑺𝒆𝒓𝒊𝒇', callback_data='style+bold_cool'),
        InlineKeyboardButton('𝑆𝑒𝑟𝑖𝑓', callback_data='style+cool'),
        InlineKeyboardButton('Sᴍᴀʟʟ Cᴀᴘs', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('𝓈𝒸𝓇𝒾𝓅𝓉', callback_data='style+script'),
        InlineKeyboardButton('𝓼𝓬𝓻𝓲𝓹𝓽', callback_data='style+script_bolt'),
        InlineKeyboardButton('ᵗⁱⁿʸ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('ᑕOᗰIᑕ', callback_data='style+comic'),
        InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
        InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
        InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
        InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎', callback_data='style+circles')
        ],[
        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),
        ],[      
        InlineKeyboardButton('Next ➡️', callback_data="nxt")
    ]]
    if not cb:
        if ' ' in m.text:
            title = m.text.split(" ", 1)[1]
            await m.reply_text(title, reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=m.id)                     
        else:
            await m.reply_text(text="Enter Any Text Eg:- `/font [text]`")    
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))



#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
@app.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('🇸 🇵 🇪 🇨 🇮 🇦 🇱 ', callback_data='style+special'),
            InlineKeyboardButton('🅂🅀🅄🄰🅁🄴🅂', callback_data='style+squares'),
            InlineKeyboardButton('🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎', callback_data='style+squares_bold'),
            ],[            
            InlineKeyboardButton('U͟n͟d͟e͟r͟l͟i͟n͟e͟', callback_data='style+underline'),            
            ],[
            InlineKeyboardButton('⬅️ Back', callback_data='nxt+0'),
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
@app.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic 
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'underline':
        cls = Fonts.underline

    r, oldtxt = m.message.reply_to_message.text.split(None, 1) 
    new_text = cls(oldtxt)            
    try:
        await m.message.edit_text(f"`{new_text}`\n\n👆🏻 Click To Copy", reply_markup=m.message.reply_markup)
    except Exception as e:
        print(e)      
                  
@app.on_message(filters.command(["portrait"]))
async def upscaleImages(client, message):
    file = await getFile(message)
    if file == 1:
       return await message.reply_text("File size is large")
    if file is None:
       return await message.reply_text("Please reply to an image to apply portrait image.")
    msg = await message.reply("Wait a min, Uploading From Harsha's Server..⚡")
    imageBytes = open(file,"rb").read()
    os.remove(file)
    upscaledImage = await UpscaleImages(imageBytes)
    try:
      await message.reply_document(open(upscaledImage,"rb"))
      await msg.delete()
      os.remove(upscaledImage)
    except Exception as e:
       await msg.edit(f"{e}")
        
async def UpscaleImages(image: bytes) -> str:
    """
    Portrait an image and return with Portrait image path.
    """
    client = AsyncClient()
    content = await client.upscale(image)
    await client.close()
    upscaled_file_path = "portrait.png"
    with open(upscaled_file_path, "wb") as output_file:
        output_file.write(content)
    return upscaled_file_path


@app.on_message(filters.command("collage") & filters.private)
async def collage_command(client, message):
    user_id = message.from_user.id
    photo_dict[user_id] = []
    await message.reply_text("Please send me 10 photos to create a collage.")

@app.on_message(filters.photo & filters.private)
async def collect_photos(client, message):
    user_id = message.from_user.id
    if user_id in photo_dict:
        try:
            photo_path = await message.download()
            if photo_path:
                photo_dict[user_id].append(photo_path)
                photo_count = len(photo_dict[user_id])
                if photo_count < 10:
                    await message.reply_text(f"Received {photo_count} photo(s). Please send {10 - photo_count} more photo(s).")
                elif photo_count == 10:
                    await message.reply_text(
                        "You have uploaded 10 photos. Click the button below to create the collage.",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Create Collage", callback_data="create_collage")]]
                        )
                    )
            else:
                await message.reply_text("Failed to download the photo. Please try again.")
        except Exception as e:
            await message.reply_text(f"An error occurred: {e}")

@app.on_callback_query(filters.regex("create_collage"))
async def create_collage_callback(client, callback_query):
    user_id = callback_query.from_user.id
    
    if user_id in photo_dict and len(photo_dict[user_id]) == 10:
        photos = photo_dict[user_id]
        try:
            collage = create_collage(photos)
            collage_path = f"collage_{user_id}.png"
            collage.save(collage_path)
            
            await client.send_photo(
                chat_id=callback_query.message.chat.id,
                photo=collage_path,
                caption="Here's your collage!"
            )
            os.remove(collage_path)
        except Exception as e:
            await callback_query.message.reply_text(f"Failed to create collage: {e}")
        finally:
            # Clear the user's photo list and delete uploaded photos
            for photo in photo_dict[user_id]:
                if os.path.exists(photo):
                    os.remove(photo)
            del photo_dict[user_id]
    else:
        await callback_query.answer("You need to upload exactly 10 photos.", show_alert=True)

def create_collage(image_paths, collage_width=1000):
    images = [Image.open(image_path) for image_path in image_paths]
    
    # Resize images to be the same width and height
    img_width, img_height = images[0].size
    for i in range(1, len(images)):
        images[i] = images[i].resize((img_width, img_height))
    
    # Calculate the total collage height for five rows of images
    collage_height = img_height * 5
    collage = Image.new('RGB', (img_width * 2, collage_height))
    
    # Positioning images in two columns
    x_offsets = [0, img_width]  # Two columns
    for i in range(2):  # Two columns
        y_offset = 0
        for j in range(5):  # Five images per column
            collage.paste(images[i * 5 + j], (x_offsets[i], y_offset))
            y_offset += img_height
    
    return collage

     
#info text                                              
@app.on_message(filters.command(["id", "info"]))
async def media_info(client, message):
    try:
        # Check if a user ID is provided
        if len(message.command) < 2:
            await message.reply_text("Please provide a user ID.\nUsage: `/info <telegram_user_id>`")
            return

        user_id = int(message.command[1])
        sh = await message.reply("Please wait...")

        try:
            user = await client.get_users(user_id)
        except Exception as e:
            await sh.delete()
            await message.reply_text(f"Error fetching user details: {e}")
            return

        buttons = [[
            InlineKeyboardButton("✨️ Support", url="https://t.me/Sunrises24botsupport"),
            InlineKeyboardButton("📢 Updates", url="https://t.me/Sunrises24botupdates")
        ]]
        
        if user.photo:
            user_dp = await client.download_media(message=user.photo.big_file_id)
            await message.reply_photo(
                photo=user_dp,
                caption=INFO_TXT.format(id=user.id, dc=user.dc_id, n=user.first_name, u=user.username or 'N/A'),
                reply_markup=InlineKeyboardMarkup(buttons),
                quote=True,
                parse_mode=enums.ParseMode.MARKDOWN  # Use MARKDOWN for formatting
            )
            os.remove(user_dp)
        else:
            await message.reply_text(
                text=INFO_TXT.format(id=user.id, dc=user.dc_id, n=user.first_name, u=user.username or 'N/A'),
                reply_markup=InlineKeyboardMarkup(buttons),
                quote=True,
                parse_mode=enums.ParseMode.MARKDOWN  # Use MARKDOWN for formatting
            )
        await sh.delete()

    except IndexError:
        await message.reply_text("Please provide a user ID.\nUsage: `/info <telegram_user_id>`")
    except Exception as e:
        print(e)
        await message.reply_text(f"[404] Error: {e}")



# Command to start a giveaway (only for admins)
@app.on_message(filters.command("giveaway") & filters.group & filters.user(ADMIN))
async def start_giveaway(client: Client, message: Message):
    chat_id = message.chat.id
    members = []

    # Get all members in the group
    async for member in client.get_chat_members(chat_id):
        user = member.user
        if not user.is_bot:
            members.append((user.id, user.username))

    if not members:
        await message.reply("No members found in this group.")
        return

    # Randomly select a winner
    winner_id, winner_username = random.choice(members)

    await message.reply(f"🎉 Congratulations! The winner is @{winner_username} (ID: {winner_id}). 🎉")


@app.on_message(filters.command("removetext"))
async def removetext_command(client, message):
    if message.reply_to_message:
        photo = await message.reply_to_message.download()
        brush_size = 20  # Size of the brush
        mask = create_mask(photo, brush_size)
        clean_photo = remove_text_from_photo(photo, mask)
        clean_photo_path = "clean_photo_" + str(message.chat.id) + ".png"
        clean_photo.save(clean_photo_path)
        await message.reply_photo(
            photo=clean_photo_path,
            caption="Text removed from photo!"
        )
        os.remove(clean_photo_path)
    else:
        await message.reply_text("Please reply to an image to remove text.")

def create_mask(image_path, brush_size):
    image = Image.open(image_path)
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)

    # Define the areas to be brushed out, here it is manually set for demonstration
    # In a real scenario, this should be an interactive selection
    draw.rectangle([50, 50, 150, 150], fill=255)  # Example area

    return np.array(mask)

def remove_text_from_photo(image_path, mask):
    image = cv2.imread(image_path)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    inpainted_image = cv2.inpaint(image, mask[:, :, 0], inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(inpainted_image, cv2.COLOR_BGR2RGB))



# Run the bot
app.run()
