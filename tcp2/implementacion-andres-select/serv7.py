import socket
import select
import sys
import datetime
import time
import queue

import noticia
import os

noti = noticia.Noticia(datetime.date.today(), "prueba")
noticias = [noti, noti]
list_of_nicknames = []
buffersize = 4096


def server(server_address, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    s.bind((server_address, server_port))
    s.listen(5)
    inputs = [s]
    outputs = []
    message_queues = {}
    print("Escuchando ...")

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        print(readable, exceptional)

        for elem in exceptional:
            inputs.remove(elem)
            if s in outputs:
                outputs.remove(elem)
            s.close()
            del message_queues[elem]

        for elem in readable:

            try:
                if elem is s:
                    connection, client_address = s.accept()
                    print('Connected by', client_address)
                    connection.setblocking(0)
                    inputs.append(connection)
                    message_queues[connection] = queue.Queue()

                else:
                    mensaje = elem.recv(buffersize).decode("utf-8")
                    mensaje = mensaje.split()
                    print(mensaje)

                    if mensaje[0] == "nick":
                        if mensaje[1] in list_of_nicknames:
                            elem.send(b"NACK")
                            print("Fallo en registrar cliente: {}".format(mensaje[1]))
                        else:
                            elem.send(b"ACK")
                            list_of_nicknames.append(mensaje[1])

                    elif mensaje[0] == "request":
                        fecha = datetime.date(int(mensaje[1]), int(mensaje[2]), int(mensaje[3]))
                        for aux in noticias:
                            if aux.fecha > fecha:
                                elem.send(aux.texto.encode("utf-8"))
                                time.sleep(1)
                        elem.send(b"fin-de-mensaje")

                    elif mensaje[0] == "news":
                        fecha = datetime.date.today()
                        texto = mensaje[1:]
                        texto = "".join(texto)
                        aux = noticia.Noticia(fecha, texto)
                        noticias.append(aux)
                        elem.send(b"noticia-recibida")

            except IndexError:
                elem.close()
                print("cerro")
                inputs.remove(elem)


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
