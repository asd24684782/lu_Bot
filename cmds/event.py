import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json



with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):



    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(jdata['GENERAL'])
        await channel.send(f'給{member} 一杯卡布奇諾!')
        print(f'給{member} 一杯卡布奇諾!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(jdata['GENERAL'])
        await channel.send(f'{member} 給人秒了')
        print(f'{member} 給人秒了')
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == '卡布奇諾':
            await msg.channel.send(f'給{msg.author.nick}一杯卡布奇諾')
        elif msg.content == '炸他':
            await msg.channel.send('漂亮')
        elif msg.content == '反手一個K':
            await msg.channel.send('埋伏他一手')

def setup(bot):
    bot.add_cog(Event(bot))