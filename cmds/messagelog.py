import discord
from discord.ext import commands
from core.classes import Cog_Extension  # 從core資料夾 import Cog_Extension這個class
import json
import datetime
import time

# 宣告 jfile
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Messagelog(Cog_Extension):
    #訊息產生
    @commands.Cog.listener()
    async def on_message(self, ctx):
        messagelog = []
        channel_id = ctx.channel.id
        message_id = ctx.id
        self.channel = self.bot.get_channel(int(jdata['messagelog_channel']))
        if ctx.author != self.bot.user:
            print(ctx.channel.id)
            with open('message.json', 'w', encoding='utf-8') as f:
                json.dump(messagelog, f)
            embed = discord.Embed(title="有人建立訊息", description=ctx.content, color=0x00ff15, timestamp=datetime.datetime.utcnow())
            #embed.description("這是訊息")
            embed.add_field(name="頻道", value=ctx.channel, inline=True)
            embed.add_field(name="頻道Id", value=ctx.channel.id, inline=True)
            embed.add_field(name="訊息Id", value=ctx.id, inline=False)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url, url=ctx.author.avatar_url)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text="用戶Id: %s" %ctx.id)
            print("hi")
            await self.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Messagelog(bot))
