# -*- coding: utf-8 -*-
"""
Genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo. 
Proporciona pistas como "mayor" o "menor". Termina cuando el usuario acierte.
"""

import random

num_secreto = random.randint(1, 100)

numero = int(input("Introduzca un número entre 1 y 100: "))

while numero != num_secreto:
    if numero < num_secreto:
        print(f"El número secreto es mayor a {numero}")
        numero = int(input("Introduce otro número: "))
    else:
        print(f"El número secreto es menor a {numero}")
        numero = int(input("Introduce otro número: "))
        
print("FELICIDADES!!")
