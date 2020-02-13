import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def join(self,ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def ping(self,ctx):
        await ctx.send('suck')

    @commands.command()
    async def hi(self,ctx):
        await ctx.send('滾')

def setup(bot):
    bot.add_cog(Main(bot))