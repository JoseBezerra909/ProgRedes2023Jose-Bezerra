import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True :
    mensagem = bytes(input('Digite a MSG: '),'utf-8')
    udp_socket.sendto(mensagem,('localhost',50000))
    if (mensagem.decode()).lower() == 'exit':
        udp_socket.close()
        break

