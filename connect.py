from telnetlib import Telnet

host = '163.172.210.70'
port = 2010

username = 'btest'
password = 'fatboy'

with Telnet(host, port) as tn:
    # tn.interact()
    tn.read_until(b"Enter your name: ")
    tn.write(username.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    tn.write(b"tell btest hi\n")
    tn.write(b"quit\n")

    print(tn.read_all().decode('ascii'))

