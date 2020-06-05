import asyncio
import json
import socket
from telnetlib import Telnet
import os
from dotenv import load_dotenv

class Connect:

    def __init__(self, master):
        load_dotenv()
        self.HOST = os.getenv('EOTL_HOST')
        self.PORT = os.getenv('EOTL_PORT')
        self.USER = os.getenv('EOTL_USER')
        self.PASS = os.getenv('EOTL_PASS')
        self.PROMPT = b"Ready> "
        self.master = master
        self.END_PROMPT = b'***END***\r\n'
        self.END_OF_LINE = b"\r\n"
        self.END_OF_WHO = self.PROMPT
        self.CURRENT_TEXT = ""

    async def mud_connect(self, loop):
        try:
            reader, writer = await asyncio.open_connection(self.HOST, self.PORT, loop=loop)
        except socket.timeout:
            print("Connection timeout caught.")

        # while True: # todo loop this in case connection lost?
        text = await reader.readuntil(b"Enter your name: ")
        print(text.decode())
        writer.write(self.USER.encode('ascii') + b"\n")
        text = await reader.readuntil(b"Password: ")
        print(text.decode())
        writer.write(self.PASS.encode('ascii') + b"\n")
        text = await reader.readuntil(self.PROMPT)
        text = await reader.readuntil(self.PROMPT)
        # break

        print("========[ CONNECTED ]========")
        # self.END = self.END_PROMPT
        self.END = self.END_PROMPT
        while True:
            btext = await reader.readuntil(self.END)
            try:
                text = btext.decode('ascii', "ignore")
                text = ''.join(char for char in text if char != '')

                # Strip prompt
                if text[:7] == "Ready> ":
                    text = text[7:]
            except Exception as ex:
                print("==================\nmud_connect\nException: ",ex,"\n==================\n")

            # self.text_received(text[:-11])
            # print("TEXT:", text)
            text = text.replace('\n', '').replace('\r', '')
            # text = ''.join(text.split("\n"))
            # print("TEXT:", text)
            self.text_received(text)
        # print("Close the socket")

        # writer.close()


    def text_received(self, text):
        '''
        Called when text is received by the bot/user on the MUD
        :param text: the text received
        :return:
        '''

        if text is None or text == '' or len(text) < 11:
            return

        # strip end
        # if text[-11:-2] == "***END***":
        if "***END***" in text:
            text = text.replace("***END***", "")
            print("NEW TEXT:", text)
            # text = text[:-11]

        else: # this shouldn't happen
            return

        # print("text_received:\n",text)

        # Text is JSON, so it needs to be sent to discord bot.receive_json()
        ind = text.find("***JSON***")
        if (ind >= 0):
            self.master.json_from_mud(text[ind+10:])
        else:
            print(f"Received from MUD:\n{text}")

    def send_json_from_mud(self, jtext):
        print(jtext)
        # for testing purposes
        # if jpkg is None:
        #     jpkg = test_list.test_list_json
        # It


        # Convert json pkg to python dict
        # pkg = json.loads(jpkg)

        # # Send it to the Discord bot
        # if pkg["id"] == "auto_who":
        #     self.master.auto_who(pkg)










































    # ===========================================================================================

    # ===========================================================================================

    # three ways to send properly coded text
    #   tn.write(USER.encode('ascii') + b"\n")
    #   test_str = bytes(f'tell {USER} hi\n', 'utf-8')
    #   tn.write(b"tell btest hi\n")

#===========================================================================================

#===========================================================================================
    # @asyncio.coroutine
    # def connect(self):
    #     self.reader, self.writer = asyncio.open_connection(self.HOST, self.PORT)
    #     print("Connect()")
    #
    #     while True:
    #         msg = yield from self.reader.readline()
    #         if msg.strip() is None:
    #             yield from asyncio.sleep(1)
    #             continue
    #         self.handle_msg(msg)
    #     asyncio.sleep(1)
    #
    # @asyncio.coroutine
    # def handle_msg(self, msg):
    #     print("handle_msg():", msg)
    #     self.writer.write("self.writer.write(",msg,")")
    #
    # def execute_discord_command(cmd=None):
    #     pass
#=======================================================
# print("======================================")
# print("Loop would go after this")
# print("======================================")
#
# print("========[ LOOPING ]========")
# # while True:
# try:
#     while True:
#         print("Before the await")
#         message = "blank message"
#         message = self.tn.read_until(b'\n\n', timeout=.1).decode('ascii')
#         print("xxx", message, "xxx")
#         if message != b'' and message != '':
#             print("===>", message)
#         # await asyncio.sleep(10)
# except EOFError:
#     print("=====[ Connection Closed ]=====")
# except Exception as ex:
#     pass
#     # print("===============================================================")
#     # print("EXCEPTION: ", ex)
#     # print("===============================================================")
#     # print("  tn: ", self.tn)
#     # # print("  msg: ", message)
#     # return
# print("========[ END LOOP ]========")

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
# tn.write(b"tell blaine hi\n")
# print("Told blaine hi")
# # # text = tn.read_until(b'aving')
# # # Thanks for playing, come back soon
# # # print(tn.read_until.decode('ascii'))
# # print(tn.read_until(self.PROMPT).decode('ascii'))
# # tn.write(b"quit\n")
# # print(text)
# print("======================================")
# print("Loop would go after this")
# print("======================================")
#
# print("========[ LOOPING ]========")
# # while True:
# try:
#     while True:
#         print("Before the await")
#         message = "blank message"
#         message = self.tn.read_until(b'\n\n', timeout=.1).decode('ascii')
#         print("xxx", message, "xxx")
#         if message != b'' and message != '':
#             print("===>", message)
#         # await asyncio.sleep(10)
# except EOFError:
#     print("=====[ Connection Closed ]=====")
# except Exception as ex:
#     pass
#     # print("===============================================================")
#     # print("EXCEPTION: ", ex)
#     # print("===============================================================")
#     # print("  tn: ", self.tn)
#     # # print("  msg: ", message)
#     # return
# print("========[ END LOOP ]========")

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
# tn.write(b"tell blaine hi\n")
# print("Told blaine hi")
# # text = tn.read_until(b'aving')
# # Thanks for playing, come back soon
# # print(tn.read_until.decode('ascii'))
# print(tn.read_until(self.PROMPT).decode('ascii'))
# tn.write(b"quit\n")
# print(text)
#===========================================================

    # def get_who_list(tn):
    #     print("========[ WHO LIST  ]========")
    #     tn.write(b"who -ps eval -f i:3000\n")
    #
    #     text = tn.read_until(b" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").decode('ascii')
    #     # print(tn.read_until(b" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").decode('ascii'))
    #     print(text)
    #     print("========[  WHO END  ]========")
    #
    # @asyncio.coroutine
    # async def main_loop(self):
    #     print("========[ LOOPING ]========")
    #     # while True:
    #     try:
    #         # while True:
    #         print("Before the await")
    #         message = "blank message"
    #         await self.tn.read_until(b'\n\n', timeout=.1).decode('ascii')
    #         print("xxx", message, "xxx")
    #         if message != b'' and message != '':
    #             print("===>", message)
    #     except EOFError:
    #         print("=====[ Connection Closed ]=====")
    #     except Exception as ex:
    #         pass
    #         # print("===============================================================")
    #         # print("EXCEPTION: ", ex)
    #         # print("===============================================================")
    #         # print("  tn: ", self.tn)
    #         # # print("  msg: ", message)
    #         # return
    #     print("========[ END LOOP ]========")
    #
    # # @asyncio.coroutine
    # # def shell(self):
    #
    #
    # async def a_send_reply(self, what):
    #     if what is not None:
    #         msg = what.encode('ascii')
    #         msg = bytes(f'{what}\n', 'utf-8')
    #         print("=====>", msg)
    #
    #         # msg = what.encode('ascii' + b"\n")
    #         try:
    #             # await self.tn.write(msg.encode('ascii'))
    #             await self.tn.write(msg)
    #         except Exception as ex:
    #             print("===============================================================")
    #             print("EXCEPTION: ", ex)
    #             print("===============================================================")
    #             print("  tn: ", self.tn)
    #             print("  msg: ", msg)
    #             print("  what: ", what)
    #     else:
    #         await self.tn.write("Null message".encode('ascii')+b"\n")
    #
    # def send_reply(self, what):
    #     loop = asyncio.get_event_loop()
    #     loop.create_task(self.a_send_reply("tell blaine Received"))
    #
