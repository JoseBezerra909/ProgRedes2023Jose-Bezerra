import socket, time

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True :
    menu = input(f'BAIXAR ARQUIVOS DIGITE{": 1":>2}\r\nENVIAR MENSAGEM DIGITE{": 2":>2}\r\nPARA SAIR DIGITE {": exit":>11}\r\n>')
    udp_socket.sendto(menu.encode(),('localhost',60000))
    if menu.lower() == 'exit':
        break
    if menu == '1':
        time.sleep(1)
        retorno = eval((udp_socket.recvfrom(4096)[0]).decode())
        print(retorno)
        break

