def len_arquive(arquivo, type):
    with open(f'{arquivo}.{type}', 'r', encoding='utf=8') as archive:
    
        return archive.read()