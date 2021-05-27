import socket
import select
import errno
import os
import sys
from excepciones import UsuarioInvalido

TAMANNO_CABECERA = 10

if len(sys.argv) == 1:
    direccion = "127.0.0.1"
    puerto = 4500
elif len(sys.argv) == 3:
    direccion = sys.argv[1]
    puerto = int(sys.argv[2])
else:
    print("Error en los argumentos")
    exit(1)

mi_nombre = input("Username: ")

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect((direccion, puerto))
socket_cliente.setblocking(False)

nombre_usuario = mi_nombre.encode('utf-8')
cabecera_usuario = f"{len(nombre_usuario):<{TAMANNO_CABECERA}}".encode('utf-8')
socket_cliente.send(cabecera_usuario + nombre_usuario)

lista_sockets = [socket_cliente, sys.stdin]

while True:

            print(f"Dime algo hostia {mi_nombre}")
    #lectores_potenciales, _, _ = select.select(lista_sockets, [], [])

    #for socket_lector in lectores_potenciales:
        #if socket_lector == sys.stdin:
            # Teclado
            mensaje = input()
            if mensaje:
                mensaje = mensaje.encode('utf-8')
                cabecera_mensaje = f"{len(mensaje):<{TAMANNO_CABECERA}}".encode('utf-8')
                socket_cliente.send(cabecera_mensaje + mensaje)
        #else:
            #Mensaje del servidor
            cabecera_usuario = socket_cliente.recv(TAMANNO_CABECERA)

            if not len(cabecera_usuario):
                print('Conexión cerrada por el servidor')
                sys.exit()

            tamanno_usuario = int(cabecera_usuario.decode('utf-8').strip())
            nombre_usuario = socket_cliente.recv(tamanno_usuario).decode('utf-8')

            cabecera_mensaje = socket_cliente.recv(TAMANNO_CABECERA)
            tamanno_mensaje = int(cabecera_mensaje.decode('utf-8').strip())
            mensaje = socket_cliente.recv(tamanno_mensaje).decode('utf-8')

            # Imprimir mensaje otro usuario
            print(f'El servidor dice: {nombre_usuario} > {mensaje}')
