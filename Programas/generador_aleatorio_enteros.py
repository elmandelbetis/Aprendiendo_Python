# -*- coding: utf-8 -*-
"""
GENERADOR DE ALEATORIOS ÚNICOS
Genera una lista de números aleatorios sin repetir dentro de un rango especificado.
"""

import random


lista_aleatorios = []

cota_min = int(input("Introduzca el rango mínimo: "))
cota_max = int(input("Introduzca el rango máximo: "))


while cota_min >= cota_max:
    print("Por favor, introduzca un rango válido.")
    cota_min = int(input("Introduzca el rango mínimo: "))
    cota_max = int(input("Introduzca el rango máximo: "))


for i in range (cota_min, cota_max):
    num_random = random.randint(cota_min, cota_max)
    
    while num_random in lista_aleatorios:
        num_random = random.randint(cota_min, cota_max)
    
    lista_aleatorios.append(num_random)


print("Lista de aleatorios:")
print(lista_aleatorios)
