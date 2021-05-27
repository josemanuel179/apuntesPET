import os
import sys
from time import sleep


def servidor():
    os.close(client_readfd)
    os.close(client_writefd)
    server_readf = os.fdopen(server_readfd, 'r')
    file_name = server_readf.read()
    server_readf.close()
    print("Proceso servidor lee: {}".format(file_name))
    try:
        target_file = open(file_name, 'rb')
        data = target_file.read()
        target_file.close()
        server_writef = os.fdopen(server_writefd, 'wb')
        server_writef.write(data)
        server_writef.flush()
        sleep(0.25)

    except OSError:
        server_writef = os.fdopen(server_writefd, 'w')
        data = "Error en el fichero"
        server_writef.write(data)
        server_writef.flush()
        sleep(0.25)
        exit(1)


def cliente():
    os.close(server_writefd)
    os.close(server_readfd)
    client_writef = os.fdopen(client_writefd, 'w')

    file_name = sys.argv[1]

    client_writef.write(file_name)
    client_writef.flush()
    client_writef.close()
    client_readf = os.fdopen(client_readfd, 'rb')
    data = client_readf.read()
    os.write(1,data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error en los argumentos")
        exit(1)
    server_readfd, client_writefd = os.pipe()
    client_readfd, server_writefd = os.pipe()

    pid = os.fork()
    if pid:
        # padre
        servidor()

    else:
        # hijo
        cliente()











