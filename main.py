# import os
# import discord
# from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord_stuff.eotl_client import EotlClient

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

bot = Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot connected.")

@bot.command()
async def send(*, message):
    print(f'Message: {message}\n')
    global target_channel
    await bot.send_message(target_channel, message)

client = EotlClient()
client.run(client.TOKEN)


# get guild stuff
# for guild in client.guilds:
#     if guild.name == GUILD:
#         break


# print(f'Guild: {guild} - {type(guild)} - {type(guild.id)} - {type(GUILD)}')
# guild = discord.utils.find(lambda g: str(g.id) == GUILD, client.guilds)
# guild = discord.utils.get(client.guilds, name=GUILD)