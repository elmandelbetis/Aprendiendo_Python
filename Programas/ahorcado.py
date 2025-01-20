# -*- coding: utf-8 -*-
"""
JUEGO DEL AHORCADO:
    
El usuario intenta adivinar una palabra letra por letra antes de quedarse 
sin intentos.
"""
import random


# Constantes
intentos_consumidos = 0
num_intentos = 10

with open("../files/lista_ahorcado.txt") as archivo:
    lista_palabras = [linea.strip().lower() for linea in archivo]


palabra = random.choice(lista_palabras)
longitud = len(palabra)

# Creación de una lista para representar el progreso del jugador
progreso = ["_"] * longitud

# Mostrar la palabra oculta inicialmente
print("Palabra:")
print(" ".join(progreso))


while intentos_consumidos < num_intentos and "_" in progreso:
    letra = input("\n\nIntroduzca una letra: ").lower().strip()

    if not letra or len(letra) != 1 or not letra.isalpha():
        print("Por favor, introduce una letra válida.")
        continue
    
    # Verificar si la letra está en la palabra
    if letra in palabra:
        for idx, char in enumerate(palabra):
            if char == letra:
                progreso[idx] = letra
        print("\nCorrecto!")
    else:
        intentos_consumidos += 1
        print(f"\nIncorrecto. Te quedan {num_intentos - intentos_consumidos} intentos.")
    
    
    # Mostrar el progreso actual
    print(" ".join(progreso))
    
    
# Verificar el resultado del juego
if "_" not in progreso:
    print("\nFelicidades, has ganado!!")
else:
    print(f"\nTe has quedado sin intentos. La palabra era: {palabra}")

