import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 9999           # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (HOST, PORT)

udp.sendto('Testando'.encode('utf-8'),destino)
udp.sendto('Testando novamente'.encode('utf-8'),destino)

udp.close()