import socket
import json
import threading

err_msg = json.dumps({ 'status': 'bad', 
					   'reason': 'wrong msg format'})
ok_msg = json.dumps({ 'status': 'ok'})



class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print(client,address);
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, conn, address):
        size = 1024
        data = json.loads(conn.recv(1024).decode('utf-8'))
        if data['type'] == 'server':
            if len(data['login']) > 0:
                conn.send(bytes(ok_msg,'utf-8'))
            else: 
                conn.send(bytes(err_msg,'utf-8'))
        else:
            conn.send(bytes(err_msg,'utf-8'))

        while True:
            try:
                data = json.loads(conn.recv(1024).decode('utf-8'))
                print(data)
                if data['type'] == 'server':
                	print("smth wrong")
                	conn.send(bytes(err_msg,'utf-8'))
                else:
                    raise error('Client disconnected')
                    conn.close()

            except:
                conn.close()
                return False



ThreadedServer('192.168.1.121',9087).listen()
