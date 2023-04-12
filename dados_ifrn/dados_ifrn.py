import requests,json
unidades = {}
cmd = ''
url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'
dados = requests.get(url).json()
try:
  open('relatorio.txt','x')
except:
    
    for a in range(len(dados)):
        check = dados[a]['campus']
        check2 = dados[a]['curso']
        if check not in unidades:
            unidades[check] = {'Total': 1, check2:1}
        elif (check in unidades) and (check2 not in unidades[check]):
            unidades[check]['Total'] += 1
            unidades[check][check2] = 1
        elif (check in unidades) and (check2 in unidades[check]):
            unidades[check]['Total'] += 1
            unidades[check][check2] += 1

    while cmd != 'N':
        for a in unidades.keys():
            print(f'Total de alunos no campus {a}: {unidades[a]["Total"]}')

        cmd = input('Qual campus deseja acessar?(digite "n" para sair):').upper()
        
        if cmd == 'N':
           exit()
        else:
            with open('relatorio.txt','w') as relatorio:
                relatorio.write('')
            
            for a in unidades[cmd]:
                print(f'{a}: {unidades[cmd][a]}')
                with open('relatorio.txt','a') as relatorio:
                    relatorio.write(f'{a}: {unidades[cmd][a]}\n')