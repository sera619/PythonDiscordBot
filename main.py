# -*- coding: utf-8 -*-

import os
import discord
import asyncio
import functools
import itertools
import math
import random
import youtube_dl
import ffmpeg
from async_timeout import timeout
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get as G
from keep_alive import keep_alive as K


role_dic = {"RUDEL":902278661523251210, "WELPE": 902278757723807766}
rolelist = [902278661523251210,902278757723807766]

TOKEN = os.environ['TOKEN']
SERVER_NAME = os.environ['DISCORD_SERVER']

client = discord.Client()

client = Bot(command_prefix="!")

message_hi = "\nHallo @{user}!\nWie gehts dir heute?"


command_message = "\nFolgende Befehle kannst du verwenden:\n- 1: __!hi__ - FoxBot sagt dir 'hallo'.\n - 2: __!commands__ - Zeigt dir eine Liste der Befehle\n - 3: __!music__ - zeigt ein Befehls-Liste für den Musik-Bot.\n\nUm diesese Commmands zu nutzen schreibe folgendes in den Chat:\n__Beispiel:__\n```!hi + [drücke enter]```"
online_users = client.users

"""
Setzt `Playing ` status
await client.change_presence(activity=discord.Game(name="a game"))

Setzt `Streaming ` status
await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

Setzt `Listening ` status
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

Setzt `Watching ` status

await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="a movie"))

"""

# Startup routine 
@client.event
async def on_ready():
  print('Bot ist eingeloggt als: {0.user}'.format(client))
  for guild in client.guilds:
    if guild.name != SERVER_NAME:
      # debugger: print({guild.name})
      break
    # debugger: print([guild.roles])
    
    # ändert Aktivität:
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="A Fox Tale"))
    
    print(
      f'{client.user} ist verbunden mit den folgenden Servern:\n'
      +f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Server Mitglieder:\n - {members}')


# message Reaktionen
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content == "!welpe":
    role = G(message.server.roles, name='Welpe')
    await client.add_roles(message.author, role)

  if message.content.startswith("!hi"):
    await message.channel.send(message_hi.format(user = message.author.name))
    await message.author.create_dm()
    await message.author.dm_channel.send(
      f"Hallo {message.author.name},\n"+
      f"Dies ist eine Testnachricht, Danke!"
    )

  if message.content.startswith("!commands"):
    await message.channel.send(command_message)

# private willkommens Nachricht

@client.event
async def on_member_join(member):
  role = G(member.guilds.roles, name="Welpe")
  await member.add_roles(role)
  await member.create_dm()
  await member.dm_channel.send(
    f"Hallo {member.name}, Willkommen auf dem Discord zum Spiel 'A Fox Tale'!\n"+
    f"--- noch nicht fertig --- =D"
  )






@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='musiclounge')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

K()
client.run(TOKEN)