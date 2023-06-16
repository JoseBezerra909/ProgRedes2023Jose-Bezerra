import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect(('localhost',50000))

while True:
    mensagem = bytes(input('Digite a mensagem: '),'utf-8')
    tcp_socket.send(mensagem)
    if (mensagem.decode()).lower() == 'exit':
        tcp_socket.close()
        print('Fechando socket')
        break