# Started April 17th, 2018

import socket
import threading 

def main():
	server_socket      = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	# These are temporary of course
	server_ip   	   = "0.0.0.0"
	server_port 	   = 1400
	server_max_clients = 2 # This program is for 

	# Bind the socket to a port on an ip
	server_socket.bind( (server_ip, server_port) )

	# Start listening for incoming requests
	server_socket.listen(server_max_clients)

	# Make sure the server_sock actually initialized
	if not server_socket:
		print("Error creating server socket. Exiting..")
		exit(1)
	else:
		print("Server started at {0}:{1}".format(server_ip, server_port))

	while True:
		client_connection, client_address = server_socket.accept()
		print("{0} joined the server...".format(client_address))

		# Test message
		client_connection.send("This is a test".encode(encoding="utf-8"))

if __name__ ==  "__main__":
	main()