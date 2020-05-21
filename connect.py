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

with Telnet(HOST, PORT) as tn:
    # tn.interact()
    tn.read_until(b"Enter your name: ")
    tn.write(USER.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASS.encode('ascii') + b"\n")

    test_str = bytes(f'tell {USER} hi\n', 'utf-8')
    tn.write(test_str)
    tn.write(b"tell btest hi\n")
    tn.write(b"who -ps eval -f i:3000\n")
    # text = tn.read_until(b'aving')
    tn.write(b"quit\n")

    print(tn.read_all().decode('ascii'))
    print("========[ ENDED ]========\n")
    # print(text)


# three ways to send properly coded text
#   tn.write(USER.encode('ascii') + b"\n")
#   test_str = bytes(f'tell {USER} hi\n', 'utf-8')
#   tn.write(b"tell btest hi\n")

