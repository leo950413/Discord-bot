import os
import discord
# import interactions
from discord.ext import commands

# Basic setting
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="#",intents=intents)
channel_id = 692690549487960155

# handle start event
@client.event
async def on_ready():
  game = discord.Game('#help')
  print("bot start")
  await client.change_presence(status=discord.Status.online, activity=game)

# handle command error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.channel.send(f"**{ctx.message.content} is not a valid command**")

# import all cog
for filename in os.listdir("./cog"):
  if filename.endswith('.py'):
    client.load_extension(f"cog.{filename[:-3]}")


client.run(os.getenv('TOKEN'))