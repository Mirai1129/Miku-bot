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

load_dotenv()
bot.run(os.getenv('TOKEN'))
