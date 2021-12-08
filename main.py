import discord
import os
import time
from discord import colour
from discord.enums import Status
from discord.utils import get as G
from discord.ext import commands
from discord.embeds import Embed as EM
from datetime import datetime
import keep_alive

E_MESSAGE = "\nDu gehörst nicht zum  __Development-Team__ \n__Netter Versuch!__ :smile:"
SYSTEM_CHANNEL = 902288786250166283
RULEZ_CHANNEL = 902436882904920074
POST_CHANNEL = ""

BOT_VERSION = "v1.9"
# -> Member ID´s
SAMU_ID = os.environ['SAMU_ID']
CEO_ID = os.environ['CEO_ID']
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
DM_MESSAGE =f'\nWillkommen auf dem Discord von "A Fox Tale".\nSchön dich hier zu sehen. Um einen Reibungslosen Umgang zu gewährleisten,'
f'\nakzeptiere bitte die Regeln im #rulez Channel.\nHalte dich an diese Regeln!\n\nSolltest du Fragen oder Probleme haben wende dich bitte an einen Administrator oder an den CEO.'
f'\nDas Team von "A Fox Tale" wünscht dir viel Spaß\nLiebe grüße, __Das Dev-Team__!'

RULE_EMBED = EM(
    title="_'A Fox Tale'- DISCORD-REGELN_",
    description='_Hallo schön dich hier zu sehen!Um ein friedliches Miteinander zu gewährleisten akzeptiere bitte folgende Regeln._\n\n'
    f'___Bei Verstoß dieser Regeln ist mit einem temporären Ban bis zum völligen Ausschluss alles möglich!___\n\n'
    f'1. Ein freundlicher und respektvoller Umgang ist jederzeit Pflicht!\n\n'
    f'2. Rassismus, Hatespeech, Sexsismus oder andere Abarten werden ohne Ankündigung und ohne Chance auf wideruf gebannt.\n\n'
    f'2. Den Anweisungen von Administratoren (CeO-> Administrator-> Moderator) ist stets Folge zu leisten. \n\n'
    f'3. Fremdwerbung ist ist verboten. \n\n'
    f'4. Das grundlose taggen / pingen / markieren von Nutzern & Benutzerrängen ist untersagt. \n\n'
    f'5. Keine unpassenden Profile (Nutzernamen, Avatare, Accounts und Status). Dazu zählen unter Anderem leere Nutzenamen, ungewöhnliche Unicode Zeichen oder übermäßig lange Nutzernamen. \n\n'
    f'6. Das Teilen von personenbezogenen Daten ist verboten. \n\n'
    f'7. NSFW-Inhalte (pornografie etc.) sind in allen Channeln verboten. \n\n'
    f'8. Spammen ist verboten. \n\n'
    f'9. Trolling ist verboten. \n\n'
    f'10. Halte dich an die Channel Themen und halte Konversationen in den passenden Channeln. \n\n'
    f'11. Administratoren haben das letzte Wort. \n\n'
    f'12. Der CEO das allerletzte!')



class MyClient(discord.Client):
    maintain_mode: bool
    debugging:bool
    guild_name = ""
    channel = ""
    rule_embed = RULE_EMBED
    rulez_channel = ""
    # Commando vars
    # initialize Client
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.debugging = True
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
            print("\n" + f'#####################################\n'
                  f'#      Bot ist initialisiert:       #\n'
                  f'#***********************************#\n'
                  f'#   Bot User_ID: {self.user.id}     #\n'
                  f'#   Bot User_Name: {self.user}      #\n'
                  f'#   Bot Server name: {guild.name}   #\n'
                  f'#####################################\n')
            keep_alive.name_server = guild.name
            self.guild_name = guild.name
            keep_alive.id_server = str(guild.id)
            keep_alive.id_bot = str(self.user.id)
            keep_alive.name_bot = str(self.user)
            keep_alive.bot_status = "Online / "+str(self.activity)             
            keep_alive.bot_version = str(BOT_VERSION)
            keep_alive.keep_alive()
            self.channel = guild.get_channel(int(SYSTEM_CHANNEL))
            rulez_channel = guild.get_channel(int(RULEZ_CHANNEL))

            # REGEL POST


            # Debugging Mode Message
            if self.debugging == True:
                await self.change_presence(
                            activity=discord.Activity(
                            type=discord.ActivityType.competing,
                            name="der Werkstatt",
                            status=discord.Status.idle))
                await self.channel.send(
                f'\n:head_bandage:\n'
                f'\n... __DEBUG-MODUS__ ...\n'
                f'\n... :pray: SORRY FÜR DEN SPAM :pray: ...\n'
                )

            # Normal Welcome Message
            else:
                await self.channel.send("\nBootsequenz wurde initialisiert...\n... Starte Systeme...")
                time.sleep(5)
                await self.change_presence(status=True,
                                        activity=discord.Activity(
                                            type=discord.ActivityType.listening,
                                            name="!commands"))
                embed = EM(
                    title="DUDEBOT",
                    description="\n"
                    f'DUDEBOT wurde __von__:\n\n _S3R43o3_ \n\n'
                    f':watch: _'+str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+'\n\n_ gestartet! \n\n'
                    f'Keine Auffälligkeiten im System erkannt.\n'
                    f':christmas_tree: :santa: HoHoHo Ich glaub das Weihnachtet bald. :santa: :christmas_tree:'
                )
                embed.set_author(name="")
                embed.set_thumbnail(url=LOGO_URL)
                return await self.channel.send(embed=embed)

    async def post_embed():
        if keep_alive.new_embed:
            post_embed = EM(
                title = 'embed post test',
                description= 'embed post test text if u read this text to the end u didnt understand what exactly test text mean =D'
            )
            return await POST_CHANNEL.send(embed=post_embed)
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        # message role change
        if message.content.startswith('!welpe'):
            role = G(message.guild.roles, name="Welpe")
            return await message.author.add_roles(message.author, role)
        # -> !commands
        if message.content.startswith('!commands'):
            embed = EM(
                title="_Die Befehls-Liste für 'A Fox Tale'- Discord_",
                description="\n" +
                f'Eine Liste der Chat-Befehle die du verwenden kannst. \n'
                f'Gebe hierzu im Chat folgende Befehle ein:\n\n'
                f'1: ```!hi``` - _FoxBot_ sagt dir "Hallo". \n'
                f'2: ```!commands``` - _FoxBot_ zeigt dir die ChatBefehl-Liste. \n'
                f'3: ```!homepage``` - _FoxBot_ erstellt einen Link zur Spiel-Homepage. \n'
                f'4: ```!invite``` - _FoxBot_ generiert einen Invite-Link für diesen Discord-Server. \n'
                f'5: ```!status``` - Zeigt den aktuellen Entwicklungs-Status des Spiels. \n'
                f'6: ```!musik```  - _FoxBot_ zeigt dir die Befehlsliste für den Musik-Bot. \n'
                f'7: ```!emoji``` - _FoxBot_ zeigt dir eine Liste mit den Custom-Emojis vom Server. \n'
            )
            embed.set_author(name="")
            embed.set_thumbnail(url=LOGO_URL)
            return await message.reply(embed=embed)

        # -> !hi
        if message.content.startswith('!hi'):
            return await message.reply(
                WELCOME_MESSAGE.format(user=message.author.name))

        # -> !homepage
        if message.content.startswith('!homepage'):
            embed = EM(
                title="_Die 'A Fox Tale' Homepage_",
                description="\n" +
                f"_Der Link zur offiziellen Homepage von 'A Fox Tale':_ \n"
                f'Link: *{HOMEPAGE_URL}*')
            embed.set_author(name="")
            embed.set_thumbnail(url=LOGO_URL)

            return await message.reply(embed=embed)

        # -> !invite
        if message.content.startswith('!invite'):
            embed = EM(title='_"A Fox Tale" - Discord-Einladungslink_',
                       description="\n" +
                       f"_Der gewünschte Einladungslink:_ \n"
                       f'{INVITE_LINK}')
            embed.set_author(name="")
            embed.set_thumbnail(url=LOGO_URL)

            return await message.reply(embed=embed)

        # -> emojis
        if message.content.startswith('!emoji'):
            embed = EM(
                title="_'A Fox Tale' - Emoji-Liste_",
                description="\n" +
                f'Um die Custom-Emojis zu verwenden nutze folgende Codes: \n\n'
                f'```:fox_red:``` - coloriertes GameLogo \n'
                f'```:fox_white:``` - weißes GameLogo \n')
            embed.set_author(name="")
            embed.set_thumbnail(url=LOGO_URL)
            return await message.reply(embed=embed)

        # -> !status
        if message.content.startswith('!status'):
            embed = EM(
                title='_"A Fox Tale" - Entwicklungsstatus_',
                description="\n" +
                f'Aktuell befinden wir uns in der internen Alpha-Testphase. \n'
                f'Derzeitige Version: \n\n'
                f'__{GAME_VERSION}__ \n\n'
                f'Eine erste spielbare Demo wird spätestens ab dem: \n\n'
                f'__31.12.2021__ \n\n'
                f'verfügbar sein. \n'
                f'Alle weiteren Informationen zum Spiel findest du unter:\n'
                f'*{HOMEPAGE_URL}*')
            embed.set_author(name="")
            embed.set_thumbnail(url=LOGO_URL)

            return await message.reply(embed=embed)
        # -> !musik
        if message.content.startswith('!musik'):
            embed = EM(
                title='_Die Musik-Bot Befehls-Liste_',
                description="\n" + f'Alle Musik-Bot Befehle. \n'
                f'Bitte beachte die folgenden Befehle nur im #musicspam Kanal zu verwenden. \n'
                f'Vorsätzliche wiederholte Missachtung führt zu Konsequenzen. \n'
                f'Beispiel: ```#play https://www.youtube.com/watch?v=Q0wbyQRRQJA``` \n\n'
                f'```#play``` - Fügt einen Song zur Warteschlange hinzu und spielt ihn ab. \n'
                f'```#search``` - Durchsucht YouTube nach Ergebnissen zum Abspielen. \n'
                f'```#queue``` - Zeigt die Warteschlange der aktuellen Songs in der Wiedergabeliste an. \n'
                f'```#stop```- Stoppt den aktuellen Song und löscht die gesamte Musik-Wiedergabeliste. \n'
                f'```#vol```- Ändert/Zeigt die aktuelle Lautstärke an. \n'
                f'```#pause```- Pausiert den aktuell wiedergegebenen Track. \n'
                f'```#np```- Zeigt an, welchen Song der Bot gerade spielt. \n'
                f'```#skip```- Überspringt den aktuellen Song. \n'
                f'```#repeat```- Schaltet den Wiederholmodus ein/aus. \n'
                f'```#seek```- Sucht einen bestimmten Punkt in der aktuellen Spur. \n'
                f'```#24/7```- Schaltet den 24/7-Modus ein/aus, so dass der Bot den Sprachkanal nicht verlässt, bis du ihn stoppst. \n'
            )
            embed.set_author(name="")
            embed.set_thumbnail(url=LOGO_URL)

            return await message.reply(embed=embed)
        # -> admin commands
        # -> stream state
        if message.content.startswith('!state.stream'):
            if message.author.id == int(CEO_ID):
                await message.reply("Status wurde auf: 'Streaming' geändert.")
                return await self.change_presence(
                    status=True,
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, name="!commands"))
            else:
                return await message.reply(
                    "\nDu gehörst nicht zum :fox_red: __Development-Team__ .\nNetter _Versuch!_ :smile:"
                )
        # -> Maintain-Mode
        if message.content.startswith('!state.maintain'):
            print(message.author.id)
            if message.author.id == int(CEO_ID):
                if self.maintain_mode == False:
                    self.maintain_mode = True
                    await message.reply(
                        "\nSystem-Wartung wird initialisiert...\nSysteme werden heruntergefahren."
                    )
                    await self.change_presence(
                        status=discord.Status.do_not_disturb,
                        activity=discord.Activity(
                            type=discord.ActivityType.competing,
                            name="der Werkstatt"))
                    return await message.reply(
                        "\nSystem-Wartung vollständig initialisiert.")
                else:
                    return await message.reply(
                        "\n... ich befinde mich bereits im Wartungsmodus ...")
            else:
                return await message.reply(E_MESSAGE)
        # -> stop maintainmode
        if message.content.startswith('!state.return'):
            if message.author.id == int(CEO_ID):
                if self.maintain_mode == True:
                    self.maintain_mode = False
                    await message.reply(
                        "\n... System-Wartung abgeschlossen.\nSysteme werden reaktiviert."
                    )
                    await self.change_presence(
                        status=discord.Status.online,
                        activity=discord.Activity(
                            type=discord.ActivityType.playing,
                            name="!commands"))
                    return await message.reply(
                        "\nAlle Systeme bereit.\nDanke für das Update")
                else:
                    return await message.reply(
                        "\nDazu müsste ich ersteinmal weg sein.")
            else:
                return await message.reply(E_MESSAGE)
        # -> Todos
        if message.content.startswith('!todo.audio'):
            if message.author.id == int(SAMU_ID) or int(CEO_ID):
                embed = EM(
                    title="_Audio TODO-Liste:_",
                    description="\n" +
                    f'Track für den Wald bzw. Feldebene - [ ] \n'
                    f'Combat Track: DK C3 boss blues quest abgeschlossen - [ ]\n'
                    f'menü selection sound; button klicks - [ ] \n'
                    f'error - [ ] \n'
                    f'"textschreiben" letterprintsound - [ ] \n'
                    f'höhlen track - [ ] \n'
                    f'verließ sound - [x] \n'
                    f'sound zum reisen/fliegen/reiten: Secret of Mana OST Prophecy - [ ]\n'
                )
                embed.set_author(name="")
                embed.set_thumbnail(url=LOGO_URL)
                return await message.reply(embed=embed)
            else:
                return await message.reply(E_MESSAGE)

    async def on_member_join(self, member):
        guild = member.guild
        if self.channel is not None:
            to_send = 'Willkommen {0.mention} to {1.name}!'.format(
                member, guild)
            await self.channel.send(to_send)
        dm_text = DM_MESSAGE
        return await member.create_dm(message=dm_text)

    async def on_reaction_add(self, reaction, user):
        welpe = discord.utils.get(user.guild.roles, name="Welpe")
        rudel = discord.utils.get(user.guild.roles, name="Rudel")
        if str(reaction.emoji) == ":white_check_mark:":
                return await user.add_roles(welpe)
        elif str(reaction.emoji) == ":x:":
                return await user.add_roles(rudel)
        
        
client = MyClient()

intents = discord.Intents.default()
intents.members = True
print(intents)
client.run(TOKEN)
    
    
