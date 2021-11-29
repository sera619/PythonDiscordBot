import discord
import os
from discord import colour
from discord.utils import get as G
from discord.ext import commands
from discord.embeds import Embed as EM, EmptyEmbed
from keep_alive import keep_alive as K



# spiel versionsnummer
GAME_VERSION = "v0.0.1.0.1"
# discord invit link
INVITE_LINK = os.environ['INVITE_LINK']
# discord token to connect with server
TOKEN = os.environ['TOKEN']
# server name 
SERVER_NAME = os.environ['DISCORD_SERVER']
# reactionrole message id
MES_ID = 914572418650107904
# welcome message
WELCOME_MESSAGE = '\nHallo @{user}!\nWie geht es dir heute?'
# commandlist message
COMMAND_MESSAGE = '\nFolgende Befehle kannst du verwenden:'
# Game logo url
LOGO_URL = "https://github.com/sera619/FOX-TALE-Alpha/blob/master/assets/img/icons/game_logo_colored.png?raw=true"
# homepage url
HOMEPAGE_URL = "https://sera619.github.io/FOX-TALE-Alpha/"
# DM welcome message
DM_MESSAGE = f'\nWillkommen auf dem Discord von "A Fox Tale".\nSchön dich hier zu sehen. Um einen Reibungslosen Umgang zu gewährleisten,'
f'\nakzeptiere bitte die Regeln im #rulez Channel.\nHalte dich an diese Regeln!\n\nSolltest du Fragen oder Probleme haben wende dich bitte an einen Administrator oder an den CEO.'
f'\nDas Team von "A Fox Tale" wünscht dir viel Spaß\nLiebe grüße, __Das Dev-Team__!'





class MyClient(discord.Client):
    # Commando vars
    # initialize Client
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ID der Message der die Rectionrolefunktion hinzugefügt werden soll
        self.role_message_id = MES_ID
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 0,
            discord.PartialEmoji(name='🟡'): 0,
            discord.PartialEmoji(name='Welpe', id=902278757723807766): 0
        }

    async def on_ready(self):
        for guild in self.guilds:
            if guild.name != SERVER_NAME:
                # debugger : print({guild.name})
                break
            print("\n"+
                f'#####################################\n'
                f'#      Bot ist initialisiert:       #\n'
                f'#***********************************#\n'
                f'#   Bot User_ID: {self.user.id}     #\n'
                f'#   Bot User_Name: {self.user}      #\n'
                f'#   Bot Server name: {guild.name}   #\n'
                f'#####################################\n')
            await self.change_presence(status = 'This Bot is created by © S3R43o3',activity=discord.Activity(type=discord.ActivityType.watching, name="S3R43o3"))
    async def on_message(self, message):
        if message.author == self.user:
            return
        # message commands
        if message.content.startswith('!welpe'):
            role = G(message.guild.roles, name="Welpe")
            return await self.add_roles(message.author, role)
        # -> !commands
        if message.content.startswith('!commands'):
            embed = EM(
                title="_Die Befehls-Liste für 'A Fox Tale'- Discord_",
                description = "\n"+
                             f'Eine Liste der Chat-Befehele die du verwenden kannst. \n'
                             f'Gebe hierzu im Chat folgende Befehle ein:\n\n'
                             f'1: ```!hi``` - _FoxBot_ sagt dir "Hallo". \n'
                             f'2: ```!commands``` - _FoxBot_ zeigt dir die ChatBefehl-Liste. \n'
                             f'3: ```!homepage``` - _FoxBot_ erstellt einen Link zur Spiel-Homepage. \n'
                             f'4: ```!invite``` - _FoxBot_ generiert einen Invite-Link für diesen Discord-Server. \n'
                             f'5: ```!status``` - Zeigt den aktuellen Entwicklungs-Status des Spiels.'
            )
            embed.set_author(name = "")
            embed.set_thumbnail(url= LOGO_URL)
            return await message.channel.send(embed=embed)
        
        # -> !hi
        if message.content.startswith('!hi'):
            return await message.reply(WELCOME_MESSAGE.format(user=message.author.name), mention = True)
                
        # -> !homepage
        if message.content.startswith('!homepage'):
            embed = EM(
                title="_Die 'A Fox Tale' Homepage_",
                description = "\n"+
                             f"_Der Link zur offiziellen Homepage von 'A Fox Tale':_ \n"
                             f'Link: *{HOMEPAGE_URL}*'
            )
            embed.set_author(name = "")
            embed.set_thumbnail(url = LOGO_URL)
            
            return await message.reply(embed = embed)
        
        # -> !invite
        if message.content.startswith('!invite'):
            embed = EM(
                title = '_"A Fox Tale" - Discord-Einladungslink_',
                description = "\n"+
                            f"_Der gewünschte Einladungslink:_ \n"
                            f'{INVITE_LINK}'
            )
        
        # -> !status
        if message.content.startswith('!status'):
            embed = EM(
                title = '_"A Fox Tale" - Entwicklungsstatus_',
                description = "\n"+
                        f'Aktuell befinden wir uns in der internen Alpha-Testphase. \n'
                        f'Derzeitige Version: _{GAME_VERSION}_\n\n'
                        f'Eine erste spielbare Demo wird spätestens ab dem _31.12.2021_ verfügbar sein.'
                        f'Alle weiteren Informationen zum Spiel findest du unter:\n'
                        f'*{HOMEPAGE_URL}*'
            )   
    
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Willkommen {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
        dm_text = DM_MESSAGE
        return await member.create_dm(message = dm_text)
    
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        '''vergibt eine Rolle anhand des emoji'''
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # wenn das emoji nicht eines von der liste ist -> exit
            return

        role = guild.get_role(role_id)
        if role is None:
            # geht sicher das rolle existiert und valide ist
            return

        try:
            await payload.member.add_roles(role)
        except discord.HTTPException:
            pass

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        '''Entfernt die Rolle anhand des Emoji´s'''
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        role = guild.get_role(role_id)
        if role is None:
            return

        # payload für on_raw_reaction_remove enthält 'member' nicht
        # generiere über 'user_id'
        member = guild.get_member(payload.user_id)
        if member is None:
            return

        try:
            await member.remove_roles(role)
        except discord.HTTPException:
            pass

    

intents = discord.Intents.default()
intents.members = True
K()
client = MyClient()
client.run(TOKEN)