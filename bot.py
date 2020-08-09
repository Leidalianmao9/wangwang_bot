import discord
from discord.ext import commands

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

bot.run('NzQxODE4NDgxNTM5ODA5MzMx.Xy9GTA.wc140Z4QPRl36wwfIGHqP-1O9CI')
