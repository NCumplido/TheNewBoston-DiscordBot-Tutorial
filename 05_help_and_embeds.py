import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description='Welcome to the channel, this help section lists all of the commands for this channel',
        color=discord.Colour.greyple()
    )
    embed.set_thumbnail(url='https://images4.alphacoders.com/188/188384.jpg')
    embed.add_field(
        name='!help',
        value='List all of the commands',
        inline=False
    )
    embed.add_field(
        name='!poke',
        value='Poke someone',
        inline=True
    )
    embed.add_field(
        name='!double_poke',
        value='Poke two people',
        inline=True
    )
    embed.add_field(
        name='!greet',
        value='Greet multiple people',
        inline=True
    )

    await ctx.send(embed=embed)

@bot.command()
async def poke(ctx, arg):
    """
    !Poke someone
    """
    await ctx.send(f'Poked {arg}')

@bot.command()
async def info(ctx):
    """
    ctx - context (information about how the command was executed)
    !info
    """
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.command()
async def double_poke(ctx, arg1, arg2):
    """
    !double_ poke John Jane
    """
    await ctx.send(f'Double poked {arg1} and {arg2}')

@bot.command()
async def greet(ctx, *args):
    """
    !greet John Jane Fred Kristy Mike Holly
    """

    everyone = ', '.join(args)

    await ctx.send(f'Greeted {everyone}')


bot.run('Remove Key')
