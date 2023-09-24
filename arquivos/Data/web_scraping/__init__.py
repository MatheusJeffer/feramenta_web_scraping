def w3c_site():
    import requests
    import os
    
    from bs4 import BeautifulSoup
    
    from arquivos.Data import txt_function    

    html_tags_definitive = []
    dev_mozilla_dados = []
    tags_dados = []
    all_tags = []
    tags_definitive = []
    
    mozilla = requests.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Element")
    w3docs = requests.get('https://www.w3docs.com/learn-html/deprecated-html-tags.html')

    conteudo = mozilla.content
    conteudo1 = w3docs.content
    
    dev_mozilla = BeautifulSoup(conteudo,'html.parser')
    w3_docs = BeautifulSoup(conteudo1, 'html.parser')
    
    html_w3_docs = w3_docs.findAll('a')
    html_dev_mozilla = dev_mozilla.findAll('a')

    
    
    

    
    
    for tag in html_w3_docs:
        if tag not in all_tags:  
            all_tags.append(tag.text)
            tags_definitive.append(all_tags[:])
            all_tags.clear()

    for items in html_w3_docs:
         for obsolute in items:
             if obsolute in ('<blink>', '<basefont>', '<applet>', '<isindex>'): 
                 html_tags_definitive.append(obsolute)

    for item in html_tags_definitive:
        if html_tags_definitive.count(item) > 1:
            pos = html_tags_definitive.index(item)
            html_tags_definitive.pop(pos)
             

          


    

    for html_content in html_dev_mozilla:
    
        if html_content.text not in dev_mozilla_dados:
            dev_mozilla_dados.append(html_content.text)
            tags_dados.append(dev_mozilla_dados[:])
            dev_mozilla_dados.clear()
    for dados in tags_dados:
        for tag in dados:
            if tag not in html_tags_definitive:  
                html_tags_definitive.append(tag)
        
    for  html_tags in html_tags_definitive:
         txt_function.tags(html_tags)
    
