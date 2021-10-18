import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

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

@bot.event
async def on_member_join(member):
  print(f'{member}加入了')
  channel = bot.get_channel(479169635015458817)
  await channel.send(f'{member.mention} 加入了')

@bot.event
async def on_member_remove(member):
  print(f'{member}離開了')
  channel = bot.get_channel(479170776851808256)
  await channel.send(f'**{member}** 離開了')

load_dotenv()
bot.run(os.getenv('TOKEN'))
