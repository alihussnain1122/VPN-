import socket
import ssl

def vpn_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap socket with SSL for encryption
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('certificates/server.crt')  # Update path to certificate

    secure_socket = context.wrap_socket(client_socket, server_hostname='localhost')

    try:
        secure_socket.connect(('localhost', 1194))
        secure_socket.send("Hello from the VPN Client".encode('utf-8'))
        
        response = secure_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    finally:
        secure_socket.close()

if __name__ == "__main__":
    vpn_client()
