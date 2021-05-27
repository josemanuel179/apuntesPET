import socket
import os
import sys
import select

TAMANNO_CABECERA = 10

def recibir_mensaje(socket_cliente):
    try:
        cabecera_mensaje = socket_cliente.recv(TAMANNO_CABECERA)
        
        if not len(cabecera_mensaje):
            return False

        length_mensaje = int(cabecera_mensaje.decode('utf-8').strip())
        return {'header': cabecera_mensaje, 'data': socket_cliente.recv(length_mensaje)}
    except:
        return False

def broadcast(socket_escritor, mensaje):
    for socket in clientes:
        #if socket != socket_escritor:
        socket.send(user['header'] + user['data'] + mensaje['header'] + mensaje['data'])

def eliminar_cliente(socket_cliente):
    lista_sockets.remove(socket_cliente)
    lista_nombres.remove(clientes[socket_cliente]['data'])
    del clientes[socket_cliente]


# ------- #

if len(sys.argv) == 1:
    address = "0.0.0.0"
    port = 4500

elif len(sys.argv) == 2:
    address = "0.0.0.0"
    port = int(sys.argv[1])

elif len(sys.argv) == 3:
    address = sys.argv[1]
    port = int(sys.argv[2])

else:
    print("Error en los argumentos")
    exit(1)


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_servidor.bind((address, port))
socket_servidor.listen()

lista_sockets = [socket_servidor]
lista_nombres =[]
clientes = {}

print("Arrancando servidor en dirección: " + address + " puerto: " + str(port))

try:
    while True:
        lectores_potenciales, _, errores_potenciales = select.select(lista_sockets, [], lista_sockets, 0)
    
        for socket_lector in lectores_potenciales:
            # Nueva conexión
            if socket_lector == socket_servidor: 
                socket_cliente, direccion_cliente = socket_servidor.accept()
                lista_sockets.append(socket_cliente)

            # Recibir nombre usuario
            elif socket_lector not in clientes:
                user = recibir_mensaje(socket_cliente)
                
                if user is False:
                    continue

                if user['data'] in lista_nombres:
                    socket_lector.send("User used".encode("utf-8"))
                    continue

                lista_nombres.append(user['data'])
                clientes[socket_lector] = user

                print('Nueva conexión desde {}:{}, usuario: {}'.format(*direccion_cliente, user['data'].decode('utf-8')))

            # Recibir mensaje
            else:
                mensaje = recibir_mensaje(socket_lector)
                if mensaje is False:
                    print('Cierre conexión : {}'.format(clientes[socket_lector]['data'].decode('utf-8')))
                    eliminar_cliente(socket_lector)
                    continue

                print(f'Mensaje de {user["data"].decode("utf-8")}: {mensaje["data"].decode("utf-8")}')
                broadcast(socket_lector, mensaje)

        for socket_lector in errores_potenciales:
            eliminar_cliente(socket_lector)

except:
    pass