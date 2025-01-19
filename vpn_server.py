import socket
import ssl

def vpn_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1194))  # Port 1194 is commonly used for VPNs
    server_socket.listen(5)

    print("VPN Server is listening on port 1194...")

    # Wrap socket with SSL for encryption
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="certificates/server.crt", keyfile="certificates/server.key")  # Update path to certificates

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Incoming connection from {client_address}")

        # Upgrade client socket to use SSL
        secure_socket = context.wrap_socket(client_socket, server_side=True)

        try:
            data = secure_socket.recv(1024).decode('utf-8')
            print(f"Received data: {data}")
            secure_socket.send("Secure connection established!".encode('utf-8'))
        except ssl.SSLError as e:
            print(f"SSL error: {e}")
        finally:
            secure_socket.close()

if __name__ == "__main__":
    vpn_server()
