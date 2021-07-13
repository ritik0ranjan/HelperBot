import discord, asyncio
from core import HelperBot, Cog
from discord.ext import tasks


class RainbowRole(Cog):
    def __init__(self, bot: HelperBot):
        self.bot = bot
        self.RainbowRole.start()

    @tasks.loop(seconds=60.0)
    async def RainbowRole(self):
        #await asyncio.sleep(5)
        role = discord.utils.get(self.bot.guilds[0].roles, name='RainbowRole')
        if role: 
          await role.edit(colour=discord.Colour.random(),
                          reason="Action featured by !! Ritik Ranjan [*.*]#9230")

def setup(bot):
    bot.add_cog(RainbowRole(bot))