

from loader import dp,bot
import requests
from pytube import YouTube
from aiogram import types

@dp.message_handler(content_types=['text'])
async def bot_echo(message: types.Message):
  my_video = YouTube(message.text)
  url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

  querystring = {"videoId": my_video.video_id, "lang": "uz", "videos": "true", "audios": "true", "subtitles": "true"}

  headers = {
    "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com",
    "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  a = response.json()
  print(a)
  t = response.json()['title']
  v = response.json()['videos']['items'][0]['url']
  d = response.json()['description']
  chanel = response.json()['channel']['name']
  print(t)
  print(v)
  print(d)



  await bot.send_video(chat_id=message.chat.id,caption=f'{t}\n\nHappy to help! Your @YouTubeApp_bot.',video=v)
  await message.answer(text=f'{d}\n\n\n{chanel}')

  print(response.text)