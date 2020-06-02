import asyncio
import json
from telnetlib import Telnet
import os
from dotenv import load_dotenv

# from mud_stuff import who
# import start
from mud_stuff.test_list import test_list

class Connect:

    def __init__(self, master):
        load_dotenv()
        self.HOST = os.getenv('EOTL_HOST')
        self.PORT = os.getenv('EOTL_PORT')
        self.USER = os.getenv('EOTL_USER')
        self.PASS = os.getenv('EOTL_PASS')
        self.PROMPT = b"Ready>"
        self.master = master

    @asyncio.coroutine
    def connect(self):
        self.reader, self.writer = asyncio.open_connection(self.HOST, self.PORT)
        print("Connect()")

        while True:
            msg = yield from self.reader.readline()
            if msg.strip() is None:
                yield from asyncio.sleep(1)
                continue
            self.handle_msg(msg)
        asyncio.sleep(1)

    @asyncio.coroutine
    def handle_msg(self, msg):
        print("handle_msg():", msg)
        self.writer.write("self.writer.write(",msg,")")

    def execute_discord_command(cmd=None):
        pass

    def package_received(self, jpkg=None):
        # for testing purposes
        if jpkg is None:
            jpkg = test_list.test_list_json

        # Convert json pkg to python dict
        pkg = json.loads(jpkg)

        # Send it to the Discord bot
        if pkg["id"] == "auto_who":
            self.master.auto_who(pkg)

    def get_who_list(tn):
        print("========[ WHO LIST  ]========")
        tn.write(b"who -ps eval -f i:3000\n")

        text = tn.read_until(b" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").decode('ascii')
        # print(tn.read_until(b" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").decode('ascii'))
        print(text)
        print("========[  WHO END  ]========")

    @asyncio.coroutine
    async def main_loop(self):
        print("========[ LOOPING ]========")
        # while True:
        try:
            # while True:
            print("Before the await")
            message = "blank message"
            await self.tn.read_until(b'\n\n', timeout=.1).decode('ascii')
            print("xxx", message, "xxx")
            if message != b'' and message != '':
                print("===>", message)
        except EOFError:
            print("=====[ Connection Closed ]=====")
        except Exception as ex:
            pass
            # print("===============================================================")
            # print("EXCEPTION: ", ex)
            # print("===============================================================")
            # print("  tn: ", self.tn)
            # # print("  msg: ", message)
            # return
        print("========[ END LOOP ]========")

    # @asyncio.coroutine
    # def shell(self):

    @asyncio.coroutine
    def do_connect(self):
        with Telnet(self.HOST, self.PORT) as tn:
            self.tn = tn
            # tn.interact()
            tn.read_until(b"Enter your name: ")
            tn.write(self.USER.encode('ascii') + b"\n")
            tn.read_until(b"Password: ")
            tn.write(self.PASS.encode('ascii') + b"\n")

            print("========[ CONNECTED ]========")
            connected = True
            tn.read_until(b'The Eotl uptime meter').decode('ascii')

            # This is before prompt
            tn.read_until(self.PROMPT).decode('ascii')

            # Start input loop
            # loop = asyncio.get_event_loop()
            # loop.create_task(self.main_loop())
            # asyncio.run(self.main_loop())
            print("======================================")
            print("Loop would go after this")
            print("======================================")

            print("========[ LOOPING ]========")
            # while True:
            try:
                while True:
                    print("Before the await")
                    message = "blank message"
                    message = self.tn.read_until(b'\n\n', timeout=.1).decode('ascii')
                    print("xxx", message, "xxx")
                    if message != b'' and message != '':
                        print("===>", message)
                    # await asyncio.sleep(10)
            except EOFError:
                print("=====[ Connection Closed ]=====")
            except Exception as ex:
                pass
                # print("===============================================================")
                # print("EXCEPTION: ", ex)
                # print("===============================================================")
                # print("  tn: ", self.tn)
                # # print("  msg: ", message)
                # return
            print("========[ END LOOP ]========")

            # return
            # self.main_loop()
            # while connected:
            #     tn.read_until(b"***BEGIN***")
            #     msg = tn.read_until(b"***END***").decode('ascii')[0:-9]
            #     if msg == 'hi':
            #         self.send_reply("hi")
            #     else:
            #         print(f'MESSAGE: {msg}')
            #         print("FROM JSON: ",json.loads(msg))
            #         self.package_received(msg)
            #     # Todo: do command here
            #     if msg == 'disconnect':
            #         connected = False
            # self.main_loop()
            # print("after read_until(PROMPT)")

            # get_who_list(tn)

            # print(tn.read_until(PROMPT).decode('ascii'))
            # print(tn.read_all().decode('ascii'))
            # print("Before test_str...")
            # test_str = bytes('tell blaine hi\n', 'ascii')
            # print(f"test_str = '{test_str}' type = '{type(test_str)}'")
            # tn.write(test_str)
            # print("After the write...")
            tn.write(b"tell blaine hi\n")
            print("Told blaine hi")
            # # text = tn.read_until(b'aving')
            # # Thanks for playing, come back soon
            # # print(tn.read_until.decode('ascii'))
            # print(tn.read_until(self.PROMPT).decode('ascii'))
            # tn.write(b"quit\n")
            # print(text)

    async def a_send_reply(self, what):
        if what is not None:
            msg = what.encode('ascii')
            msg = bytes(f'{what}\n', 'utf-8')
            print("=====>", msg)

            # msg = what.encode('ascii' + b"\n")
            try:
                # await self.tn.write(msg.encode('ascii'))
                await self.tn.write(msg)
            except Exception as ex:
                print("===============================================================")
                print("EXCEPTION: ", ex)
                print("===============================================================")
                print("  tn: ", self.tn)
                print("  msg: ", msg)
                print("  what: ", what)
        else:
            await self.tn.write("Null message".encode('ascii')+b"\n")

    def send_reply(self, what):
        loop = asyncio.get_event_loop()
        loop.create_task(self.a_send_reply("tell blaine Received"))




    # three ways to send properly coded text
    #   tn.write(USER.encode('ascii') + b"\n")
    #   test_str = bytes(f'tell {USER} hi\n', 'utf-8')
    #   tn.write(b"tell btest hi\n")

#===========================================================================================

#===========================================================================================