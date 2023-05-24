#imports
import socket
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

#url_s = manipular_url(input(f'Digite a URL:'))
#print(url_s)

#url_host    = url_s[0]
#url_image   = url_s[1]

host = 'nasa.gov'
port = 443

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((host , port))

requisicao = f'HEAD / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\nConnection: close\r\n\r\n'
tcp_socket.sendall(requisicao.encode('utf-8'))

print('-'*100)
print(str(tcp_socket.recv(1024), 'utf-8'))
print('-'*100)

tcp_socket.close()