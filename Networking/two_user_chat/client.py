# Created April 17th, 2018

import socket

def main():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# These are temporary of course
	server_ip   = "0.0.0.0"
	server_port = 1400
	packet_size = 2048

	client_socket.connect( (server_ip, server_port) )

	# So the client_sock doesn't crash
	while True:
		try:
			# The data will be encoded with utf-8 when it arrives
			server_data = (client_socket.recv(packet_size).decode("utf-8"))
			print(server_data)

		except:
			print("The server has shutdown. Disconnecting from server...")
			client_socket.close()
			exit(1)



if __name__ == "__main__":
	main()