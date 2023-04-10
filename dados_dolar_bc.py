# discente: José Bezerra de Araújo Neto
# matrícula: 20222014050021
# Questão 01: Solicitar o ano e a média das cotações de compra e
#             e venda do ano informado e as maiores cotações de 
#             compra e venda de cada mês 

import requests
#solicita qual ano o usuário quer consultar para formatar a url
ano = int(input('Informe qual ano deseja consultar:'))
url  = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2701-31-{ano+1}%27&$format=json'
dados = requests.get(url).json()

#função que da a média de compra e venda do mês
def mediadomes(x):
    mes_atual = '01'
    mes_compra = mes_venda = dias = maior_compra = maior_venda =  0
    for a in range(len(x['value'])):
        mes = x['value'][a]['dataHoraCotacao'][5:7]
        if mes != mes_atual:
            print(f'Do mês {mes_atual} Média Compra: ${(mes_compra/dias):.3f}, ',
                  f'Média Venda: ${(mes_venda/dias):.3f}',
                  f'Maior Compra: ${maior_compra:.3f}',
                  f'Maior Venda: ${maior_venda:.3f}')
            mes_atual = mes
            mes_compra = mes_venda = dias = maior_compra = maior_venda =  0
        
        if mes == mes_atual:
            mes_compra += x['value'][a]['cotacaoCompra']
            mes_venda += x['value'][a]['cotacaoVenda']
            
            if maior_compra < x['value'][a]['cotacaoCompra']:
                maior_compra = x['value'][a]['cotacaoCompra']
            
            if maior_venda < x['value'][a]['cotacaoVenda']:
                maior_venda = x['value'][a]['cotacaoVenda']
        dias += 1

#função que da a média de venda e compra do ano
def mediaanual(x):
    soma_compra = soma_venda = 0
    for a in range(len(x['value'])):
        soma_compra += x['value'][a]['cotacaoCompra']
        soma_venda += x['value'][a]['cotacaoVenda']
    print(f'a media anual de compra foi: ${soma_compra/len(x["value"]):.3f},',
          f'a media anual de venda foi: ${soma_venda/len(x["value"]):.3f}')

mediadomes(dados)
mediaanual(dados)