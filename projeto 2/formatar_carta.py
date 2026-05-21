def formatar_carta(carta: list, verificacao : bool):
    categorias = [
        'Nome', # String
        'Categoria', # String
        'Títulos', # Int
        'Vitórias', # Int
        'Habilidade', # Int
        'Velocidade', # Int
        'Ataque', # Int
        'Defesa' # Int
        ]
    
    tamanho_carta = 22
    
    if verificacao == True:
        for i in range(len(carta)):
            
            if i == 0:
            
                print(f'|{carta[0] + (' ' * (tamanho_carta - len(carta[0]) - len(carta[1]))) + carta[1]}|')
                
            elif i == 1:
                
                print(f'|{' ' * tamanho_carta}|')
            
            else:
                print(f'|{categorias[i] + (' ' * (tamanho_carta - len(str(carta[i])) - len(categorias[i]))) + str(carta[i])}| [{i-1}]')
                
    else:
        for i in range(len(carta)):
            
            if i == 0:
            
                print(f'|{carta[0] + (' ' * (tamanho_carta - len(carta[0]) - len(carta[1]))) + carta[1]}|')
                
            elif i == 1:
                
                print(f'|{' ' * tamanho_carta}|')
            
            else:
                print(f'|{categorias[i] + (' ' * (tamanho_carta - len(str(carta[i])) - len(categorias[i]))) + str(carta[i])}|')