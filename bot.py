from encodings import CodecRegistryError
from pydoc import describe
from urllib import response
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from core.classes import Cog_Extension
import json
import os

# 宣告 jfile
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix='>', intents=intents, help_command = None)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'{bot.user} 上線拉')

    #online（上線）,offline（下線),idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = nextcord.Status.online
    #playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = nextcord.Activity(type=nextcord.ActivityType.watching,
                                  name="哈囉阿~")
    await bot.change_presence(status=status_w, activity=activity_w)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')

@bot.slash_command(name = "test", description = "test", guild_ids=[jdata['Guild_id']])
async def test(interaction: Interaction):
    await interaction.response.send_message("HEllO")


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
