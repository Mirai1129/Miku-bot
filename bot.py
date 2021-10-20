import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import os

# 宣告 jfile
with open('setting.json', 'r', encoding = 'utf8') as jfile:
  jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print('Bot 上線拉')

    #online（上線）,offline（下線),idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.online
    #playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.watching,
                                    name="哈囉阿~")
    await bot.change_presence(status=status_w, activity=activity_w)

#member join 訊息
@bot.event
async def on_member_join(member):
  print(f'{member}加入了')
  channel = bot.get_channel(int(jdata['Welcome_channel'])) 
  # json傳回資料為str 轉換為int
  await channel.send(f'{member.mention} 加入了')

#member left 訊息
@bot.event
async def on_member_remove(member):
  print(f'{member}離開了')
  channel = bot.get_channel(int(jdata['Leave_channel']))
  await channel.send(f'**{member}** 離開了')

for filename in os.listdir('./cmds'):
  if filename.endswith('.py'):
    bot.load_extension(f'cmds.{filename[:-3]}')


if __name__ == "__main__":
  bot.run(jdata['TOKEN'])
