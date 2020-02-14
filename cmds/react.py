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
        #channel = ctx.message.author.voice.channel
        #server = ctx.message.guild
        #voice_client = ctx.guild.voice_client
        #print(voice_client)
        voice_client = await channel.connect()
        player = voice_client.create_ffmpeg_player('input.mp3',, after=lambda: print('done'))
        player.start()        
                
        
def setup(bot):
    bot.add_cog(React(bot))