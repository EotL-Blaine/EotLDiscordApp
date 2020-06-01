import discord
from discord.ext import commands

import mud_stuff
from connect import Connect
from mud_stuff.who import default_who

class MyBot2(commands.Bot):

    def __init__(self, master, TOKEN, GUILD, desc):
        super().__init__(command_prefix='!', description=desc)
        self.GUILD = GUILD
        self.master = master

    async def auto_who(self, info):
        print("INFO IS: ",type(info),info)
        who_list = mud_stuff.who.default_who(info)
        chan = self.get_channel(716783560861941770)
        await chan.send(who_list)

    async def relay_channel(self,info):
        for chan in self.get_all_channels():
            if chan.name == info["channel"]:
                break

        await chan.send("Relayed this")
        pass

    async def on_ready(self):
        print("Bot connected.")
        guild = self.get_guild(int(self.GUILD))
        print(f'{self.user} has connected to Discord!\n'
              f'{guild.name} (id: {guild.id})')
        # self.MUD = Connect(self)
        print("Master IS ", self.master)

# @commands.Bot.event()
# async def on_ready(self):
#     """ Called when discord bot is connected and ready """
#     print("Bot connected.")
#     guild = self.bot.get_guild(int(self.GUILD))
#     print(f'{self.user} has connected to Discord!\n'
#           f'{guild.name} (id: {guild.id})')
#     print("MUD IS ", self.mud)
#     self.mud.bot = self
