from cartas import cartas
from statistics import mean

def media() -> list:
    baralho = cartas()
    
    categoria = []
    
    medias = []
    
    for i in range(2, 8):
        
        for j in range(len(baralho)):
            
            categoria.append(baralho[j][i])
            
        medias.append(mean(categoria))
    
        categoria.clear()
        
    return medias