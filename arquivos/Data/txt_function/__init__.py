def tags(tag):
    tag = str(tag)
    tags_vazias = ('<basefont>')
    tags_deprecated = ('<tt>', '<s>', '<strike>', '<plaintext>', '<menu>', '<marquee>', '<noframes>', '<isindex>', '<frameset>', '<frame>', '<font>', '<embed>', '<dir>', '<center>', '<blink>', '<big>', '<acronym>', '<applet>', '<u>', '<nobr>')                                                                                    
    tags_site  = []
        
    with open('Tags.txt', 'a') as archive:
          if tag in tags_deprecated:
             if tag not in tags_site:
               if tag in tags_deprecated:  
                   s = tag.replace('<', '</')
                   tags_site.append(s)
                   archive.write(f'{s}\n')
               if tag == '<basefont>': 
                    archive.write(f'{tag}\n')
                 