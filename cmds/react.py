import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension  # 從core資料夾 import Cog_Extension這個class
import random
import json

# 宣告 jfile
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def web(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)


def setup(bot):
    bot.add_cog(React(bot))
