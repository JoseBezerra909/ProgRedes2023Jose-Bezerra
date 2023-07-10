#instalaveis python-dotenv,requests
#josé = 5296130584 gio = 697251208 

import socket, threading,requests,os
from external import *

sock = CONEXÃO_SERVER()

API_key = '6369609697:AAHtZAD_hwaUW1zPMss3XKBdUjeh4muweCI'

url_req = f'https://api.telegram.org/bot{API_key}'

requisicao = requests.get(url_req+'/getUpdates')

print(requisicao.json())

id_chat = int(input('Informe o id do Chat:'))

resposta = {'chat_id':id_chat,'text':'olá....'}

var = requests.post(url_req+'/sendMessage',data=resposta)

print(id_chat)