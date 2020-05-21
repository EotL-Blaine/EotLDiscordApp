import os
import discord
from dotenv import load_dotenv
from discord.ext.commands import Bot

class EotlClient(discord.Client):
    """
    Custom class for discord client
    Handles initialization and events

    Attributes
    ----------
    TOKEN : str
        retrieved from .env file, token for connecting to server
    GUILD : str
        retrieved from .env file, this is the guild ID (str)

    Methods
    -------
    __init__()
        Initializes instance
    on_ready()
        Called when client connects to the discord server

    """

    def __init__(self):
        super().__init__()
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD = os.getenv('DISCORD_GUILD')
        print(f'token: {type(self.TOKEN)}\nguild: {type(self.GUILD)}')

    async def on_ready(self):
        '''Called when client connects to the discord server'''
        guild = self.get_guild(int(self.GUILD))

        print(f'{self.user} has connected to Discord!\n'
              f'{guild.name} (id: {guild.id})' )


