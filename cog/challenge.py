from discord.ext import commands
from lib.show import show as sh
from lib.operate_docker import *

class Challenge(commands.Cog,description="Start some challenge instance and Check for challenge info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def challenge(self,ctx):
  
        await ctx.channel.send("#challenge show {id}")
    
    @challenge.command(brief="Show the challenge info")
    async def show(self,ctx,*arg):
        
        try:
            index = int(arg[0])
        
        except  ValueError:

            await ctx.channel.send("Invalid number")
            return 
        
        res = sh(index)
        

        if(res):
            await ctx.channel.send(embed=res) 

        else:
            await ctx.channel.send("This challenge not exits") 

    @challenge.command(brief="Start your instance")
    async def start(self,ctx,*arg):
        
        id = ctx.message.author.id

        if(isinstance(arg[0],int) or id==0):

            await ctx.channel.send("Not an valid challenge id")

        res = create(str(id),int(arg[0]))
  
        await ctx.channel.send(res)         

    @challenge.command()
    async def delete(self,ctx):

        id = ctx.message.author.id
        res = delete(str(id))

        await ctx.channel.send(res)


def setup(bot):
    
    bot.add_cog(Challenge(bot))