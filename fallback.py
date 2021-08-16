import discord
import os
from discord.ext import commands
import sys
import configparser

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
  print('FALLBACK READY.')

@bot.command()
async def start(ctx):
  if ctx.author.id == 273845229130481665:
    await ctx.send(embed=discord.Embed(title='Starting bot...', description='', color=0xFFFFFF))
    os.system('python3 ctx.py &')
    sys.exit(0)

#this command is deprecated, use /update instead
@bot.command()
async def update(ctx):
  if ctx.author.id == 273845229130481665:
    await ctx.send(embed=discord.Embed(title='Updating bot...', description='', color=0xFF0000))
    os.system('git pull')

@bot.command()
async def ping(ctx):
  print('fallback pinged')
  await ctx.send('pong!')

config = configparser.ConfigParser()
config.read('cred.ini')
bot.run(config['config']['fessortoken'])
