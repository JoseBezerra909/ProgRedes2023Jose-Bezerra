import socket, os, sys,time
from constants import *

diretorios_img = os.path.dirname(__file__)
sock = CONEXAO_SERVER()

try:
    while True:
        print(f'Aguardando conexão:')
        conexao,client = sock.accept()
        print(f'Conexão estabelecida com: {client}')
        comunicacao = (conexao.recv(4096)).decode()
        verificacao = CHECAR_ARQUIVO(comunicacao,diretorios_img)
        
        if verificacao[0] == False:
            conexao.send(str(verificacao).encode())
        else:
            conexao.send(str(verificacao).encode())
            total_data_retorno = 0
            with open(verificacao[2], 'rb') as arquivo_retorno:
                while True:
                    data_retorno = arquivo_retorno.read(4096)
                    total_data_retorno += len(data_retorno)
                    sys.stdout.write(f'\rBaixando:{total_data_retorno} {verificacao[1]}')
                    conexao.send(data_retorno)
                    if not data_retorno:
                        break
        break
except:
    print(f'ERRO: {sys.exc_info}')




'''
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
'''