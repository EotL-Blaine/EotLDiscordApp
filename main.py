import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from discord_stuff import discord_who

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
    Get list of who is on the game
    Default list, color eval i guess
        [Jan]  Cozminsky (5m)
        [Frob] Blaine
        [350]  Torr      (60m)
    Alternate list by guild:
        Etc
        [Jan]  Cozminsky
        Red Disciple
        [174]  Butkus
        Fighter
        [5]    Lilguy
        - Swordsman
        [132]  Liveblade

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

    if (message.content[0] == '!'):
        await message.channel.send(
            f'Command given: {message.content[1:]}'
        )
        # do command
        await bot.process_commands(message)
        return

    jan =  "[Jan ]"
    arch = "[Arch]"
    play = "278"
    n1 = "Cozminksy"
    n2 = "Arphen"
    n3 = "Torralt"

    who_list = ([
        f'{"[Jan ]":^6} {n1:13} : Etc (3m)',
        f'{"[Arch]":^6} {n2:13} : Capacitor (15m)',
        f'{"[Frob]":^6} {"Blaine":13} : Cleric (15m)',
        f'{"235":^6} {"Torr_alt":13} : Headhunter (>1hr)',
        f'{"117":^6} {"Dude":13} : Bodyguard (15m)',
        f'{"95":^6} {"Ratchet":13} : Berserker (9m)',
        f'{"9":^6} {"Gorda":13} : None (>1hr)',
    ])

    # who_list[0] =  f"```md\n# {who_list[0]}```"
    # who_list[1] =  f"```py\n@ {who_list[1]}```"
    # who_list[2] =  f"```py\n@ {who_list[2]}```"
    # who_list[3] =  f"```md\n> {who_list[3]}```"
    # who_list[4] =  f"```md\n# {who_list[4]}```"
    # who_list[5] =  f"```md\n# {who_list[5]}```"
    # who_list[6] =  f"```md\n> {who_list[6]}```"

    # who_list[0] =  f"md\n# {who_list[0]}"
    # who_list[1] =  f"py\n@ {who_list[1]}"
    # who_list[2] =  f"py\n@ {who_list[2]}"
    # who_list[3] =  f"md\n> {who_list[3]}"
    # who_list[4] =  f"md\n# {who_list[4]}"
    # who_list[5] =  f"md\n# {who_list[5]}"
    # who_list[6] =  f"md\n> {who_list[6]}"

    who_list[0] =  f"# {who_list[0]}"
    who_list[1] =  f"- {who_list[1]}"
    who_list[2] =  f"- {who_list[2]}"
    who_list[3] =  f"> {who_list[3]}"
    who_list[4] =  f"# {who_list[4]}"
    who_list[5] =  f"# {who_list[5]}"
    who_list[6] =  f"> {who_list[6]}"

    x = f"```md\n{'==============[ EotL - Who ]==============':^40}\n\n"
    for w in who_list:
        x += w + "\n"
    x += "```"

    p1 = f'{jan:^6} {n1:13} : Etc (3m)'
    p2 = f'{arch:^6} {n2:13} : Capacitor (15m)'
    p3 = f'{play:^6} {n3:13} : Headhunter (>1hr)'

    await message.channel.send( x )
    #
    #     f"```md\n# {p1}```"
    #     f"```py\n@ {p2}```"
    #     f"```md\n> {p3}```"
    #
    # )
        
    '''
        [Jan]  Cozminsky    (Pacifist)
        [Arch] Arphen       (Capacitor)
        [Gue]  Randoguest   (Hobo)
        [258]  Torralt      (Red disciple)
        [158]  Multiped     (Berzerker)
    '''

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