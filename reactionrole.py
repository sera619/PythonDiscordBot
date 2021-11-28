import discord


mes_id = 914572418650107904


class Reaction(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ID der Message der die Rectionrolefunktion hinzugefügt werden soll
        self.role_message_id = mes_id
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 0,
            discord.PartialEmoji(name='🟡'): 0,
            discord.PartialEmoji(name='green', id=1): 0
        }

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

client = Reaction(intents=intents)
