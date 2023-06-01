import socket

host  = 'https://ead.ifrn.edu.br/portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png'
port  = 80

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((host , port))

requisicao = f'HEAD / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
tcp_socket.sendall(requisicao.encode('utf-8'))

print('-'*100)
print(str(tcp_socket.recv(1024), 'utf-8'))
print('-'*100)

tcp_socket.close()