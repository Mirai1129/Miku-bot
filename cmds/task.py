import discord
from discord.ext import commands
from core.classes import Cog_Extension  # 從core資料夾 import Cog_Extension這個class
import json, asyncio, datetime

# 宣告 jfile
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def setup(bot):
    bot.add_cog(Task(bot))
