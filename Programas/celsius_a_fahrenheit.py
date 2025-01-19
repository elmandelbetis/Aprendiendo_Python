# -*- coding: utf-8 -*-
"""
Convierte grados Celsius a Fahrenheit y viceversa.
"""

def cel_to_fahr(grados_celsius):
    return grados_celsius * 9/5 + 32

def mostrar_menu():
    print("------------------------------------------")
    print("CONVERTIDOR GRADOS CELSIUS A FAHRENHEIT")
    print("------------------------------------------")

car = 's'

while (car != 'N' and car != 'n'):
    mostrar_menu()
    
    if car != 's' and car != 'S' and car != 'n' and car != 'N':
        print("Opción inválida. Pruebe otra vez.\n")
    else:
        grados = float(input("Introduzca un número de grados determinado: "))
        print(f"Grados Fahrenheit: {cel_to_fahr(grados)}")
        mostrar_menu()
        car = input("Continuar (S/N)?: ")
    
print("Adiós")
