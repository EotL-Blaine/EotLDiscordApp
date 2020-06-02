import asyncio
import os
import threading

import discord
from dotenv import load_dotenv
from discord.ext import commands

from connect import Connect

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
desc = '''The End of the Line LPMUD Discord Bot'''
bot = commands.Bot(command_prefix='!', description=desc)

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
    # members = discord_who.get_discord_who(ctx.guild)
    # await ctx.send(f'Members: \n{members}')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""

    # await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
    await ctx.send(
        f'Welcome, {member.name} to the End of the Line Discord!,\n\n'
        f'Remember the rules:\n'
        "1) have fun\n"
        "2) don't piss someone off bigger than you"
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
        # j_list= test_list.test_list_json
        # who = bot.who(j_list)
        # x = "\n".join(who)
        # await message.channel.send(x)
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

class Start:
    '''

    '''
    def __init__(self):
        self.bot = None
        self.mud = None
        pass

    async def send_auto_who(self, chan, who):
        await chan.send(who)

    def auto_who(self, info):
        from mud_stuff.who import default_who
        print("MASTER auto_who()")
        who = default_who(info)
        chan = bot.get_channel(716783560861941770)

        # Send async
        loop = asyncio.get_event_loop()
        loop.create_task(self.send_auto_who(chan, who))


master = Start()

# Mud object
mud = Connect(master)

# For callbacks
master.bot = bot
master.mud = mud

loop = asyncio.get_event_loop()
loop.create_task(bot.start(TOKEN))
loop.run_until_complete(mud.mud_connect(loop))
loop.close()

# ===========================================================================================

# ===========================================================================================


# mud.do_connect()
# mud_app = mud.tn
# mud_app = mud.connect()
# mud_task = asyncio.ensure_future(mud.connect())
# loop = asyncio.get_event_loop()
# loop.run_forever()

# Get the asyncio event loop

# print("==[ Getting the asyncio.get_event_loop()")
# # main_loop = asyncio.get_event_loop()
# print("==[ Should have asynctio event loop")
# # asyncio.get_child_watcher()
#
# print("\n==< Creating MUD Bot task")
# # mud_task = main_loop.create_task(mud.do_connect())
# # thread_mud = threading.Thread(target=mud.do_connect())
# # thread_mud.start()
# print("==< MUD Bot task should be created")
#
#
#
#
# print("==[ Creating Discord Bot Task")
# # bot_task = main_loop.create_task(start())
# print("==[ Discord Bot Task Assigned")
# main_loop.run_until_complete(bot_task)
# thread = threading.Thread(target=run_it_forever, args=(bot_task,))
# thread.start()

    # bot.run(TOKEN)


# print("*** Attempting to start the tasks")
# main_loop.run_until_complete(mud_task)
# mud_loop = asyncio.get_event_loop()
# mud_loop.run_until_complete(mud.connect())
# mud_loop.close()

# main_loop = asyncio.get_event_loop()

# thread_bot = threading.Thread(target=run_it_forever, args=(bot_task,))
# thread_bot.start()
# thread_mud = threading.Thread(target=run_it_forever, args=(mud_task,))
# thread_mud.start()

# @asyncio.coroutine
# async def start():
#     await bot.start(TOKEN)

# def run_it_forever(loop):
#     loop.run_forever()

# def init():
#     # asyncio.get_child_watcher()
#     bot_loop = asyncio.get_event_loop()
#     bot_loop.create_task(start())
#
#     thread = threading.Thread(target=run_it_forever, args=(bot_loop,))
#     thread.start()