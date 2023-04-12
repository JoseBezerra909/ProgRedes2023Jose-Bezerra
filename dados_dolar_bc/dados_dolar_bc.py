import requests
ano = int(input('Informe qual ano deseja consultar:'))

url  = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2701-31-{ano+1}%27&$format=json'

dados = requests.get(url).json()

def mediadomes(x):
    mes_atual = '01'
    mes_compra = mes_venda = dias = 0
    for a in range(len(x['value'])):
        mes = x['value'][a]['dataHoraCotacao'][5:7]
        if mes != mes_atual:
            print(f'media de Compra do mês {mes_atual} foi: ${(mes_compra/dias):.2f}, ',
                  f'media de Venda do mês {mes_atual} foi: ${(mes_venda/dias):.2f}')
            mes_atual = mes
            mes_compra = mes_venda = dias = 0
        if mes == mes_atual:
            mes_compra += x['value'][a]['cotacaoCompra']
            mes_venda += x['value'][a]['cotacaoVenda']
        dias += 1

def mediaanual(x):
    soma_compra = soma_venda = 0
    for a in range(len(x['value'])):
        soma_compra += x['value'][a]['cotacaoCompra']
        soma_venda += x['value'][a]['cotacaoVenda']
    print(f'a media anual de compra foi: ${soma_compra/len(x["value"]):.2f},',
          f'a media anual de venda foi: ${soma_venda/len(x["value"]):.2f}')

mediadomes(dados)
mediaanual(dados)