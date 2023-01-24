import socket
import threading
import data_base

HOST = "127.0.0.1"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client, is_admin):
    nick = nicknames[clients.index(client)].decode("utf-8")
    while True:
        try:
            message = client.recv(1024)

            msg = message[len(nicknames[clients.index(client)]) + 2:].decode("utf-8")

            if msg.startswith("/"):
                if is_admin:
                    pass
                else:
                    client.send("You don't have permission\n".encode('utf-8'))
            else:
                print(f"{nick} says {message}")
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        broadcast(f" {nickname} connected to the server \n".encode("utf-8"))
        client.send("Connected to the server".encode('utf-8'))
        is_admin = data_base.check_permission(nickname.decode("utf-8"))
        thread = threading.Thread(target=handle, args=(client, is_admin))
        thread.start()


def check_commands(msg):
    # print("y")
    # if data_base.check_permission(nick):
    # print(data_base.check_permission(nick))
    # else:
    #     print("you don't have permission")
    pass

def kick():
    pass


def ban():
    pass


print("server running")
receive()
