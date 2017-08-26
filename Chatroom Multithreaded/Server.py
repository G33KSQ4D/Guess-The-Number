import socket
import threading

# I don't feel like passing this into the arguments of functions, so I'm making it global
connected_clients = []


def main():
    print("Created by EagleSnipez/G33KSQ4D with the help from hej. and a few other people from discord - August 16th, 2017")
    host = "0.0.0.0"
    port = 8000
    max_clients = 5
    # buffer = 4096

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(max_clients)

    if not server_sock:
        print("Error creating server socket. Exiting..")
        exit(1)
    else:
        print("Server started at {0}:{1}".format(host, port))

    # The thread for multi-threading
    accept_connections = threading.Thread(target=accept_incoming_connection, args=(server_sock, max_clients))
    accept_connections.start()


def accept_incoming_connection(server_sock, max_clients):
    while True: # while len(connected_clients) <= max_clients
        print("Waiting for clients to join...")
        connection, address = server_sock.accept()
        connected_clients.append(connection)
        print("{0} joined the server...".format(address))

        # Send the client their WAN IP or else they can not see it
        connection.send(address[0].encode(encoding="utf-8"))

        # If there's a new connection start a new thread for them (Data)
        read_client_data = threading.Thread(target=read_incoming_data, args=(connection, address))
        read_client_data.start()  # I forgot this before and was wondering why I couldn't receive data from clients haha


def read_incoming_data(client_connection, client_address):
    while True:
        try:
            data = (client_connection.recv(2048)).decode('utf-8')
            if len(data) <= 0:
                print("{0} has disconnected".format(client_address[0]))
                client_connection.close()
                connected_clients.remove(client_connection)
                break
            else:
                print("{0} > {1}".format(client_address, data))
                broadcast_data_to_connections(data, client_address, client_connection)

        # If there's no data (No connection), close the socket
        except:
            print("{0} has disconnected".format(client_address))
            client_connection.close()
            connected_clients.remove(client_connection)
            break


def broadcast_data_to_connections(message, client_address, client_connection):
    for client in connected_clients:
        if client != client_connection: # We don't want to display message to the sender
            # client_address[0] so you only see the IP address and not port or tuple or IP and port
            client.send(("{0} > {1}\n".format(client_address[0], message)).encode(encoding="utf-8"))


def handle_server_commands(command, client_connection):
    if command == "/users":
        client_connection.send("Users currently in this server: ".encode(encoding="utf-8"))

        for user in connected_clients:
            client_connection.send(user.getsockname().encode(encoding="utf-8"))

if __name__ == "__main__":
    main()
