import socket
import os
import math

host = '127.0.0.1'
porta = 9999


cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cliente.connect((host,porta))

cliente.send('Testando'.encode('utf-8'))
cliente.send('Testando Novamente\n'.encode('utf-8'))

cliente.close()