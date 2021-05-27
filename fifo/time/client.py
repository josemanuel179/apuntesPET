import os, time, errno

FIFO = '/tmp/server-client'

fifo_lectura = open(FIFO, "r")
mensaje_cliente = fifo_lectura.readline()
print(mensaje_cliente)
'''
for line in (fifo_lectura.readlines() [-1:]):
    print(line)
'''
