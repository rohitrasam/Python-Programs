import socket as st

server = st.socket(st.AF_INET, st.SOCK_STREAM)  # SOCK_STREAM for TCP protocol

server.bind(('0.0.0.0', 9999))

server.listen(1)
print("Server started!")

msg = ''
client, addr = server.accept()

while msg != 'Q':
    msg = client.recv(1024).decode()
    print(msg)
    client.send("Recieved message on the server side.".encode())

server.close()