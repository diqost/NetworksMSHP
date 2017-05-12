import socket
import json
import threading

err_msg = json.dumps({ 'status': 'bad', 
					   'reason': 'wrong msg format'})


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = json.loads(conn.recv(1024).decode('utf-8'))
                print(data)
                if data['type'] == 'server':
                	print("smth wrong")
                	conn.send(bytes(err_msg,'utf-8'))
                else:
                    raise error('Client disconnected')
                    client.close()

            except:
                client.close()
                return False



ThreadedServer('',9085).listen()
