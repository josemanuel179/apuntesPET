import socket
import os
import sys

def client(direccion, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (direccion, puerto)
    s.connect(server_address)
    try:
        # Manda caca
        s.sendall("caca".encode("utf-8"))
        while True:
            data = s.recv(1024)
            if data:
                print(data.decode("utf-8").strip())
                break

    except:
        print("Error paquete")
        s.close()

    finally:
        s.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        address = "127.0.0.1"
        port = 45000
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    client(address, port)

