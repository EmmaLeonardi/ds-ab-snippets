from snippets.lab3.utility import *
from snippets.lab3.tests.utility_tests import *


p= TCPPeer(4040, startListening)
username = input('Enter your username to start the chat:\n')
print('Type your message and press Enter to send it. Messages from other peers will be displayed below.')

while True:
    try:
        content = input()
        peerlist.sendMessage(username=username, message=content)
    except (EOFError, KeyboardInterrupt):
        if p:
            p.close()
        break
