import discord
from discord.ext import commands
from core.classes import Cog_Extension  # 從core資料夾 import Cog_Extension這個class
import json
import datetime

# 宣告 jfile
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Main(Cog_Extension):

    #ping指令 ctx = content
    @commands.command()
    async def ping(self, ctx):  # class底下的 def()前面要加arguement
        embed = discord.Embed(title='延遲時間(ms)',
                              description=f'{round(self.bot.latency*1000)} 毫秒',
                              color=0xb12091)
        await ctx.send(embed=embed)

    # bot.latency 機器人延遲時間 預設時間為s
    # round 小數點四捨五入

    # 崁入訊息
    @commands.command()
    async def em(self, ctx):
        embed = discord.Embed(title="this is a title",
                              description="this is a description",
                              color=0x488fdb,
                              timestamp=datetime.datetime.now())
        embed.set_author(name="im a authoe")
        embed.add_field(name="hi", value="value", inline=True)
        embed.set_footer(text="good morning")
        await ctx.send(embed=embed)

    # 重複使用者說的話
    @commands.command()
    async def sayrepeat(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    # 清理訊息
    @commands.command()
    async def clear(self, ctx, num: int):
        await ctx.channel.purge(limit=(num + 1))


def setup(bot):
    bot.add_cog(Main(bot))
