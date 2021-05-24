# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Instructions", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://telegra.ph/file/f3355429254bb12fd1ae5.jpg"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

𝒲ℯ𝓁𝒸ℴ𝓂ℯ 𝓉ℴ 𝒲𝒶𝓉𝒸𝒽 𝒶𝓃𝒾𝓂ℯ 𝒯.𝒱 , 𝒽ℯ𝓇ℯ 𝓎ℴ𝓊 𝒸𝒶𝓃 𝒹ℴ𝓌𝓃𝓁ℴ𝒶𝒹 ℴ𝓇 𝓌𝒶𝓉𝒸𝒽 𝒶𝓃𝒾𝓂ℯ 𝒻ℴ𝓇 𝒻𝓇ℯℯ 🤩🤩

!!!  __𝒫𝓁ℯ𝒶𝓈ℯ 𝓇ℯ𝒶𝒹 𝒶𝓁𝓁 𝓉𝒽ℯ 𝒾𝓃𝓈𝓉𝓇𝓊𝒸𝓉𝒾ℴ𝓃𝓈 𝒶𝒷ℴ𝓊𝓉 𝓉𝒽ℯ 𝒷ℴ𝓉 𝒷ℯ𝒻ℴ𝓇ℯ 𝓊𝓈𝒾𝓃ℊ__  

𝒟ℴ /𝓈ℯ𝒶𝓇𝒸𝒽 𝓉ℴ 𝓈ℯ𝒶𝓇𝒸𝒽 𝒶𝓃𝓎 𝒶𝓃𝒾𝓂ℯ""", reply_markup=reply_markup, parse_mode="markdown")
