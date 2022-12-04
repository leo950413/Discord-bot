import discord
from discord.ext import commands
from operator import itemgetter
from lib.db import *
from lib.user_action import score as sc



class Search(commands.Cog,description="Get your score."):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def score(self,ctx):
            score_board = test()
            score_board = sorted(score_board,key=itemgetter(1),reverse=True)
            index = 0
            for r in score_board:
      
                r = list(r)
                user = self.bot.get_user(int(score_board[index][0]))
                if user is None :
                    r.append("Unknown User")
                else:
                    r.append(user)
        
                score_board[index] = r
                index += 1
            names = ''
            for index in range(len(score_board)):

                if type(score_board[index][3]) is str:
                    names += f'{index+1}#<{score_board[index][3]}> -with {score_board[index][1]}\n'
                else:

                    names += f'{index+1}#<{score_board[index][3].mention}> -with {score_board[index][1]}\n'
            embed = discord.Embed(title="Leaderboard")
            embed.add_field(name="Names", value=names, inline=False)
            embed.set_footer(text=f"{sc(str(ctx.message.author.id))}")
            await ctx.channel.send(embed=embed)

    
def setup(bot):

    bot.add_cog(Search(bot))