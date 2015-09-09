import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))


client_socket.settimeout(3)
REQ = "GET /api/getState HTTP/1.0\r\n\r\n"
client_socket.send(REQ)

data = client_socket.recv(1024)

print "RECIEVED:" , data