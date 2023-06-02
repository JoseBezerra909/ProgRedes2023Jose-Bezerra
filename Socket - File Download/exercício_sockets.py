#imports
import socket, ssl, sys, requests
#--------------------------------------------
#funções
def manipular_url(original_url):
    #Retira da url declarada os dados necessário para requisição
    url = original_url.split('://',1)
    cabecalho = requests.head(original_url).headers
    protocolo = url[0]
    host,url_image = url[1].split('/',1)[0],'/' + url[1].split('/',1)[1]
    image = url_image.rsplit('/',1)[1]
    image = image.rsplit('.', 1)[0]
    extensao = '.' + (cabecalho['Content-Type'].split('/',1)[1]).split(';')[0]
    tamanho = cabecalho['Content-Length']
    return {'protocolo':protocolo, 'host':host, 'url_image':url_image, 'image':image, 'extensao':extensao, 'tamanho':tamanho}

def conexao(host,protocolo):
    #cria uma conexão http ou https atraves da url
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if 'https' == protocolo:
        try:
            port = 443
            context = ssl.create_default_context()
            context.check_hostname = 0
            context.verify_mode = 0
            socketTCP_ok = context.wrap_socket(socketTCP,server_hostname = host)
            socketTCP_ok.connect((host,port))
            print(f'Conexão HTTPS Estabelecida!')
            return socketTCP_ok
        except:
            print(f'Erro na conexão HTTP: {sys.exc_info()[0]}')
            exit()
    elif 'http' == protocolo:
        try:
            port = 80
            socketTCP.connect((host,port))
            print(f'Conexão HTTP Estabalecida!')
            return socketTCP
        except:
            print(f'Erro na conexão HTTP: {sys.exc_info()[0]}')
            exit()
    else:
        print(f'Protocolo não suportado')
    return

def salvar(dados,arquivo,extensao):
    #Função para criar/salvar os arquivos baixados dos dados requisitados
    character = [':','/','*','?','"','<','>','|',"'"]
    local = 0
    for special in character:
        while local != -1:    
            local = arquivo.find(special)
            arquivo = arquivo.replace(special,'')
        local = 0
    try:
        
        image = open(arquivo + extensao,'wb')
        image.write(dados[1])
        image.close()
        cabecalho = open(arquivo + '.txt' ,'wb')
        cabecalho.write(dados[0])
        cabecalho.close()
        #print(f'\nSeguintes Arquivos Salvos:\n{arquivo+extensao}\n{arquivo+"txt"}')
    except OSError as e:
        print(e)
        exit()
    except:
        print(f'Erro: {sys.exc_info()[0]}')
        exit()
#---------------------------------------------
#Separa as informações necessárias
url_s = manipular_url(input('Digite uma URL:'))
#url_s = manipular_url('https://ead.ifrn.edu.br/portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png')
#url_s = manipular_url('http://httpbin.org/image/png')
#url_s = manipular_url('https://down-lum-br.img.susercontent.com/br-11134103-23010-10t41nrr7vlv89.webp')
#url_s = manipular_url('https://www.caelum.com.br/apostila/apostila-python-orientacao-a-objetos.pdf')
#url_s = manipular_url('https://uploads.jovemnerd.com.br/wp-content/uploads/2022/04/star_wars_darth_vader_tudo_sobre__cv04bw-1210x544.jpg')
print(url_s)
requisicao = bytes(f'GET {url_s["url_image"]} HTTP/1.1\r\nHost: {url_s["host"]}\r\nConnection: close\r\n\r\n','utf-8')
buffer = 4096
data_ret = b''
try:
    #Estabelece conexão e recebe os dados
    conectado = conexao(url_s['host'],url_s['protocolo'])
    conectado.sendall(requisicao)
    print(f'{"Preparando Para Baixar Dados!"}')
    while True:
        data = conectado.recv(buffer)
        data_ret += data
        sys.stdout.write(f'\rBaixando: {len(data_ret)}')
        if not data:
            conectado.close()
            break
    dados = data_ret.split('\r\n\r\n'.encode())
    print(f'\n{dados[0]}')
except:
    print(f'Erro ao baixar: {sys.exc_info()[0]}')
    exit()
salvar(dados,url_s['image'],url_s['extensao'])