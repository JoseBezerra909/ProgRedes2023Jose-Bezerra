#imports
import socket, ssl, sys
#--------------------------------------------
#funções
def manipular_url(original_url):
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
        )'''
    return s,url_host, url_image, arq_img,arq_txt

#---------------------------------------------
#url_s = manipular_url('http://portal.mec.gov.br/images/comunicado/govbr.png')
#url_s = manipular_url('https://www.nasa.gov/sites/default/files/thumbnails/image/nasa-logo-web-rgb.png')
url_s = manipular_url('https://ead.ifrn.edu.br/portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png')
protocolo = url_s[0]
host = url_s[1]
image = url_s[2]
request = bytes(f'GET {image} HTTP/1.1\r\nHost: {host}\r\n\r\n','utf-8')
buffer = 1024

if 'https' in protocolo :
    port = 443
    context = ssl.create_default_context()
    context.check_hostname = 0
    context.verify_mode = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_ok = context.wrap_socket(sock, server_hostname=host)
    sock_ok.connect((host, port))
    sock_ok.sendall(request)
    data_ret = b''
    while True:
        print('ok')
        data = sock_ok.recv(buffer)
        if not data: 
            print(data_ret)
            break
        data_ret += data
    sock_ok.close()
else:
    print('foi por aqui')
    port = '80'