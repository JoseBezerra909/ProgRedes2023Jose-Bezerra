import socket,os

#FUNÇÕES
def CONEXAO_SERVER():
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket_server.bind(('localhost',50000))
    tcp_socket_server.listen(1)
    return tcp_socket_server

def CONEXAO_CLIENT():
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket_server.connect(('localhost',50000))
    return tcp_socket_server

def CHECAR_ARQUIVO(pedido,check):
    server_img = check + '\img_server\\'
    client_img = check + '\img_client\\'
    relatorio = os.listdir(server_img)
    if pedido in relatorio:
        arq_size = os.path.getsize(server_img + pedido)
        return (True, arq_size, server_img + pedido, client_img + pedido)
    else:
        sugestao = []
        for x in relatorio:
            if x.find(pedido) != -1:
                sugestao.append(x)
        return (False,sugestao)

#-------------------------------------------------------------------------
#CONSTANTES
#-------------------------------------------------------------------------