# -*- coding: utf-8 -*-
import os.path
import os
import discord
from datetime import datetime
from discord.ext import commands
from discord.utils import get as G
from keep_alive import keep_alive as K
from reactionrole import Reaction as RR


role_dic = {"RUDEL": 902278661523251210, "WELPE": 902278757723807766}
rolelist = [902278661523251210, 902278757723807766]

TOKEN = os.environ['TOKEN']
SERVER_NAME = os.environ['DISCORD_SERVER']

client = discord.Client()
message_hi = "\nHallo @{user}!\nWie gehts dir heute?"
command_message = "\nFolgende Befehle kannst du verwenden:\n- 1: __!hi__ - FoxBot sagt dir 'hallo'.\n - 2: __!commands__ - Zeigt dir eine Liste der Befehle\n - 3: __!music__ - zeigt ein Befehls-Liste für den Musik-Bot.\n\nUm diesese Commmands zu nutzen schreibe folgendes in den Chat:\n__Beispiel:__\n```!hi + [drücke enter]```"
online_users = client.users


# startup routine

@client.event
async def on_ready():
    print('Bot ist eingeloggt als: {0.user}'.format(client))
    client.wait_until_ready()
    for guild in client.guilds:
        if guild.name != SERVER_NAME:
            # debugger: print({guild.name})
            break
    # debugger: print([guild.roles])

    print(
        f'{client.user} ist verbunden mit den folgenden Servern:\n'
        f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Server Mitglieder:\n - {members}')


# message Reaktionen
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!welpe'):
        role = G(message.server.roles, name='Welpe')
    await client.add_roles(message.author, role)

    if message.content.startswith("!hi"):
        await message.channel.send(message_hi.format(user=message.author.name))
        await message.author.create_dm()
        await message.author.dm_channel.send(
            f"Hallo {message.author.name},\n" +
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
        f"Hallo {member.name},\nWillkommen auf dem Discord zum Spiel 'A Fox Tale'!\n" +
        f"--- noch nicht fertig --- =D")


RR

K()
client.run(TOKEN)
