import random

def tirar_carta(baralho: list) -> list:
    
    carta = random.choice(list(baralho))
    
    baralho.remove(carta)
    
    return carta, baralho