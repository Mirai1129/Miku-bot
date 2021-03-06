import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension  # 從core資料夾 import Cog_Extension這個class
import json
import time
import datetime

# 宣告 jfile
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Main(Cog_Extension):

    #ping指令 ctx = content
    @commands.command()
    async def ping(self, ctx):  # class底下的 def()前面要加arguement
        embed = nextcord.Embed(title='延遲時間(ms)',
                              description=f'{round(self.bot.latency*1000)} 毫秒',
                              color=0xb12091)
        await ctx.send(embed=embed)

    # bot.latency 機器人延遲時間 預設時間為s
    # round 小數點四捨五入

    # 崁入訊息
    @commands.command()
    async def em(self, ctx, des, auth):
        embed = nextcord.Embed(title="this is a title",
                              description=des,
                              color=0x488fdb,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=auth)
        embed.add_field(name="hi", value="value", inline=True)
        embed.set_footer(text="good morning")
        await ctx.send(embed=embed) 

    # 重複使用者說的話
    @commands.command()
    async def sayrepeat(self, ctx, *, msg):
        embed = nextcord.Embed(description=msg,
                              color=0x488fdb,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=ctx.author)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    # 清理訊息
    @commands.command()
    async def clear(self, ctx, num: int):
        await ctx.channel.purge(limit=(num + 1))

    @commands.command()
    async def emoji(self, ctx, msg):
        await ctx.message.add_reaction(msg)

    @commands.command()
    async def nowtime(self, ctx):
        await ctx.send(f'現在時間是: <t:{int(time.time())}:F>')

    #@commands.command()
    #async def help(self, ctx):
     #   await ctx.send('hi')


def setup(bot):
    bot.add_cog(Main(bot))
