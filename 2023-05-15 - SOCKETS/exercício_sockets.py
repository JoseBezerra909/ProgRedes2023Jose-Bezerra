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

url_s = manipular_url(input(f'Digite a URL:'))
print(url_s)

url_host    = url_s[0]
url_image   = url_s[1]
url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
host_port   = 80
buffer_size = 1024

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, host_port))
sock_img.sendall(url_request.encode())

print('\nBaixando a imagem...')
# Montado a variável que armazenará os dados de retorno
data_ret = b''
while True:
    data = sock_img.recv(buffer_size)
    if not data: break
    data_ret += data

sock_img.close()

# Obtendo o tamanho da imagem
img_size = -1
tmp = data_ret.split('\r\n'.encode())
for line in tmp:
   if 'Content-Length:'.encode() in line:
      img_size = int(line.split()[1])
      break
print(f'\nTamanho da Imagem: {img_size} bytes')

# Separando o Cabeçalho dos Dados
delimiter = '\r\n\r\n'.encode()
position  = data_ret.find(delimiter)
headers   = data_ret[:position]
image     = data_ret[position+4:]

# Salvando a imagem
file_output = open('image.png', 'wb')
file_output.write(image)
file_output.close()