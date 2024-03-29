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
    flag = True

    while flag:

        try:
            _, nick = connect_account(client)
            if _ == 1:
                flag = False
            elif _ == 0:
                client.close()
                return 0
        except:
            client.close()
            return 0

    if _ == 1:
        try:
            with open('ban_list.txt', 'r') as f:
                ban_list = f.readline()
                if str(nick) in ban_list:
                    client.send("[SERVER]You are banned".encode("utf-8"))
                    client.close()
                    return 0
        except:
            pass
        if nick is not None:
            nicknames.append(nick)
            clients.append(client)
            broadcast(f"[SERVER]{nick} connected to the server \n".encode("utf-8"))
            is_admin = data_base.check_permission(nick)
            thread = threading.Thread(target=handle, args=(client, is_admin, nick))
            thread.start()
        else:
            client.close()
            return 0
    else:
        client.close()
        return 0


def connect_account(client):
    try:
        range = 5
        while range:
            recv = client.recv(1024).decode("utf-8").split(" ")
            nick = recv[1]
            password = recv[2]
            recv = recv[0]

            if recv == "L":
                if data_base.log_in(nick, password):
                    client.send("1".encode("utf-8"))
                    return 1, nick
                else:
                    client.send("0".encode("utf-8"))
                    range -= 1
            elif recv == "R":
                if data_base.if_used(nick):
                    data_base.register_client(nick, password)
                    client.send("1".encode("utf-8"))
                    return 2, None
                else:
                    client.send("0".encode("utf-8"))
        client.send("Too many mistakes try later".encode("utf-8"))
        return 0, None

    except:
        return 0, None


def handle(client, is_admin, nick):
    while True:
        try:
            message = client.recv(1024)
            msg = message[: -1].decode("utf-8")

            if msg.startswith("/"):
                if is_admin:
                    if not check_commands(msg):
                        client.send("[SERVER]Wrong command\n".encode('utf-8'))
                else:
                    client.send("[SERVER]You don't have permission\n".encode('utf-8'))
            else:
                message = f"{nick}: {msg}\n".encode('utf-8')
                print(message[:-1])
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
        kick(msg[6:])
        return 1

    elif msg.startswith("/ban"):
        ban(msg[5:])
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
