import discord
from discord.ext import commands
import json
import os


with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)
    token = jdata['TOKEN']
    welcome_channel = jdata['WELCOME']
    leave_channel = jdata['LEAVE']


bot = commands.Bot(command_prefix = '[')

@bot.event
async def on_ready():
    print('bot is online')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(741865350626410506)
    await channel.send(f'{member} join') 

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(741868171618943027)
    await channel.send(f'{member} leave')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'load cmds.{extension} done')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unload cmds.{extension} done')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reload cmds.{extension} done')

for filename in os.listdir('./cmds'):
    if filename.endswith('py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(token)
