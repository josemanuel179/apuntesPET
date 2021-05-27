import socket
import os
import sys
bufferSize = 4096


def client(server_address, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_address, server_port))

    nick_check = 0
    while True:
        if nick_check == 0:
            nick = input("Introduce tu Nickname: ")
            mensaje_nick = "nick " + nick
            s.sendto(mensaje_nick.encode("utf-8"), (server_address, port))
            confirmacion = s.recv(bufferSize).decode("utf-8")
            if confirmacion == "ACK":
                print("Login exitoso")
                nick_check = 1
            else:
                print("Error en login")
                break

        string_opciones = "Opcion 1: Solicitar noticias\n" + "Opcion 2: Enviar noticia\n" + "Opcion 3: Salir\n"
        opcion = input(string_opciones)

        if opcion == "1":
            fecha = input("Solicitar noticias desde la fecha (formato de fecha año mes dia separado por espacios: ")
            string_enviar = "request " + fecha
            s.sendto(string_enviar.encode("utf-8"), (server_address, port))
            while True:
                noticias = s.recv(bufferSize).decode("utf-8")
                print(noticias)
                if noticias == "fin-de-mensaje":
                    break

        elif opcion == "2":
            noticia = input("Escriba la noticia a enviar: ")
            string_enviar = "news " + noticia
            s.sendto(string_enviar.encode("utf-8"), (server_address, port))
            confirmacion = s.recv(bufferSize).decode("utf-8")
            if confirmacion == "noticia-recibida":
                print("Noticia enviada exitosamente")
            else:
                print("Error al enviar")

        elif opcion == "3":
            s.close()
            exit(1)

        else:
            print("Error en la opcion elegida")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        address = "127.0.0.1"
        port = 65432
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    client(address, port)