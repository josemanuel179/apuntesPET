import socket
import select
import sys
import datetime
import time

import noticia
import os
noti = noticia.Noticia(datetime.date.today(), "prueba")
noticias = [noti, noti]
buffersize = 4096


def server(server_address, server_port):
    # Creacion socket inicial
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((server_address, server_port))
    s.listen(5)  # El 5 es el backlog
    s.setblocking(0)
    print("Escuchando ...")

    # Creacion objeto epoll
    poller_connections = select.epoll()
    poller_connections.register(s.fileno(), select.EPOLLIN)

    # Listas usadas en el servidor
    list_of_clients = []
    list_of_nicknames = []

    while True:
        print("polling")
        events = poller_connections.poll()
        print(events)
        # Manejo de eventos
        for fileno, event in events:
            print(fileno)
            # Evento cliente nuevo
            if fileno == s.fileno():
                conn, addr = s.accept()
                print('Connected by', addr)
                conn.setblocking(0)
                list_of_clients.append(conn.fileno())
                poller_connections.register(conn.fileno(), select.EPOLLIN)

            # Evento un cliente dice algo
            elif event & select.EPOLLIN:
                mensaje = os.read(fileno, buffersize).decode("utf-8")
                mensaje = mensaje.split()
                print(mensaje)

                if mensaje[0] == "nick":
                    if mensaje[1] in list_of_nicknames:
                        os.write(fileno, b"NACK")
                        print("Fallo en registrar cliente: {}".format(mensaje[1]))
                    else:
                        os.write(fileno, b"ACK")
                        list_of_nicknames.append(mensaje[1])

                elif mensaje[0] == "request":
                    fecha = datetime.date(int(mensaje[1]), int(mensaje[2]), int(mensaje[3]))
                    for elem in noticias:
                        if elem.fecha > fecha:
                            os.write(fileno, elem.texto.encode("utf-8"))
                            time.sleep(1)
                    os.write(fileno, b"fin-de-mensaje")

                elif mensaje[0] == "news":
                    fecha = datetime.date.today()
                    texto = mensaje[1:]
                    texto = "".join(texto)
                    aux = noticia.Noticia(fecha, texto)
                    noticias.append(aux)
                    os.write(fileno, b"noticia-recibida")


if __name__ == "__main__":

    if len(sys.argv) == 1:
        address = "0.0.0.0"
        port = 65432
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    server(address, port)
