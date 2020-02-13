import discord
from discord.ext import commands
from discord.utils import get
from core.classes import Cog_Extension
import youtube_dl

class React(Cog_Extension):

    @commands.command()
    async def cappuccino(self, ctx):
        await ctx.send('給阿姨一杯卡布奇諾')

    @commands.command()
    async def p(self,ctx):
        channel = ctx.message.author.voice.channel
        #server = ctx.message.guild
        #voice_client = ctx.guild.voice_client
        #print(voice_client)
        voice_client = await channel.connect()
        print(channel)
        #player = await voice_client.create_ytdl_player('https://www.youtube.com/watch?v=WO8mrVjW0-c')
        #voice_client.play(discord.FFmpegPCMAudio('https://www.youtube.com/watch?v=WO8mrVjW0-c'), after=lambda e: print('done', e))
        #voice_client.is_playing()
        
def setup(bot):
    bot.add_cog(React(bot))