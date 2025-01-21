# -*- coding: utf-8 -*-
"""
GENERADOR DE ALEATORIOS ÚNICOS
Genera una lista de números aleatorios sin repetir dentro de un rango especificado.
"""

import random


lista_aleatorios = []

cota_min = int(input("Introduzca el rango mínimo: "))
cota_max = int(input("Introduzca el rango máximo: "))
# num_elementos = int(input("Introduzca el número de elementos de la lista: "))


for i in range (0, num_elementos):
    num_random = random.randint(cota_min, cota_max)
    
    while(num_random in lista_aleatorios):
        num_random = random.randint(cota_min, cota_max)
    
    lista_aleatorios.append(num_random)


print(f"Lista de aleatorios: {lista_aleatorios}")
