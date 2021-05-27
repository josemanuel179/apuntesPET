import socket
import os
import sys
import math
import daemon

def servidor(direccion):

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((direccion, 65432))

	print("Escuchando ...")
	
	while True:
		data, addr = s.recvfrom(1024)
		child_pid = os.fork()

		if child_pid == 0:

			nombre_fichero = data.decode("utf-8").strip()

			try:
				fichero = open(nombre_fichero, "r")
				texto = fichero.read()
				texto_enviar = texto + "\n"
				
				tamanno_texto = str(math.ceil(len(texto_enviar) / 1024) + 1)
				s.sendto(tamanno_texto.encode("utf-8"), addr)

				while len(texto_enviar) > 1024:
					s.sendto(texto_enviar[:1024].encode("utf-8"), addr)
					texto_enviar = texto_enviar[1024:]

				s.sendto(texto_enviar[:1024].encode("utf-8"), addr)
				s.sendto("Fin de fichero \n".encode("utf-8"), addr)

			except FileNotFoundError:
				s.sendto("Error al abrir el fichero\n".encode('utf-8'), addr)

	s.close()

with daemon.DaemonContext():
	
	if len(sys.argv) == 1:
		address = "0.0.0.0"
	elif len(sys.argv) == 2:
		address = sys.argv[1]
	else:
		print("Error en los argumentos")
		exit(1)
	
	servidor(address)