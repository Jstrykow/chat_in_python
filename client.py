import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) 


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    # to na pewno do porawy - to jest tcp
    print(client.recv(2048).decode(FORMAT))
    

send("HELLO WORLD1!")
send("HELLO WORLD2!")
send("HELLO WORLD3!")
send(DISCONNECT_MESSAGE)