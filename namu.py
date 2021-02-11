import discord
import urllib.request
import os
client = discord.Client()
@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    #나무위키 검색결과 받아오기
  if message.content.startswith('#나무'):
         Text=""
         learn=message.content.split(" ")
         vrsize=len(learn)
         vrsize=int(vrsize)
         for i in range(1,vrsize):
             Text=(Text+learn[i])
         
         encText=urllib.parse.quote(Text)
         link=('https://namu.wiki/w/'+encText)
         await message.channel.send(link)

client.run(os.environ['BOT_TOKEN'])