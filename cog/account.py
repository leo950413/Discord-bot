from discord.ext import commands
from lib.user_action import *



class Account(commands.Cog,description="Create your account here"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="create your account")
    async def create(self,ctx):
  
        id = ctx.message.author.id
        res = creat_user(str(id))
        await ctx.channel.send(res)

def setup(bot):
    bot.add_cog(Account(bot))