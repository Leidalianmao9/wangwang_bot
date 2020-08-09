import discord
from discord.ext import commands
import json


with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)
    token = jdata['TOKEN']
    welcome_channel = jdata['WELCOME']
    leave_channel = jdata['LEAVE']
    pic = jdata['PIC_PATH']


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
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def hi(ctx):
    await ctx.send('hello '+ str(ctx.author) + ". Hope you make a lot of money today!")

@bot.command()
async def pic(ctx):
    picture = discord.File(jdata['PIC_PATH'])
    await ctx.send(file = picture)


bot.run(token)
