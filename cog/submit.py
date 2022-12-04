from discord.ext import commands
from lib.user_action import *
import discord

channel_id = 692690549487960155

class Submit(commands.Cog,description="Submit your flag here"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def submit(self,ctx,*arg):

        if not(isinstance(ctx.channel, discord.channel.DMChannel)):
            
            await ctx.reply("Only submit your flag through PM")
            await ctx.message.delete()
        else:
            user = ctx.message.author
            id = user.id
            status,res = flag_validate(arg[0],str(id))
            
            if (not(status)):

                await ctx.reply(res,mention_author=True)
                
            else:

                await ctx.reply(res,mention_author=True)
                await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')


def setup(bot):
    bot.add_cog(Submit(bot))