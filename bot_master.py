import asyncio
import json


class Master:
    '''

    '''
    def __init__(self):
        self.bot = None
        self.mud = None

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
        # print("TYPE:", type(jstr))
        print("BEFORE:", jstr)
        pkg = json.loads(jstr)

        # Auto-who posted from MUD
        if pkg["id"] == "auto_who":
            self.auto_who(pkg["data"])
        elif pkg["id"] == "relay":
            self.relay(pkg)
        else:
            pass

    def relay(self, pkg):
        for ch in self.bot.get_all_channels():
            if ch.name == pkg["channel"]:
                break
        # msg = f'```[**{pkg["player"].capitalize()}**]: {pkg["message"]}```'
        msg = f'>>> **[{pkg["player"].capitalize()}]** {pkg["message"]}'
        loop = asyncio.get_event_loop()
        loop.create_task(self.send_to_channel(ch, msg))



        # print("CHANNEL:", chan)
        # print(pkg)
