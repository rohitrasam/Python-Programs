
import socket as st

client = st.socket(st.AF_INET, st.SOCK_STREAM)

client.connect(("127.0.0.1", 9999))
print("Client Online")

msg = ''

while msg != 'Q':
    msg = input("Enter a message to send!\n-> ")
    client.send(msg.encode())
    print(client.recv(1024).decode())

client.close()
