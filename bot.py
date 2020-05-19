import os
import discord
import dotenv
from dotenv import load_dotenv
from discord.ext.commands import Bot

# print(dir(dotenv))
from discord_who import get_discord_who

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

bot = Bot(command_prefix='!')

# @bot.event
# async def on_ready():

def get_guild():
    for guild in client.guilds:
        if guild.name == GUILD:
            return guild

@bot.command()
async def send(*, message):
    print(f'Message: {message}\n')
    global target_channel
    await bot.send_message(target_channel, message)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to Discord!\n'
          f'{guild.name} (id: {guild.id})'
          )

    print(f'Event: {client.event}\n')

    # get_discord_who(guild)

    # print("Channels:")
    # print(client.get_all_channels())
    # for channel in client.get_all_channels():
    #     print(f'{channel}')

    channel = client.get_channel(711792526197260398)
    # channel = bot.get
    print(f'Channel is: {channel}')


    # for channel2 in guild.channels:
    #     if channel2.name == "bitch":
    #         break

    # await channel2.send("Hello world part 2")


    # channel = discord.Object(id="bitch")
    channel = discord.Object(id="bitch")
    print("CHANNEL: "+channel.name)
    await channel.send("Hello world")


    # global target_channel
    # target_channel = bot.get_channel(711792526197260398)
    # await bot.send_message(target_channel, "Bot active")


client.run(TOKEN)

# members = '\n - '.join([member.name for member in guild.members])
# print(f'Guild Members:\n - {members}')

# print("==========\nBot Ready\n==========")

# channel = discord.Object(id="bitch")
# await client.send_message(channel, "hello")
