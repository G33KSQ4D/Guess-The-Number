# Created April 17th, 2018

"""
1. Create socket
2. Connect to host
3. Start multithreading processes for chattin between
   the two people
"""

import socket
import threading
import traceback

def main():
	# Incase the user is a moron
    while True:
        try:
            print("How to format -> host:port")
            host_port_list = input("Enter the address and port (Check above for how to format it): ").split(":")
            host_port_list[1] = int(host_port_list[1])

            if len(host_port_list) == 2:
                # 3 numbers * 4 times + 3 dots (Ex: 192.168.0.101)
                # host_port_list[0] == host name len ipv4 is always greater than 12
                if 7 <= len(host_port_list[0]) <= 3*4+3:
                    if 0 < host_port_list[1] < 65535:
                        print("Alright, trying to connect to server...\n")
                        host = host_port_list[0]
                        port = host_port_list[1]
                        
                        try:
                        	# This function will call other functions
                        	client_socket = initialize_client_socket(host, port)

                        except Exception:
                        	print("Something went wrong... Exiting")
                        	exit(1)

                    else:
                        raise Exception("Port number out of range")
                else:
                    raise Exception("Invalid IP Address")
            else:
                raise Exception("Invalid print format")

        except Exception:
            print(traceback.format_exc())
            continue

def initialize_client_socket(host, port):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	client_socket.connect( (host, port) )

	# Multithreading (Read + write)
	get_incoming_packets_thread = threading.Thread(target=get_incoming_packets, args=(client_socket))
	send_client_packets_thread  = threading.Thread(target=send_client_packets_thread, args=(client_socket))

	get_incoming_packets_thread.start()
	send_client_packets_thread.start()

def get_incoming_packets(client_socket):
	packet_byte_size = 2048

	while True:
		try:
			data = (client_socket.recv(packet_byte_size)).decode("utf-8")
			print(data)

		except:
			print("An error occured. Closing server...\n")
			client_socket.close()
			exit(1)


def send_client_packets(client_socket):
	while True:
		try:
			data = input("> ").encode("utf-8")
			client_socket.send(data)

		except:
			print("An error occured. Closing server...\n")
			client_socket.close()
			exit(1)		

if __name__ == "__main__":
	main()