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

client.run('ODkxNjE0NDE5OTU4Nzg0MDEz.YVA6ow.LlH0EVj-0jsPZSTdg0_Sz2_7qGM')