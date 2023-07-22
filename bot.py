import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
import shutil
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery
from yt_dlp import YoutubeDL

CHOOSE_UR_LANG = " Choose Your folmula ! "
CHOOSE_UR_LANG_BUTTONS = [
    [InlineKeyboardButton("vid 360p",callback_data="vid 360p")],
     [InlineKeyboardButton("vid 720p",callback_data="vid 720p")],
     [InlineKeyboardButton("aud",callback_data="aud")]
]


bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6030811502:AAF0tj9q_2BH1HpmRZLkuvBQttmxYdYFw6o"
)
@bot.on_message(filters.command('dl') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " جار التحميل  ",disable_web_page_preview=True)
    zaza = 12
    while (zaza <= 50): 
     cmd(f'mkdir downloads')
     cmd(f'cd ./downloads/ && wget https://al-angarie.com/audio/167/a{zaza}.mp3 && cd ..' )
     zaza += 1
    cmd('uploadgram -1001821573758 ./downloads/ ')
    shutil.rmtree('./downloads/') 


bot.run()
