# -*- coding: utf-8 -*-
"""
SISTEMA DE REGISTRO DE ESTUDIANTES
Permite agregar, eliminar y listar estudiantes, con información como nombre, 
edad y calificaciones.
"""


def aniadir_estudiante(l):
    nombre = input("Inserte nombre del estudiante: ")
    edad = int(input("Inserte la edad del estudiante: "))
    
    calificaciones = []
    datos_estudiante = {(nombre, edad): calificaciones}
    
    l.update(datos_estudiante)


def aniadir_calificaciones(l, nombre):
    for clave, calificaciones in l.items():
        if clave[0] == nombre:
            print(f"Estudiante encontrado: {clave}")
            nota = 0
            while nota != -1:
                nota = float(input("Inserte calificación (-1 para finalizar): "))
                if nota != -1:
                    calificaciones.append(nota)
            print(f"Calificaciones actualizadas: {calificaciones}")
            return
    
    print("Estudiante no encontrado.")


def eliminar_estudiante(l, nombre):
    for clave in list(l.keys()):
        if clave[0] == nombre:
            del l[clave]
            print(f"Estudiante {nombre} eliminado")
            return
    
    print("Estudiante no encontrado.")


def mostrar_menu():
    print("\nSISTEMA DE REGISTRO DE ESTUDIANTES")
    print("1- Insertar estudiante")
    print("2- Añadir calificaciones")
    print("3- Eliminar estudiante")
    print("N- Salir")



lista_estudiantes = {}

mostrar_menu()
car = input("Elija una opción (1/2/3/N)?: ")

while car not in ['n', 'N']:
    if car == '1':
        aniadir_estudiante(lista_estudiantes)
    elif car == '2':
        al = input("Escriba el alumno a actualizar: ")
        aniadir_calificaciones(lista_estudiantes, al)
    elif car == '3':
        al = input("Escriba el alumno a eliminar: ")
        eliminar_estudiante(lista_estudiantes, al)
    else:
        print("Por favor, seleccione una opción válida.")
    
    mostrar_menu()
    car = input("Elija una opción (1/2/3/N)?: ")


print("Saliendo...")
