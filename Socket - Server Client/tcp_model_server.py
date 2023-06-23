import socket, os, sys,time
from constants import *

diretorios_img = os.path.dirname(__file__)
sock = CONEXAO_SERVER()

try:
    print(f'Aguardando conexão:')
    conexao,client = sock.accept()
    print(f'Conexão estabelecida com: {client}')
    while True:
        comunicacao = (conexao.recv(4096)).decode()
        if comunicacao.lower() == 'exit':
            conexao.close()
            sock.close()
            print(f'Fechando SOCKET')
            break
        
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
                    sys.stdout.write(f'\rEnviando:{total_data_retorno} | {verificacao[1]}')
                    conexao.send(data_retorno)
                    if not data_retorno:
                        print()
                        break
except:
    print(f'ERRO: {sys.exc_info}')