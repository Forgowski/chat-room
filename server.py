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


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        connecting_thread = threading.Thread(target=connecting, args=(client,))
        connecting_thread.start()


def connecting(client):
    try:
        _, nick = connect_account(client)
    except:
        client.close()
        return 0
    if _:
        try:
            with open('ban_list.txt', 'r') as f:
                ban_list = f.readline()
                if str(nick) in ban_list:
                    client.send("[SERVER]You are banned".encode("utf-8"))
                    client.close()
        except:
            pass
        client.send(f"NICK{nick}".encode("utf-8"))
        nicknames.append(nick)
        clients.append(client)
        broadcast(f"[SERVER]{nick} connected to the server \n".encode("utf-8"))
        is_admin = data_base.check_permission(nick)
        thread = threading.Thread(target=handle, args=(client, is_admin))
        thread.start()
        return 0


def connect_account(client):
    try:
        range = 5
        while range:
            nick = client.recv(1024).decode("utf-8")
            password = client.recv(1024).decode("utf-8")
            if data_base.log_in(nick, password):
                client.send("1".encode("utf-8"))
                return 1, nick
            else:
                client.send("0".encode("utf-8"))
                range -= 1

        client.send("Too many mistakes try later".encode("utf-8"))
        client.close()

    except:
        client.close()




def handle(client, is_admin):
    nick = nicknames[clients.index(client)]
    while True:
        try:
            message = client.recv(1024)
            print(message)
            msg = message[len(nicknames[clients.index(client)]) + 2: -1].decode("utf-8")

            if msg.startswith("/"):
                if is_admin:
                    if not check_commands(msg):
                        client.send("[SERVER]Wrong command\n".encode('utf-8'))
                else:
                    client.send("[SERVER]You don't have permission\n".encode('utf-8'))
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


def broadcast(message):
    for client in clients:
        client.send(message)


def check_commands(msg):
    if msg.startswith("/kick"):
        kick(msg[6:].encode("utf-8"))
        return 1

    elif msg.startswith("/ban"):
        ban(msg[5:].encode("utf-8"))
        return 1

    else:
        return 0


def kick(nick_to_kick):
    try:
        index = nicknames.index(nick_to_kick)
        clients[index].send("[SERVER]You are kicked from the server".encode('utf-8'))
        clients[index].close()
        clients.remove(clients[index])
        nicknames.remove(nick_to_kick)
    except:
        pass


def ban(nick_to_ban):
    try:
        index = nicknames.index(nick_to_ban)
        clients[index].send("[SERVER]You are kicked from the server".encode('utf-8'))
        clients[index].close()
        clients.remove(clients[index])
        nicknames.remove(nick_to_ban)
        with open("ban_list.txt", "a") as f:
            f.write(f"{nick_to_ban}\n")
    except:
        pass




print("server running")
receive()
