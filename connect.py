from telnetlib import Telnet
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('EOTL_HOST')
PORT = os.getenv('EOTL_PORT')
USER = os.getenv('EOTL_USER')
PASS = os.getenv('EOTL_PASS')

# host = '163.172.210.70'
# port = 2010
#
# username = 'btest'
# password = 'fatboy'
PROMPT = b"Ready>"

def execute_discord_command(cmd=None):
    pass



def get_who_list(tn):
    print("========[ WHO LIST  ]========")
    tn.write(b"who -ps eval -f i:3000\n")

    text = tn.read_until(b" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").decode('ascii')
    # print(tn.read_until(b" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~").decode('ascii'))
    print(text)
    print("========[  WHO END  ]========")

with Telnet(HOST, PORT) as tn:
    # tn.interact()
    tn.read_until(b"Enter your name: ")
    tn.write(USER.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASS.encode('ascii') + b"\n")

    print("========[ CONNECTED ]========")
    connected = True
    tn.read_until(b'The Eotl uptime meter').decode('ascii')

    # This is before prompt
    tn.read_until(PROMPT).decode('ascii')

    # Start input loop
    print("========[ LOOPING ]========")
    while connected:
        tn.read_until(b"***BEGIN***")
        msg = tn.read_until(b"***END***").decode('ascii')[0:-9]
        print(f'MESSAGE: {msg}')
        # Todo: do command here
        if msg == 'disconnect':
            connected = False
    print("========[ END LOOP ]========")

    # print("after read_until(PROMPT)")

    # get_who_list(tn)

    # print(tn.read_until(PROMPT).decode('ascii'))
    # print(tn.read_all().decode('ascii'))
    print("Before test_str...")
    test_str = bytes('tell blaine hi\n', 'ascii')
    print(f"test_str = '{test_str}' type = '{type(test_str)}'")
    tn.write(test_str)
    print("After the write...")
    # tn.write(b"tell blaine hi\n")
    # text = tn.read_until(b'aving')
    # Thanks for playing, come back soon
    # print(tn.read_until.decode('ascii'))
    print(tn.read_until(PROMPT).decode('ascii'))
    tn.write(b"quit\n")
    # print(text)



# three ways to send properly coded text
#   tn.write(USER.encode('ascii') + b"\n")
#   test_str = bytes(f'tell {USER} hi\n', 'utf-8')
#   tn.write(b"tell btest hi\n")

