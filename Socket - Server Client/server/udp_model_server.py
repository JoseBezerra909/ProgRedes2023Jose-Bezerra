import socket,sys,os, time


def lista_arquivos():

    atual_dir = os.path.dirname(__file__) + '\img'
    arquivos_lista = os.listdir(atual_dir)
    return arquivos_lista

arquivos = str(lista_arquivos())
print(arquivos)
arquivos = eval(arquivos)
#arquivos = bytes(list(lista_arquivos()), 'utf-8')
print(arquivos)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind(('localhost', 60000))

try:
    print(f'Aguardando MSG:')
    while True:
        menu,ip_client = udp_socket.recvfrom(4096)
        print(ip_client)
        if (menu.decode()).lower() == 'exit':
            print('Fechando Server')
            udp_socket.close()
            break
        if menu.decode() == '1':
            udp_socket.sendto(arquivos,(ip_client[0],ip_client[1]))
except AttributeError as b:
    print(b)

except TypeError as e:
    print(e)
except:
    udp_socket.close()
    print(f'Erro: {sys.exc_info()[0]}')

'''print(f"{ip_client}: {menu.decode()}")'''