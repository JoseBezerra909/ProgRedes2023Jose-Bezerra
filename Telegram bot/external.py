#imports
import socket

#FUNÇÕES
def CONEXÃO_SERVER():
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket_server.bind(('localhost',50000))
    tcp_socket_server.listen()
    return tcp_socket_server

'''
import os
from dotenv import load_dotenv
load_dotenv(override=True)
with open('Telegram bot/.env','r') as env:
    api = env.readline()
    print(api)
API_key = os.getenv("API_BOT_TELEGRAM")
'''