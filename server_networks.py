import socket
import json
sock = socket.socket()
sock.bind(('', 9096))
sock.listen(1)
conn, addr = sock.accept()
print ('connected:', addr)
err_msg = json.dumps({ 'status': 'bad', 
					   'reason': 'wrong msg format'})
try:
	data = json.loads(conn.recv(1024).decode('utf-8'))
	print(data)
	if not data['type'] == 'server':
		print("smth wrong")
		conn.send(bytes(err_msg,'utf-8'))
except:
	print('exception occures')
	if conn:
		conn.send(bytes(err_msg,'utf-8'))

while True:
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    print('accepted', data)
    conn.send(bytes(data.upper(),'utf-8'))

conn.close()
