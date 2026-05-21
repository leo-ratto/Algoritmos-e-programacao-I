from formatar_carta import formatar_carta
import time

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

def pvp(cartas_p1: list, cartas_p2: list, jogador: int, p1: str, p2: str) -> tuple[list, list, int]:

    if jogador == 1:
        primeiro = p1
        
        segundo = p2
        
    else:
        primeiro = p2
        
        segundo = p1

    print(f'\nNúmero de cartas de {p1}: {len(cartas_p1)}\nNúmero de cartas de {p2}: {len(cartas_p2)}')
    
    carta_p1 = cartas_p1[0]
    cartas_p1.remove(carta_p1)
    
    carta_p2 = cartas_p2[0]
    cartas_p2.remove(carta_p2)
    
    rodada = [carta_p1, carta_p2]
    
    monte = [carta_p1, carta_p2]
    
    print(f'\nVez de {primeiro}')
    
    time.sleep(1)
    
    _ = input(f'\nPrecione Enter para revelar a carta de {primeiro}')
    
    print(f'\nCarta de {primeiro}\n')
    formatar_carta(rodada[jogador-1], True)
    
    time.sleep(1.8)
    
    atributo = int(input('\nEscolha o atributo da carta: '))
    
    while atributo < 1 or atributo > 6:
        
        atributo = int(input('\nValor Inválido\n\nEscolha o atributo da carta: '))
        
    time.sleep(1.8)
    
    print(f'\nCarta de {primeiro}\n')
    formatar_carta(rodada[jogador-1], False)
    
    vez = rodada[jogador-1]
    
    rodada.pop(jogador-1)
    
    time.sleep(1.8)
    
    print(f'\nCarta de {segundo}\n')
    formatar_carta(rodada[0], False)
    
    atributo_rodada = categorias[atributo + 1]
    
    time.sleep(1.5)
    
    print(f'\nAtributo escolhido: {atributo_rodada}')
    
    time.sleep(1.5)
    
    print(f'\nValor de {atributo_rodada} de {primeiro}: {vez[atributo + 1]}\nValor de {atributo_rodada} de {segundo}: {rodada[0][atributo + 1]}')
    
    time.sleep(1.5)
    
    if vez[atributo + 1] > rodada[0][atributo + 1]:
        print(f'\nVitória de {primeiro}!')
        
        if primeiro == p1:
            
            cartas_p1.extend(monte)
            
        else:
            
            cartas_p2.extend(monte)
            
    elif vez[atributo + 1] < rodada[0][atributo + 1]:
        print(f'\nVitória de {segundo}!')
        
        if primeiro == p1:
            
            cartas_p2.extend(monte)
            
        else:
            
            cartas_p1.extend(monte)
            
    else:
        print('\nEmpate!')
                    
        cartas_p1.append(monte[0])
        
        cartas_p2.append(monte[1])
        
    if jogador == 1:
        jogador = 2
        
    else:
        jogador = 1
    
    return cartas_p1, cartas_p2, jogador