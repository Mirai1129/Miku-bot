import discord
from discord.ext import commands
from core.classes import Cog_Extension  # 從core資料夾 import Cog_Extension這個class
import json, asyncio, datetime
import asyncio

# 宣告 jfile
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(jdata['Ready_channel']))
            while not self.bot.is_closed():  # 如果我們機器人沒有關閉的話
                await self.channel.send(f'我在<t:1635236345:F>的時候上線了')
                # https://discord.com/developers/docs/reference#message-formatting-timestamp-styles
                await asyncio.sleep(300)  # 單位: 秒

        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_ready_channel(self, ctx, ch: int):  # ch = channel
        self.channel = self.bot.get_channel(int(jdata['Ready_channel']))
        await ctx.send(f'頻道設置為: {self.channel.mention}')


def setup(bot):
    bot.add_cog(Task(bot))
