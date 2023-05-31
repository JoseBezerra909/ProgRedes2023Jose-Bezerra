#imports
import socket, ssl, sys
#--------------------------------------------
#funções
def manipular_url(original_url):
    #Retira da url declarada os dados necessário para requisição
    url = original_url.split('//',1)
    s = url[0]
    url_host = url[1].split('/',1)[0]
    url_image = '/' + url[1].split('/',1)[1]
    arq_img = url[1].rsplit('/',1)[1]
    ext = arq_img.rsplit('.',1)[1]
    arq_txt = arq_img.replace(ext,'txt')
    '''
    print(f'{s}\n'
        f'{url_host}\n'
        f'{url_image}\n'
        f'{arq_img}\n'
        f'{arq_txt}\n'
        )
    '''
    return s,url_host, url_image, arq_img,arq_txt

def conexao(host,protocolo):
    #cria uma conexão http ou https atraves da url
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if 'https' in protocolo:
        try:
            print(f'Conexão HTTPS Estabelecida!')
            port = 443
            context = ssl.create_default_context()
            context.check_hostname = 0
            context.verify_mode = 0
            socketTCP_ok = context.wrap_socket(socketTCP,server_hostname = host)
            socketTCP_ok.connect((host,port))
            return socketTCP_ok
        except:
            print(f'Erro na conexão HTTP: {sys.exc_info()[0]}')
            exit()
    elif 'http' in protocolo:
        try:
            print(f'Conexão HTTP Estabalecida!')
            port = 80
            socketTCP.connect((host,port))
            return socketTCP
        except:
            print(f'Erro na conexão HTTP: {sys.exc_info()[0]}')
            exit()
    else:
        print(f'Protocolo não suportado')
    return

def salvar(dados,arquivo,arquivo_txt):
    #Função para criar/salvar os arquivos baixados dos dados requisitados
    try:
        image = open(f'Socket - File Download\{arquivo}','wb')
        image.write(dados[1])
        image.close()
        head = open(f'Socket - File Download\{arquivo_txt}','wb')
        head.write(dados[0])
        head.close()
        print(f'Seguintes Arquivos Salvos:\n{arquivo}\n{arquivo_txt}')
    except:
        print(f'Erro: {sys.exc_info()[0]}')
        exit()
#---------------------------------------------
#Separa as informações necessárias
url_s = manipular_url(input('Digite uma URL:'))
protocolo = url_s[0]
host = url_s[1]
image = url_s[2]
request = bytes(f'GET {image} HTTP/1.1\r\nHost: {host}\r\n\r\n','utf-8')
buffer = 1024
data_ret = b''

try:
    #Estabelece conexão e recebe os dados
    conectado = conexao(host,protocolo)
    conectado.sendall(request)
    
    print('Baixando Dados!')
    while True:
        data = conectado.recv(buffer)
        data_ret += data
        if not data:
            break  
    conectado.close()
    
    dados = data_ret.split('\r\n\r\n'.encode())
    salvar(dados,url_s[3],url_s[4])
    
except:
    print(f'Erro: {sys.exc_info()[0]}')
    exit()