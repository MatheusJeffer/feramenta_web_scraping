def filter_str( item1, item2):
    tags_txt = []     
    tags_site = []
    tags_site_formating = []
    tags_obsoltas_quan = 0

    item1 = str(item1)
    item2 = str(item2)
    tags_txt.append(item1.split())
    
                 
            
    l = item2.replace('>', '\n')

    r = l.replace(' ', '\n')
    tags_site.append(l.split())
      
    
    for  tags in tags_site:
       for tag in tags:
               tag = str(tag)
               if tag.count('<') == 1:
 
                    tags_site_formating.append(f'{tag}>')
        
               if tags_site_formating.count(f'<{tag}>') > 1:
                     pos = tags_site_formating.index(f'<{tag}>')
                     tags_site_formating.pop(pos)
      
    for  itens in tags_txt:
      for item in itens:
            for  tag_obsolute in tags_site_formating:
                   if tag_obsolute == item: 
                        tags_obsoltas_quan += 1
                        print( tag_obsolute)
    print(f'Você usou {tags_obsoltas_quan} tags obsolutas.')       
