import socket
import os
import sys
import datetime


def servidor(direccion, puerto):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((direccion, puerto))
    s.listen(50)

    print("Escuchando ...")

    while True:
        conn, addr = s.accept()

        child_pid = os.fork()
        if child_pid == 0:

            time = 0
            
            try:
                print("Conexión desde: ", addr)
                while True:
                    request = conn.recv(1024).decode("utf-8").strip()
                    if request == "request":
                        time = datetime.datetime.now()
                        response = "Tiempo actual: " + time.strftime("%c")
                        conn.sendall(response.encode("utf-8"))
                        break
                    elif request != "request":
                        response = "Request Error"
                        conn.sendall(response.encode("utf-8"))
                        break

            except KeyboardInterrupt:
                s.close()
                print("Cerrando servidor")
                exit(0)

            finally:
                conn.close()

if __name__ == "__main__":

    if len(sys.argv) == 1:
        address = "0.0.0.0"
        port = 45000
    elif len(sys.argv) == 2:
        address = "0.0.0.0"
        port = int(sys.argv[1])
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    servidor(address, port)
