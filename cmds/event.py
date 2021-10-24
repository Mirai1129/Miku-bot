import discord
from discord.ext import commands
from core.classes import Cog_Extension # 從core資料夾 import Cog_Extension這個class
import json

# 宣告 jfile
with open('setting.json', 'r', encoding = 'utf8') as jfile:
  jdata = json.load(jfile)

class Event(Cog_Extension):
  
  #member join 訊息
  @commands.Cog.listener()  
  async def on_member_join(self, member):
    print(f'{member}加入了')
    channel = self.bot.get_channel(int(jdata['Welcome_channel'])) 
    # json傳回資料為str 轉換為int
    await channel.send(f'{member.mention} 加入了')

  #member left 訊息
  @commands.Cog.listener()  
  async def on_member_remove(self, member):
    print(f'{member}離開了')
    channel = self.bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'**{member}** 離開了')
 
  #訊息內容
  @commands.Cog.listener()
  async def on_message(self, msg):
    if msg.content == 'apple':
      await msg.channel.send('hi')

def setup(bot):
  bot.add_cog(Event(bot))