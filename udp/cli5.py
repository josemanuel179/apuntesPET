import socket
import os
import sys

def client(direccion, puerto, request):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", 0))
    server_address = (direccion, puerto)
    try:
        s.sendto(request.encode("utf-8"), server_address)
        tamanno_texto = int(s.recv(1024).decode("utf-8").strip())

        while tamanno_texto > 0:
            data = s.recv(1024).decode("utf-8")
            print(data)
            tamanno_texto -= 1

    finally:
        print('Cerrando socket')
        s.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        address = "127.0.0.1"
        port = 65431
        request = sys.argv[1]
    elif len(sys.argv) == 4:
        address = sys.argv[1]
        port = int(sys.argv[2])
        request = sys.argv[3]
    else:
        print("Error en los argumentos")
        exit(1)

    client(address, port, request)

