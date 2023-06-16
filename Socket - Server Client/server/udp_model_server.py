import socket,sys,os

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind(('localhost', 50000))

try:
    print(f'Aguardando MSG:')
    while True:
        mensagem,ip_client = udp_socket.recvfrom(4096)
        if (mensagem.decode()).lower() == 'exit':
            print('Fechando Server')
            udp_socket.close()
            break
        print(f'{ip_client}: {mensagem.decode()}')
except:
    udp_socket.close()
    print(f'Erro: {sys.exc_info()[0]}')

#atual_dir = os.path.dirname(__file__) + '\img' + '\img1.png'