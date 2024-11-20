import threading
from snippets.lab3 import *

class TCPPeer(Connection):
    def __init__(self, port, callback=None):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind(address(port=port))
        self.__listener_thread = threading.Thread(target=self.__handle_incoming_connections, daemon=True)
        self.__callback = callback
        if self.__callback:
            self.__listener_thread.start()
        
    def __handle_incoming_connections(self):
        self.__socket.listen()
        self.on_event('listen', address=self.__socket.getsockname())
        try:
            while not self.__socket._closed:
                socket, address = self.__socket.accept()
                connection = Connection(socket)
                peerlist.addPeer(connection)
                self.on_event('connect', connection, address)
        except ConnectionAbortedError as e:
            pass # silently ignore error, because this is simply the socket being closed locally
        except Exception as e:
            self.on_event('error', error=e)
        finally:
            self.on_event('stop')

    @property
    def callback(self):
        return self.__callback or (lambda *_: None)

    def close(self):
        self.__socket.close()
    
class PeerList():
    def __init__(self):
        self._list=[]
        pass

    def addPeer(self, connection:Connection):
        self._list.append(connection)
    
    def removePeer(self, connection:Connection):
        self._list.remove(connection)
    
    def sendMessage(self, message:str, username: str):
        for conn in self._list:
            conn.send(username+":"+message)

def startListening(event, connection, address, error):

    print("Start listening")
    match event:
        case 'listen':
            print(f"Server listening on port {address[0]} at {', '.join(local_ips())}")
        case 'connect':
            peer_join(address)
            #TODO: mandagli lista dei peer che non conosce
            #print(f"Open ingoing connection from: {address}")
            connection.callback = on_message_received
            global remote_peer; remote_peer = connection
        case 'stop':
            print(f"Stop listening for new connections")
            peerlist.remove(connection)
        case 'error':
            print(error)
    return True

def on_message_received(event, payload, connection, error):
    match event:
        case 'message':
            parse_message(payload)
        case 'close':
            #print(f"Connection with peer {connection.remote_address} closed")
            peer_left(connection.remote_address)
            global remote_peer; remote_peer = None
        case 'error':
            print(error)

def peer_join(username:str):
    return "Peer "+username+" joined the chat"

def peer_left(username:str):
    return "Peer "+username+" left the chat"

def parse_message(payload:str):
    #i messaggi sono username:messaggio
    #oppure connect
    if(payload.split(":").)

    

peerlist=PeerList()