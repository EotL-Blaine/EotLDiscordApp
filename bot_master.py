import asyncio
import json


class Master:
    '''

    '''
    def __init__(self):
        self.bot = None
        self.mud = None
        self.loop = None
        pass

    async def send_to_channel(self, chan, what):
        await chan.send(what)

    def auto_who(self, info):
        from mud_stuff.who import default_who
        who = default_who(info)
        chan = self.bot.get_channel(716783560861941770)

        # Send async
        loop = asyncio.get_event_loop()
        loop.create_task(self.send_to_channel(chan, who))

    def json_from_mud(self, jstr):
        # print("JSON_FROM_MUD\n",jstr)
        pkg = json.loads(jstr)

        # Auto-who posted from MUD
        if pkg["id"] == "auto_who":
            self.auto_who(pkg["data"])
        else:
            pass
