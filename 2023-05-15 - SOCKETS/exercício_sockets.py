
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
#----------------------------

url_s = manipular_url(input(f'Digite a URL:'))
print(url_s[0])