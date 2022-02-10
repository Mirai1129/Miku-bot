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
    #產生訊息時的通知
    async def on_message(self, ctx):
        channel_id = ctx.channel.id
        message_id = ctx.id
        self.channel = self.bot.get_channel(int(jdata['Messagelog_channel']))
        if ctx.author != self.bot.user and ctx.author.bot != True:
            #with open('message.json', 'w', encoding='utf-8') as f:
            #json.dump(messagelog, f)
            embed = discord.Embed(title="有人建立訊息",
                                  description=ctx.content,
                                  color=0x00ff15,
                                  timestamp=datetime.datetime.utcnow())
            #embed.description("這是訊息")
            embed.add_field(name="頻道", value=ctx.channel, inline=True)
            embed.add_field(name="頻道Id", value=ctx.channel.id, inline=True)
            embed.add_field(name="訊息Id", value=ctx.id, inline=False)
            embed.set_author(name=ctx.author,
                             icon_url=ctx.author.avatar_url,
                             url=ctx.author.avatar_url)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text="用戶Id: %s" % ctx.id)
            await self.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        self.channel = self.bot.get_channel(int(jdata['Messagelog_channel']))
        if before.author != self.bot.user:
            if before.content != after.content:
                if before.author.bot != True:
                    embed = discord.Embed(title="有人編輯訊息",
                                        description="%s --> %s" % (before.content, after.content),
                                        color=0xf28f00,
                                        timestamp=datetime.datetime.utcnow())
                    #embed.description("這是訊息")
                    embed.add_field(name="頻道", value=before.channel, inline=True)
                    embed.add_field(name="頻道Id", value=before.channel.id, inline=True)
                    embed.add_field(name="訊息Id", value=before.id, inline=False)
                    embed.set_author(name=before.author,
                                    icon_url=before.author.avatar_url,
                                    url=before.author.avatar_url)
                    embed.set_thumbnail(url=before.author.avatar_url)
                    embed.set_footer(text="用戶Id: %s" % before.id)
                    await self.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.channel = self.bot.get_channel(int(jdata['Messagelog_channel']))
        if message.author != self.bot.user:
            embed = discord.Embed(title="有人刪除訊息",
                                      description=message.content,
                                      color=0xff0000,
                                      timestamp=datetime.datetime.utcnow())
                #embed.description("這是訊息")
            embed.add_field(name="頻道", value=message.channel, inline=True)
            embed.add_field(name="頻道Id", value=message.channel.id, inline=True)
            embed.add_field(name="訊息Id", value=message.id, inline=False)
            embed.set_author(name=message.author,
                                 icon_url=message.author.avatar_url,
                                 url=message.author.avatar_url)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text="用戶Id: %s" % message.id)
        await self.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Messagelog(bot))
