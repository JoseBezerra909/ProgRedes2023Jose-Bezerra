#
#Imports de funções e bibliotecas
#
import socket, os, sys
from constants import *

#
#Estabalecendo o local do arquivo e abrindo socket(Função de abrir conexão está no arquivo constants.py)
#
diretorios_img = os.path.dirname(__file__)
sock = CONEXAO_SERVER()

try:
    #
    #Aguardando conexão do cliente
    #
    print(f'Aguardando conexão:')
    conexao,client = sock.accept()
    print(f'Conexão estabelecida com: {client}')
    
    while True:
        #
        #Com o cliente conectado fica aguardando comandos para download de arquivos
        #
        comunicacao = (conexao.recv(4096)).decode()
        
        #
        #Com o comando 'exit' o client fecha conexão do socket
        #
        if comunicacao.lower() == 'exit':
            conexao.close()
            sock.close()
            print(f'Fechando SOCKET')
            break
        
        #
        #Verifica se o arquivo requisitado existe, se não gera uma lista de arquivos com nomes que encaixem no solicitado
        #
        verificacao = CHECAR_ARQUIVO(comunicacao,diretorios_img)
        if verificacao[0] == False:
            conexao.send(str(verificacao).encode())
        
        #
        #Se o Arquivo existir o programa vai abrir o arquivo ler e enviar os dados
        #
        else:
            #
            #Enviar o tamanho do arquivo primeiramente para o cliente acompanhar o progresso do download
            #
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