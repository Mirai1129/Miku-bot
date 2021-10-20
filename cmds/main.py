import discord
from discord.ext import commands
from core.classes import Cog_Extension # 從core資料夾 import Cog_Extension這個class
import json

# 宣告 jfile
with open('setting.json', 'r', encoding = 'utf8') as jfile:
  jdata = json.load(jfile)

class Main(Cog_Extension):

  #ping指令 ctx = content
  @commands.command()
  async def ping(self, ctx): # class底下的 def()前面要加arguement
    await ctx.send(f'{round(self.bot.latency*1000)} 毫秒') 
  # bot.latency 機器人延遲時間 預設時間為s
  # round 小數點四捨五入

def setup(bot):
  bot.add_cog(Main(bot))
  