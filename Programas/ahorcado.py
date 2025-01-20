# -*- coding: utf-8 -*-
"""
JUEGO DEL AHORCADO:
    
El usuario intenta adivinar una palabra letra por letra antes de quedarse 
sin intentos.
"""
import random



i = 0
intentos_consumidos = 0
num_intentos = 10
lista_palabras_posibles = ['Elefante', 'Jirafa', 'Canguro', 'Zorro', 'Cocodrilo', 'Delfin', 'Lobo',
                           'Tortuga', 'Hormiga', 'Manzana', 'Platano', 'Naranja', 'Piña', 'Sandia', 
                           'Cereza', 'Fresa', 'Mango', 'Kiwi', 'Limon', 'Rojo', 'Azul', 'Verde', 'Amarillo',
                           'Purpura', 'Marron', 'Blanco', 'Negro', 'Gris', 'España', 'Mexico', 'Argentina',
                           'Brasil', 'Italia', 'Japon', 'Alemania', 'Canada', 'Rusia', 'Australia', '']
palabra = random.random()
car = input("Introduzca una letra: ")
if (car != palabra[i]):
    intentos_consumidos += 1
else:
    i += 1

