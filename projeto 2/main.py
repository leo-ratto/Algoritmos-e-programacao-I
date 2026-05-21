from funcoes import *

import random, time


def main():
    
    baralho = cartas()

    cartas_j1 = [] 
        
    cartas_j2 = []
    
    while len(baralho) != 0:
        cartas_j1.append(tirar_carta(baralho)[0])
        
        cartas_j2.append(tirar_carta(baralho)[0])
        
    jogo = int(input('\nSUPER TRUNFO\n\n[1] Jogador x Computador\n[2] Jogador x Jogador\n\nInsira o modo de jogo: '))
    
    while jogo not in range(1, 3):
        jogo = int(input('\nValor inválido\n\n[1] Jogador x Computador\n[2] Jogador x Jogador\n\nInsira o modo de jogo: '))
    
    if jogo == 2:
        j1 = input('\nInsira o nome do Jogador 1: ')
        
        j2 = input('\nInsira o nome do Jogador 2: ')
        
        primeiro = random.randint(1, 2)
        
        while len(cartas_j1) != 0 or len(cartas_j2) != 0:
            
            primeiro = pvp(cartas_j1, cartas_j2, primeiro, j1, j2)[2]
            
    else:
        primeiro = random.randint(1, 2)
        
        while len(cartas_j1) != 0 or len(cartas_j2) != 0:
            
            primeiro = pve(cartas_j1, cartas_j2, primeiro)[2]
                
if __name__ == "__main__":
    main()