import socket
import time

ip = '0.0.0.0'
porta = 9999

tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp.bind((ip,porta))
tcp.listen(5)

print ("Ouvindo dados em %s %d" %(ip,porta))
while True:
    concetcion, cliente = tcp.accept()
    print(concetcion,cliente)
    print ('Concetado por', cliente)
    

    while True:
        start = time.perf_counter() * 1000
        msg = concetcion.recv(1024)
        if not msg: 
            break
        end = time.perf_counter() * 1000
        latencia = end - start
        vazão = (1000/latencia) * 1024
        print("vazão: %.4f" %vazão)
        print("latencia: %.2f" %latencia)       
        print (cliente, msg)
        print ('Finalizando conexao do cliente', cliente)
        concetcion.close()