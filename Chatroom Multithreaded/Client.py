import socket
import threading
import traceback


def main():
    while True:
        try:
            print("How to format -> host:port")
            host_port_list = input("Enter the address and port (Check above for how to format it): ").split(":")
            host_port_list[1] = int(host_port_list[1])

            if len(host_port_list) == 2:
                # 3 numbers * 4 times + 3 dots (192.168.0.101)
                # host_port_list[0] == host name len ipv4 is always greater than 12
                if 7 <= len(host_port_list[0]) <= 3*4+3:
                    if 0 < host_port_list[1] < 65535:
                        print("Alright, trying to connect to server...\n")
                        host = host_port_list[0]
                        port = host_port_list[1]
                        if not connect_to_server(host, port):  # If you can't connect to the server retry
                            break
                    else:
                        raise Exception("Port number out of range")
                else:
                    raise Exception("Invalid IP Address")
            else:
                raise Exception("Invalid print format")

        except Exception:
            print(traceback.format_exc())
            continue


def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Making sure client actually connects to the host
    try:
        client_socket.connect((host, port))
    except:
        print("Could not connect to {0}:{1}".format(host, port))
        return False

    # Check to see if client can receive data, if they can welcome them to the server
    try:
        client_address = (client_socket.recv(1024)).decode('utf-8')
        print("Welcome to the server: {0}!".format(client_address))

        # Creating the threads for multi-threading
        read_server_data_thread = threading.Thread(target=read_server_data, args=(client_socket, client_address))
        send_data_server_thread = threading.Thread(target=send_data_server, args=(client_socket, client_address))

        # Starting the threads for multi-threading
        read_server_data_thread.start()
        send_data_server_thread.start()

    except:
        print("Error. Cannot receive data from server.")


def read_server_data(client_socket, client_address):
    while True:
        try:
            # The data will be encoded with utf-8 when it arrives
            data = (client_socket.recv(2048)).decode('utf-8')

            # Printing a new line to make output look better
            print("\n{0}".format(data, client_address))

        except:
            print("The server has shutdown. Disconnecting from server...")
            client_socket.close()
            exit(1)


def send_data_server(client_socket, client_address):
    while True:
        text = input("{0} > ".format(client_address))
        client_socket.send(text.encode(encoding="utf-8"))

if __name__ == "__main__":
    main()
