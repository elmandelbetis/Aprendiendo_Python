# -*- coding: utf-8 -*-
"""
Solicita una frase al usuario y cuenta cuántas palabras contiene.
"""

def contar_palabras(texto):
    contador = 0
    longitud = len(texto)
    
    for i in range(longitud):
        if texto[i] == ' ' and i > 0 and texto[i-1] != ' ':
            contador += 1
            
    if longitud > 0 and texto[-1] != ' ':
        contador += 1
    
    return contador


texto = input("Introduzca un texto: ")
print(f"Número de palabras en el texto: {contar_palabras(texto)}")

