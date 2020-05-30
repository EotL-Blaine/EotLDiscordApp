import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from discord_stuff import discord_who
from mud_stuff import mud_who
from mud_stuff import test_list

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
    """Tester function, syntax:  !add x y"""
    await ctx.send(left+right)

@bot.command(name='who')
async def who(ctx, *args):
    """
    Get list of who is on the MUD

    :param ctx:
    :param args: string (optional) args,
        syntax: /guild
    """
    # just using the discord who for the time being
    members = discord_who.get_discord_who(ctx.guild)
    await ctx.send(f'Members: \n{members}')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
    await ctx.send(
        f'Welcome, {member.name} to the End of the Line Discord!,\n\n'
        f'Remember the rules:\n'
        "1) have fun\n2) don't piss someone off bigger than you"
        )
        # show additional commands for the bot, and in-game

@bot.command(name='test_join')
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

    if (message.content == "!who"):
        # relay who command to telnet
        j_list= test_list.test_list_json
        who = mud_who.default_who(j_list)
        x = "\n".join(who)
        await message.channel.send(x)
        return

    if (message.content[0] == '!'):
        await message.channel.send(
            f'Command given: {message.content[1:]}'
        )
        # do command
        await bot.process_commands(message)
        return

    # put code here to relay it to mud
    await message.channel.send(f"```py\n@Relay: {message.content}\n```")
    print(f"Relayed: {message.content}")

# async def send(ctx, *, message) should be correct syntax
# async def send(*, message):
#     print(f'Message: {message}\n')
#     global target_channel
#     await bot.send_message(target_channel, message)

bot.run(TOKEN)

# COLOR STUFF
# f"```\n**Blaine** {message.content}\n```"
# f"```cs\n<Butkus> and then some!\n```"
# f"```diff\n-<InRed> and on and on again!\n```"
# f"```CSS\n**<InYellow>** whatever you say, hoss```"
# f"```cs\n'**<dunno>** asdfadsddfa'\n```"
# f"```= Blue =\n**<dunno>** asdfadsddfa\n```"
# f"```asciidoc\n<asciidoc>**<dunno>** asdfadsddfa\n```"
# f"```---\n**<dunno>** asdfadsddfa\n```"
# "```xml\n<Blue first then Yellow = OneGreenWord after equals sign>```"
# f"```CSS\n{jan:6} {n1:13} (Etc) (3m)```"
# f"```py\n@{jan:6} {n2:13} (Etc) (15m)```"
# f"```md\n> {jan:6} {n3:13} (Whatever) (>1hr)```"

# get guild stuff
# for guild in client.guilds:
#     if guild.name == GUILD:
#         break


# print(f'Guild: {guild} - {type(guild)} - {type(guild.id)} - {type(GUILD)}')
# guild = discord.utils.find(lambda g: str(g.id) == GUILD, client.guilds)
# guild = discord.utils.get(client.guilds, name=GUILD)