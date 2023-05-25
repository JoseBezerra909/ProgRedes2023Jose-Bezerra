#imports
import socket, ssl, sys
#--------------------------------------------
#funções
def manipular_url(original_url):
    url = original_url.split('.',1)[1]
    url_host = url.split('/',1)[0]
    url_image = url.split('/',1)[1]
    arq_img = url.rsplit('/',1)[1]
    extensao = arq_img.rsplit('.',1)[1]
    arq_txt = arq_img.replace(extensao,'txt')

    print(f'{url}\n'
          f'{url_host}\n'
          f'{url_image}\n'
          f'{arq_img}\n'
          f'{arq_txt}\n'
          )
    return url_host,url_image,arq_img,arq_txt
#---------------------------------------------

#url_s = manipular_url(input('Digite URL: '))
host = 'www.example.com'
port = 80

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    request = bytes(f'GET / HTTP/1.1\r\nHost: {host}\r\n\r\n','utf-8')
    sock.send(request)

    while True:
        resposta = sock.recv(1024)
        resposta = resposta.decode('utf-8')
        print(resposta) 
        if not resposta: 
            sock.close()
            break    

except socket.gaierror as e:
    print(f'{e}')