import socket

HOST = ''
PORT = 10023
BACKLOG = 100
BUFFER_SIZE = 4096

def create_socket(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host, port))
	sock.listen(BACKLOG)
	return sock

def receive_message(sock):
	data = bytearray()
	message = ''
	while not message:
		received = sock.recv(BUFFER_SIZE)
		if not received:
			raise RuntimeError()
		data = data + received
		if b'\0' in received:
			message = data.rstrip(b'\0')
	message = message.decode('utf-8')
	return message

def prepare_message(message):
	message += '\0'
	return message.encode('utf-8')

def send_data(sock, data):
	message = prepare_message(data)
	sock.sendall(message)
