import socket
import json

sock = socket.socket()
sock.connect(('192.168.1.121', 9087))
hello = json.dumps({
					'type': 'server', 
					'login': 'lol'
				    })
msg = json.dumps({
	'type': 'broadcast', 'from': 'me', 'msg': 'kek'
})
ans = json.dumps({
	'status': 'ok'
})
print(hello)
sock.send(bytes(hello,'utf-8'))
ans = json.loads(sock.recv(1024).decode('utf-8'))
print(ans)
if ans['status'] == 'ok':
	print("U'r connected")
while True:
	sock.send(bytes(input(), 'utf-8'))
	data = sock.recv(1024).decode('utf-8')
	print(data)
sock.close()