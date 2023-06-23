import socket, os, sys
from constants import *

try: 
    sock = CONEXAO_CLIENT()
    while True:
        comunicacao = (input('DIGITE O NOME DO ARQUIVO:\r\nexit p/ Sair\r\n>')).encode()
        if (comunicacao.decode()).lower() == 'exit':
            sock.send(comunicacao)
            sock.close()
            print(f'Fechando SOCKET')
            break
        sock.send(comunicacao)
        retorno = (sock.recv(4096)).decode()
        retorno = eval(retorno)
        
        if retorno[0] == False:
            print(f'ARQUIVO INEXISTENTE, SUGESTÕES:')
            for x in retorno[1]:
                print(x)
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
