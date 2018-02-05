import CVProtocol
import socket
import sys

HOST = '127.0.0.1'
PORT = CVProtocol.PORT

if __name__ == '__main__':
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            print('\nConnected to CVServer @ {}:{}'.format(HOST, PORT))
            print('\nEnter message to relay: ')
            message = input()
            if (message == 'q'): break
            CVProtocol.send_data(sock, message)
        except ConnectionError:
            raise ConnectionError()
        finally:
            sock.close()
            print('\nConnection to CVServer @ {}:{} closed.\n'.format(HOST, PORT))
