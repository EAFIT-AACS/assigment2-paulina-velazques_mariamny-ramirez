import random

def generar_cadenas_validas(n=3):
    """Genera cadenas válidas siguiendo la gramática de palíndromos."""
    validas = []

    def generar(depth):
        if depth == 0:
            return random.choice(["", "0", "1"])
        else:
            simbolo = random.choice(["0", "1"])
            return simbolo + generar(depth - 1) + simbolo

    for _ in range(n):
        profundidad = random.randint(1, 3)
        validas.append(generar(profundidad))
    return validas

def es_palindromo(cadena):
    return cadena == cadena[::-1]

def generar_cadenas_invalidas(n=3):
    """Genera cadenas inválidas aleatorias que NO sean palíndromos."""
    invalidas = []
    while len(invalidas) < n:
        longitud = random.randint(3, 6)
        cadena = ''.join(random.choice(['0', '1']) for _ in range(longitud))
        if not es_palindromo(cadena):
            invalidas.append(cadena)
    return invalidas