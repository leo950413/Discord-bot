from discord.ext import commands
from lib.user_action import *

channel_id = 692690549487960155

class Clear(commands.Cog,description="Clean some trash message."):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def clear(ctx,*arg1):
        if(isinstance(arg1[0],int)):

            await ctx.channel.send('**Invalid number**')
        else:
            
            await ctx.channel.purge(limit=int(arg1[0])) 
def setup(bot):

    bot.add_cog(Clear(bot))