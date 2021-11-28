import os
import discord
from discord.ext import commands

TOKEN = os.environ['TOKEN']
bot = commands.Bot(command_prefix='.')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
bot.run(TOKEN)