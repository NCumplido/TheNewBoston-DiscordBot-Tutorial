import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is online and ready')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    #TODO Use collection for initial greeting
    if message.content == 'Hello' or 'hello' or 'hi' or 'Hi' or 'hi':
        await message.channel.send('Welcome!')

client.run('Remove Key')
