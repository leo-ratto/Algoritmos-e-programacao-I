from formatar_carta import formatar_carta
from media import media
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

medias = media()

def pve(cartas_p1: list, cartas_p2: list, jogador: int) -> tuple[list, list, int]:
    
    print(f'\nNúmero de cartas do Jogador: {len(cartas_p1)}\nNúmero de cartas do Computador: {len(cartas_p2)}')
    
    carta_p1 = cartas_p1[0]
    cartas_p1.remove(carta_p1)
    
    carta_p2 = cartas_p2[0]
    cartas_p2.remove(carta_p2)
    
    rodada = [carta_p1, carta_p2]
    
    if jogador == 1:

        print('\nVez do Jogador')
        
        print(f'\nCarta do Jogador\n')
        formatar_carta(rodada[0], True)
        
        time.sleep(1.8)
    
        atributo = int(input('\nEscolha o atributo da carta: '))
        
        while 1 > atributo > 6:
            
            atributo = int(input('\nValor Inválido\n\nEscolha o atributo da carta: '))
        
        time.sleep(1.8)
    
        print(f'\nCarta do Computador\n')
        formatar_carta(rodada[1], False)
        
        atributo_rodada = categorias[atributo + 1]
        
        time.sleep(1.5)
        
        print(f'\nAtributo escolhido: {atributo_rodada}')
        
        time.sleep(1.5)
        
        print(f'\nValor de {atributo_rodada} do Jogador: {rodada[0][atributo + 1]}\nValor de {atributo_rodada} do Computador: {rodada[1][atributo + 1]}')
        
        time.sleep(1.5)
        
        if rodada[0][atributo + 1] > rodada[1][atributo + 1]:
            print(f'\nVitória do Jogador!')
            
            cartas_p1.extend(rodada)
                
        elif rodada[0][atributo + 1] < rodada[1][atributo + 1]:
            print(f'\nVitória do Computador!')
            
            cartas_p2.extend(rodada)
                
        else:
            print('Empate!')
                        
            cartas_p1.append(rodada[0])
            
            cartas_p2.append(rodada[1])
        
    else:
        print('\nVez do Computador')
        
        print('O Computador está pensando', end='', flush=True)
        
        time.sleep(1)
        
        for i in range(4):
            print('.', end='', flush=True) if i != 3 else print('.', flush=True)
            
            time.sleep(1)
            
        k = []
            
        for i in range(2, 8):
            k.append(carta_p2[i]/medias[i-2])
            
        k_maior = 0
        
        melhor_atributo = 0
        
        for i in range(len(k)):
            if k[i] > k_maior:
                k_maior = k[i]
                
                melhor_atributo = i
                
        print('\nO computador escolheu o atributo')
        
        time.sleep(1)
        
        print(f'\nCarta do Computador\n')
        formatar_carta(rodada[1], False)
        
        time.sleep(1.8)
        
        print(f'\nCarta do Jogador\n')
        formatar_carta(rodada[0], False)
        
        atributo_rodada = categorias[melhor_atributo + 2]
        
        print(f'\nAtributo escolhido: {atributo_rodada}')
        
        time.sleep(1.8)   
        
        print(f'\nValor de {atributo_rodada} do Computador: {rodada[1][melhor_atributo + 2]}\nValor de {atributo_rodada} do Jogador: {rodada[0][melhor_atributo + 2]}')
        
        time.sleep(1.8)
        
        if rodada[0][melhor_atributo + 2] > rodada[1][melhor_atributo + 2]:
            print(f'\nVitória do Jogador!')
            
            cartas_p1.extend(rodada)
                
        elif rodada[0][melhor_atributo + 2] < rodada[1][melhor_atributo + 2]:
            print(f'\nVitória do Computador!')
            
            cartas_p2.extend(rodada)
                
        else:
            print('\nEmpate!')
                        
            cartas_p1.append(rodada[0])
            
            cartas_p2.append(rodada[1])
            
        time.sleep(1.8)
            
    if jogador == 1:
        jogador = 2
        
    else:
        jogador = 1
    
    return cartas_p1, cartas_p2, jogador