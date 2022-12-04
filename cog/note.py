from discord.ext import commands
from lib.user_action import *
import os

class Note(commands.Cog,description="Save your text or link."):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def note(self,ctx,*arg1):
        id = ctx.message.author.id
    
        file = open(f"./cog/note/{str(id)}","a+")
        file.write(arg1[0]+"\n")
        file.close()
        
        await ctx.channel.send("Write succesfully")

    @commands.command()
    async def read(self,ctx):
        id = ctx.message.author.id
        if os.path.exists(f"./cog/note/{str(id)}"):

            dt = open(f"./cog/note/{str(id)}","r").read().splitlines()
            await ctx.channel.send("\n".join(dt))
        
        else:

            await ctx.channel.send("You must write something before read it")            

            
            
def setup(bot):
    bot.add_cog(Note(bot))