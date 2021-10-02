from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def poke(ctx, arg):
    """
    !poke
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


bot.run('ODkxNjE0NDE5OTU4Nzg0MDEz.YVA6ow.LlH0EVj-0jsPZSTdg0_Sz2_7qGM')
