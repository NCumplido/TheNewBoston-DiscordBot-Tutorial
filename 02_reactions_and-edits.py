import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Running')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'cool':
        await message.add_reaction("\U0001F60E")

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} sent a message\n'
        f'Before content: {before.content}\n'
        f'After content: {after.content}'
    )

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

client.run('ODkxNjE0NDE5OTU4Nzg0MDEz.YVA6ow.LlH0EVj-0jsPZSTdg0_Sz2_7qGM')