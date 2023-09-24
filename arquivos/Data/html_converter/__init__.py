def html(site):
   import requests
   from bs4 import BeautifulSoup

   url = requests.get(f'https://{site}')
   url_content = url.content
   site_html = BeautifulSoup(url_content, 'html.parser')
   
   
    
   nome_arquivo = str(input('Dê um nome para o arquivo html: '))
   
   
   with open(f'{nome_arquivo}.html', 'a', encoding='utf-8') as site_html_content:
      site_html_content.write(site_html.prettify())





