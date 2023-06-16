import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind(('localhost',50000))

tcp_socket.listen(1)

while True:
    print('aguardando msg: ')
    conexao,cliente = tcp_socket.accept()
    print(f'Conectado com: {cliente[0]}')
    while True:
        mensagem = conexao.recv(4096)
        if (mensagem.decode()).lower() == 'exit':
            conexao.close()
            print('Fechando socket')
            break
        print(f'{cliente[0]}: {mensagem.decode()}')
    break
tcp_socket.close()