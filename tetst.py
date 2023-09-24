import os

from arquivos.Data import web_scraping 

from arquivos.Data import len_arquive

from arquivos.Data import filtro_strings

from arquivos.Data import html_converter

select = 1
while select != 6:
    print('~~'*20)
    print('\
    \n[1]Criar um arquivo txt.\
    \n[2]Ver todas as tags obsoletas\
    \n[3]Apagar txt pra atualizar.\
    \n[4]Analisar tags obsoleta do meu código\
    \n[5]Pegar HTML de um site\
    \n[6]Sair'
    )
    print('~~'*20)
    select = str(input('Selecione uma opção: '))

    while select.isnumeric() == False:
        print('\033[0;31mERRROR: selecione uma opção correta.\033[0m') 
        select = str(input('Selecione uma opção: '))
    select = int(select)

    if select == 1:
         web_scraping.w3c_site()
         print('\033[0;32mArquivo criado!\033[0m')

    if select == 2:
               print('=~'*20)
               print('        As tags obsoletas são: ')
               print('=~'*20)
               print('Não utilize de forma alguma essas tags,\nelas estão totalmente obsoletas,\
                     \ne causa instabilidade com navegadores.')
               print('=~'*20)
               print(len_arquive.len_arquive('Tags','txt'))
               
               print('=~'*20)

    if select == 3:
        os.remove('Tags.txt')
        web_scraping.w3c_site()
        print('\033[0;32mArquivo atualizado!\033[0m')
        
    if select == 4:
        nome_arquivo = str(input('Digite o nome do seu arquivo html: '))
        a = len_arquive.len_arquive('Tags', 'txt')  
        r = len_arquive.len_arquive(f'{nome_arquivo}', 'html') 
        filtering = filtro_strings.filter_str(a, r)
                
    if select == 5:
         sites = str(input('Digite o site: '))
         html_converter.html(sites)