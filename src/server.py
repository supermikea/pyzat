import socket
import threading

server = socket.socket()
print("Socket successfully created")


port = 1

while True:
	try:
		server.bind(('', port))
		break
	except:
		print("trying different ports...")
		port += 1

print("socket binded to %s" %(port))

server.listen(5)

while True:

	client, addr = server.accept()
	print('Got connection from', addr)

	client.send('Thank you for connecting!\n'.encode())
