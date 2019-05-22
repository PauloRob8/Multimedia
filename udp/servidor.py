import socket
import time

HOST = '0.0.0.0'              # Endereco IP do Servidor
PORT = 9999            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = (HOST, PORT)
udp.bind(origem)
n = 0

print('Ouvindo dados em %s:%d' %(HOST,PORT))

while n < 2:
    tempo_inicio = time.perf_counter() * 1000
    msg, cliente = udp.recvfrom(1024)
    tempo_fim = time.perf_counter() * 1000
    latencia = tempo_fim - tempo_inicio
    vazão = (1000/latencia) * 1024
    print (cliente, msg)
    print("vazão: %.4f" %vazão)
    print("latencia: %.2f" %latencia) 
    n += 1
udp.close()