all:
	@echo "Compilación y ejecución de la práctica"
	python3 serv6.py &
	sleep 1
	python3 cli6.py prueba.txt
	pkill -f serv6.py
	@echo "Terminado"

services:
	@echo "Compilación y ejecución de la práctica"
	python3 serv6.py &
	sleep 1
	python3 cli6.py /etc/services
	pkill -f serv6.py
	@echo "Terminado"

binary:
	@echo "Compilación y ejecución de la práctica"
	python3 serv6.py &
	sleep 1
	python3 cli6.py /boot/vmlinuz
	pkill -f serv6.py
	@echo "Terminado"

clean:
	@echo "Limpiando..."

binarybis:
	@echo "Compilación y ejecución de la práctica"
	python3 serv6.py &
	sleep 1
	python3 cli6.py /boot/vmlinuz > /tmp/caca
	diff /boot/vmlinuz /tmp/caca
	pkill -f serv6.py
	@echo "Terminado"
