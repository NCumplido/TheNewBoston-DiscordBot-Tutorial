import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is online and ready')

greetings_array = ['Hello', 'hello', 'Hi', 'hi', 'Yo', 'yo', 'Hey', 'hey']
jack_array = ['Jack Sparrow', 'Jack sparrow', 'jack sparrow', 'jack Sparrow']

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    message_content = message.content

    if message_content in greetings_array:
        await message.channel.send('Welcome!')

    elif message_content in jack_array:
        str_captain = 'Captain'
        await message.channel.send(f'{str_captain} {message_content}')

client.run('KEY')
