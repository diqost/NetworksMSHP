import socket
import json

sock = socket.socket()
sock.connect(('localhost', 9085))
hello = json.dumps({
					'type': 'server', 
					'login': 'diqost'
				    })
print (hello)
sock.send(bytes(hello,'utf-8'))
data = sock.recv(1024).decode('utf-8')
if not json.loads(data).status == 'ok':
	print("smth wrong")
	exit()
while True:
	sock.send(bytes(input(), 'utf-8'))
	data = sock.recv(1024).decode('utf-8')
	print(data)
sock.close()


 