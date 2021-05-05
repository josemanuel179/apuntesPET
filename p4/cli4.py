import socket
import os
import sys

def cliente(server_address, fichero):
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(server_address)

    try:
        mensaje = fichero
        print('Dirección fichero: {!r}'.format(mensaje))
        s.sendall(mensaje.encode('utf8'))

        tamanno_datos_recibidos = 0
        tamanno_datos_esperados = len(mensaje)

        '''
        while tamanno_datos_recibidos < tamanno_datos_esperados:
            data = s.recv(1024)
            tamanno_datos_recibidos += len(data)
            texto = data.decode('utf8').strip()
            print("Información fichero: " + texto)
        '''
        print("Información fichero: ")
        while True:
        	data = s.recv(1024)
        	if not data:
        		break
        	texto = data.decode('utf8').strip()
        	print(texto)


    finally:
        print("Cerrando socket...")
        s.close()

if __name__ == "__main__":

    if len(sys.argv) == 2:
        address = "/tmp/ped4_socket_uds"
        file = sys.argv[1]
    elif len(sys.argv) == 3:
        address = "/tmp/" + sys.argv[1]
        file = sys.argv[2]
    else:
        print("Error en los argumentos")
        exit(1) 

    cliente(address, file)