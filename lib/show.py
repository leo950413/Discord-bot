import discord
from discord import embeds
import mysql.connector


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="g52hS9C8C6aT",
  database="challenge"
)


def show(id:int)->embeds:
    """show function

    Args:
        id (int): The index of the challenge

    Returns:
        embeds: A discord embed with challenge info
    """
    try:   
         
        
        mycursor = db.cursor()
        mycursor.execute(f"SELECT * FROM info WHERE `id`={id}")
        res= mycursor.fetchall()[0]
        
        
        embed=discord.Embed(title=res[5], description=res[1],url=res[4],color=0x781717)
        embed.set_author(name=f"Author: {res[7]}")
        embed.add_field(name="Difficulty", value=res[6], inline=True)
        embed.add_field(name="Category ", value=res[0], inline=True)
        embed.add_field(name="Score", value=res[3], inline=True)
        embed.add_field(name="Attachment", value=res[4], inline=True)
        embed.add_field(name="Id", value=id, inline=True)
        return embed
    
    except IndexError:

        return False
