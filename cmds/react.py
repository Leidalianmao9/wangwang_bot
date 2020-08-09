import discord
from discord.ext import commands
from core.classes  import Cog_Extension
import json

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)
    pic = jdata['PIC_PATH']

class React(Cog_Extension):
    @commands.command()
    async def pic(self, ctx):
        picture = discord.File(jdata['PIC_PATH'])
        await ctx.send(file = picture)


def setup(bot):
    bot.add_cog(React(bot))