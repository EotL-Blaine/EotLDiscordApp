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

    async def on_member_join(self, member):
        '''
        Called upon a new member joining the server

        Parameters
        ----------
        member : member object
        '''
        await member.create_dm()
        await member.dm_channel.send(
            f'Welcome, {member.name} to the End of the Line Discord!,\n'
            f'Remember the rules:\n'
            f"1) have fun\n2) don't piss someone off bigger than you"
        )
        # show additional commands for the bot, and in-game

    async def on_message(self, message):
        '''
        Called when a member posts a message in a discord channel

        :param message: message object
        '''

        if message.author == self.user:
            return

        if (message.content[0] == '!'):
            await message.channel.send(
                f'Command given: {message.content[1:]}'
            )
            # do command
            return

        # if (message.content == 'testing 123'):
        await message.channel.send(
            f'Message: {message.content}\n'
        )
        print(f"Relayed: {message.content}")
