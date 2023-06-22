import socket, os, sys
from constants import *

try: 
    sock = CONEXAO_CLIENT()
    while True:
        comunicacao = (input('DIGITE O NOME DO ARQUIVO:\r\n>')).encode()
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
                    sys.stdout.write(f'\rBaixando:{pct} {pct_total}')
                    data_retorno = sock.recv(4096)
                    arquivo_retorno.write(data_retorno)
                    if pct > pct_total:
                        break
                    pct += 1
        break
except:
    print(f'ERRO: {sys.exc_info}')







'''
while True:
    mensagem = bytes(input('Digite a mensagem: '),'utf-8')
    tcp_socket.send(mensagem)
    if (mensagem.decode()).lower() == 'exit':
        tcp_socket.close()
        print('Fechando socket')
        break
'''