import discord
"""
@client.event
async def on_ready():
    print('Running')
client.run('ODkxNjE0NDE5OTU4Nzg0MDEz.YVA6ow.LlH0EVj-0jsPZSTdg0_Sz2_7qGM')
"""

class TutorialClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 891700351076544573

    async def on_ready(self):
        print('Ready')

    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on a reaction emoji
        """
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name =='🙂':
            role = discord.utils.get(guild.roles, name='Smile Role')
            await payload.member.add_roles(role)
        elif payload.emoji.name =='😎':
            role = discord.utils.get(guild.roles, name='Sunglasses Role')
            await payload.member.add_roles(role)
        elif payload.emoji.name =='👋':
            role = discord.utils.get(guild.roles, name='Wave Role')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on a reaction emoji
        """
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name =='🙂':
            role = discord.utils.get(guild.roles, name='Smile Role')
            await member.remove_roles(role)
        elif payload.emoji.name =='😎':
            role = discord.utils.get(guild.roles, name='Sunglasses Role')
            await member.remove_roles(role)
        elif payload.emoji.name =='👋':
            role = discord.utils.get(guild.roles, name='Wave Role')
            await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True

client = TutorialClient(intents=intents)
client.run('ODkxNjE0NDE5OTU4Nzg0MDEz.YVA6ow.LlH0EVj-0jsPZSTdg0_Sz2_7qGM')

#https://discord.com/channels/891613784953749546/891613785398313010/891700351076544573