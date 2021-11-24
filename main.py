import os
import discord

TOKEN = os.environ['TOKEN']
SERVER_NAME = os.environ['DISCORD_SERVER']

client = discord.Client()
message_hi = "\nHallo @{user}!\nWie gehts dir heute?"
command_message = "\nFolgende Befehle kannst du verwenden: \n1: !hi - FoxBot sagt dir 'hallo'.\n2: !commands - Zeigt dir list der Befehle"

@client.event
async def on_ready():
  print('Bot ist eingeloggt als: {0.user}'.format(client))
  for guild in client.guilds:
    if guild.name != SERVER_NAME:
      # debugger: print({guild.name})
      break

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
  
  if message.content.startswith("!hi"):
    await message.channel.send(message_hi.format(user = message.author.name))
    await message.author.create_dm()
    await message.author.dm_channel.send(
      f"Hallo {message.author},\n"+
      f"Dies ist eine Testnachricht, Danke!"
    )

  if message.content.startswith("!commands"):
    await message.channel.send(command_message)

# private willkommens Nachricht

@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
    f"Hallo {member.name}, Willkommen auf dem Discord zum Spiel 'A Fox Tale'!\n"+
    f""
  )

client.run(TOKEN)