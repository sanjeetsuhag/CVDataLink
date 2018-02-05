import CVProtocol

HOST = CVProtocol.HOST
PORT = CVProtocol.PORT

def handle_client(sock, addr):
    try:
        message = CVProtocol.receive_message(sock)
        print('\nReceived following from CVClient @ {}:\n{}.'.format(addr, message))
    except ConnectionError:
        raise ConnectionError()
    finally:
        print('\nConnection to CVClient @ {} closed.\n'.format(addr))
        sock.close()

if __name__ == '__main__':
    listening_socket = CVProtocol.create_socket(HOST, PORT)
    addr = listening_socket.getsockname()
    print('\nCVServer now actively listening on {}.'.format(addr))

    while True:
        client_sock, addr = listening_socket.accept()
        print('\nAccepted connection from CVClient @ {}.'.format(addr))
        handle_client(client_sock, addr)
