#imports
import socket, ssl, sys, requests
#--------------------------------------------
#funções
def manipular_url(original_url):
    #Retira da url declarada os dados necessário para requisição
    url = original_url.split('://',1)
    protocolo = url[0]
    host,url_image = url[1].split('/',1)[0],'/' + url[1].split('/',1)[1]
    image = url_image.rsplit('/',1)[1]
    extensao = image.rfind('.')
    if extensao == -1:
        extensao = '.' + dict(requests.head(original_url).headers)['Content-Type'].split('/',1)[1]
    else:
        extensao = '.'+image.rsplit('.', 1)[1]
    return {'protocolo':protocolo, 'host':host, 'url_image':url_image, 'image':image, 'extensao':extensao}

def conexao(host,protocolo):
    #cria uma conexão http ou https atraves da url
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if 'https' == protocolo:
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

def salvar(dados,arquivo,extensao):
    #Função para criar/salvar os arquivos baixados dos dados requisitados
    try:
        image = open(arquivo + extensao,'wb')
        image.write(dados[1])
        image.close()
        head = open(arquivo + '.txt' ,'wb')
        head.write(dados[0])
        head.close()
        print(f'Seguintes Arquivos Salvos:\n{arquivo}\n{arquivo}')
    except:
        print(f'Erro: {sys.exc_info()[0]}')
        exit()
#---------------------------------------------
#Separa as informações necessárias
#url_s = manipular_url(input('Digite uma URL:'))
#url_s = manipular_url('https://ead.ifrn.edu.br/portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png')
#url_s = manipular_url('http://httpbin.org/image/png')
url_s = manipular_url('https://www.caelum.com.br/apostila/apostila-python-orientacao-a-objetos.pdf')
#print(url_s)
requisicao = bytes(f'GET {url_s["url_image"]} HTTP/1.1\r\nHost: {url_s["host"]}\r\n\r\n','utf-8')
requisicao2 = bytes(f'HEAD /{url_s["url_image"]} HTTP/1.1\r\nHost: {url_s["host"]}\r\n\r\n','utf-8')
buffer = 2048
data_ret = b''
data_ret2 = b''
x = dict(requests.head('https://www.caelum.com.br/apostila/apostila-python-orientacao-a-objetos.pdf').headers)['Content-Length']
x = int(x)

try:
    #Estabelece conexão e recebe os dados
    conectado = conexao(url_s['host'],url_s['protocolo'])
    conectado.sendall(requisicao)
    
    print('Baixando Dados!')
    while True:
        data = conectado.recv(buffer)
        data_ret += data
        print(f'baixou:{len(data)}')
        print(f'total :{len(data_ret)}')
        if len(data_ret) > x:
            print('todo baixado')
            break
    '''
    x = str(requests.head('http://httpbin.org/image/png').headers)
    print(len(x))
    conectado.sendall(requisicao2)
    while True:
        data2 = conectado.recv(buffer)
        data_ret2 += data2
        print(f'baixou:{len(data2)}')
        print(f'total :{len(data_ret2)}')
        if not data2:
            print('head baixado')
            break
    '''
    conectado.close()
    
    dados = data_ret.split('\r\n\r\n'.encode())
    print(f'content-length: {x}')
    print(f'head: {4 + len(dados[0])}')
    print(f'{4 + len(dados[0]),len(dados[1])} soma: {(4+len(dados[0])) + len(dados[1])}')
    #salvar(dados,url_s['image'],url_s['extensao'])
     
except:
    print(f'Erro: {sys.exc_info()[0]}')
    exit()