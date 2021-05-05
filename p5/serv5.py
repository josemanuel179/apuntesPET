import socket
import os
import sys


def servidor(server_address):
    
    try:
        os.unlink(server_address)
    except OSError:
        if os.path.exists(server_address):
            raise

    s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    s.bind(server_address)

    while True:
        print("Escuchando ...")
        data, addr = s.recvfrom(1024)

        nombre_fichero = data.decode("utf-8").strip()

        try:
            fichero = open(nombre_fichero, "r")
            texto = fichero.read()
            texto_enviar = texto + "\n"
            sent = s.sendto(texto_enviar.encode("utf-8"), addr)

        except FileNotFoundError:
            conn.sendall("Error al abrir el fichero\n".encode('utf-8'))

        s.close()


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        address = "/tmp/ped5_socket_uds"
    elif len(sys.argv) == 2:
        address = "/tmp/" + sys.argv[1]
    else:
        print("error en los argumentos")
        exit(1)
    
    servidor(address)
