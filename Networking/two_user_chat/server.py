# Started April 17th, 2018

# Although this isn't really a server, that techincally
# is what the job of this script is.

# If you are going to use these scripts for some reason,
# Don't forget to enable port forwarding in your router settings
# For whatever port you choose

"""
1. Create socket
2. Bind - Listen - Accept -> connections
3. Start multithreading process for chatting
   between the two people
4. Add a username
"""

import socket
import threading 

def main():
	# I don't want to clutter this function

	# Create socket
	host_socket = initialize_host_socket()

	# Look for a connection
	# ** This function will call other functions **
	accept_a_client(host_socket)

def initialize_host_socket():
	"""
	Initialize a socket for the host, make sure it was successful and start listening for a connection
	"""
	host_socket     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host_ip 	    = "0.0.0.0"
	host_port 	    = 1337
	# This program is only for one person
	max_connections = 1

	# Attach the socket to a port on the host's machine
	host_socket.bind( (host_ip, host_port) )

	# Making sure the socket was created properly and is working
	if host_socket:
		print("Socket created successfully!\nListening for an incoming connection...\n")
		# Start listening for incoming connection
		host_socket.listen(max_connections)
	else:
		print("Error initializing the socket. Exiting.")
		host_socket.close()
		exit(1)

	return host_socket

def accept_a_client(host_socket):
	# Socket connection and IPv4 of the client
	connection, addr = host_socket.accept()

	# At this point, a connection was established 
	while True: # Keep the socket open until someone closes it
		# Need to multithread (To read + write)
		read_incoming_data_thread  = threading.Thread(target=read_incoming_data,  args=(connection, connection, addr))
		send_data_to_client_thread = threading.Thread(target=send_data_to_client, args=(connection, connection, addr)) 

		# Start the threads 
		read_incoming_data_thread.start()
		send_data_to_client_thread.start()


def read_incoming_data(host_socket, connection, addr):
	packet_byte_size = 2048
	while True:
		try:
			data = (connection.recv(packet_byte_size)).decode("utf-8")
			
			if len(data) <= 0:
				print("Client has disconnected")
				host_socket.close()
				exit(1)

			else:
				print(data)
		
		except:
			print("An error occured. Closing server...\n")
			host_socket.close()
			exit(1)

def send_data_to_client(host_socket, connection, addr):
	while True:
		try:
			data_to_send = input("> ").encode(encoding="utf-8")

			if data_to_send.decode("utf-8") == "quit":
				print("Closing the host socket.. Exiting.")
				host_socket.close()
				exit(1)
			else:
				connection.send(data_to_send)

		except:
			print("An error occured. Closing server...\n")
			host_socket.close()
			exit(1)

if __name__ ==  "__main__":
	main()