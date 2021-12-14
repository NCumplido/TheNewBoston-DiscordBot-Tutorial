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

client.run('Remove Key')
