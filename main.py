import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
description = '''The End of the Line LPMUD Discord Bot'''

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    """ Called when discord bot is connected and ready """
    print("Bot connected.")
    guild = bot.get_guild(int(GUILD))
    print(f'{bot.user} has connected to Discord!\n'
          f'{guild.name} (id: {guild.id})')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left+right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(
        f'Welcome, {member.name} to the End of the Line Discord!,\n'
        f'Remember the rules:\n'
        "1) have fun\n2) don't piss someone off bigger than you"
        )
        # show additional commands for the bot, and in-game
#
    pass
    # await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command(name='test_join')
# async def test_join(ctx, member: discord.Member):
async def test_join(ctx):
    joiner = ctx.author
    await ctx.send(
        f'Welcome, {joiner.name}, to the End of the Line Discord!,\n'
        f'Remember the rules:\n'
        "1) have fun\n2) don't piss someone off bigger than you"
        )

@bot.event
async def on_message(message):
    '''
    Called when a member posts a message in a discord channel

    :param message: message object
    '''

    if message.author == bot.user:
        return

    if (message.content[0] == '!'):
        await message.channel.send(
            f'Command given: {message.content[1:]}'
        )
        # do command
        await bot.process_commands(message)
        return

    await message.channel.send(
        f'Message: {message.content}\n'
    )
    print(f"Relayed: {message.content}")

# async def send(*, message):
#     print(f'Message: {message}\n')
#     global target_channel
#     await bot.send_message(target_channel, message)

bot.run(TOKEN)

# get guild stuff
# for guild in client.guilds:
#     if guild.name == GUILD:
#         break


# print(f'Guild: {guild} - {type(guild)} - {type(guild.id)} - {type(GUILD)}')
# guild = discord.utils.find(lambda g: str(g.id) == GUILD, client.guilds)
# guild = discord.utils.get(client.guilds, name=GUILD)