import discord
import os
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
  print('FALLBACK READY.')

@bot.command()
async def start(ctx):
  if ctx.author.id == 273845229130481665:
    os.system('python3 ctx.py & python3 main.py')

bot.run(os.getenv('fessortoken'))