# CVDataLink

DataLink protocol and classes to handle communication between a Client(`CVClient`) and Server(`CVServer`) via sockets.

## Usage

To send the data to the CVServer, do the following:

1. Install Python 3.
2. Add the `CVProtocol.py` file to your project's root source directory.
3. Add the following lines to the top of your script:
```python
import CVProtocol
import socket
import sys

HOST = '127.0.0.1'
PORT = CVProtocol.PORT
```
4. Use the following lines of code to instantiate a connection, and send a message:

```python
try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((HOST, PORT))
  print('\nConnected to CVServer @ {}:{}'.format(HOST, PORT))
  message = # Set this variable to the string you want to send.
  CVProtocol.send_data(sock, message)
except ConnectionError:
  raise ConnectionError()
finally:
  sock.close()
  print('\nConnection to CVServer @ {}:{} closed.\n'.format(HOST, PORT))
```
