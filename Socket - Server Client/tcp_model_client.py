#
#Imports de funções e bibliotecas
#
import socket, os, sys
from constants import *

try: 
    #
    #Abrindo socket (Função de abrir conexão está no arquivo constants.py)
    #
    sock = CONEXAO_CLIENT()
    while True:
        #
        #Envio de comando para o server com o nome do arquivo ou parte do nome ou o comando de finalizar operação
        #
        comunicacao = (input('DIGITE O NOME DO ARQUIVO:\r\nexit p/ Sair\r\n>')).encode()
        #
        #Se o comando for exit o programa encerrara a conexão
        #
        if (comunicacao.decode()).lower() == 'exit':
            sock.send(comunicacao)
            sock.close()
            print(f'Fechando SOCKET')
            break
        #
        #Se não o pedido de arquivo será enviado e aguardará o retorno da confirmação e ou de arquivos similares
        #
        sock.send(comunicacao)
        retorno = (sock.recv(4096)).decode()
        retorno = eval(retorno)
        #
        #Se o arquivo não existir o programa mostra arquivos com nome similar
        #
        if retorno[0] == False:
            print(f'ARQUIVO INEXISTENTE, SUGESTÕES:')
            for x in retorno[1]:
                print(x)
        #
        #Se não o download iniciara e salvara o arquivo
        #
        else:
            pct = 0
            pct_total = retorno[1]//4096
            print(f'Pacotes a receber: {pct_total}')
            with open(retorno[3],'wb') as arquivo_retorno:
                while True:
                    sys.stdout.write(f'\rBaixando:{pct} | {pct_total}')
                    data_retorno = sock.recv(4096)
                    arquivo_retorno.write(data_retorno)
                    if pct >= pct_total:
                        print()
                        break
                    pct += 1
except:
    print(f'ERRO: {sys.exc_info}')
