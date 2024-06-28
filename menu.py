#MENU DE FUNCIONES
import json
import funciones
import os
import datetime

def menu():

    print('************************')
    print('*     MUNDO LIBRO      *')
    print('************************')
    print()
    print('[1] - MANTENEDOR DE CATEGORIAS')
    print('[2] - REPORTES')
    print('[3] - SALIR')
    global opc

    opc = int(input('Ingrese la opción que desea: '))

    if opc == 1:
         
            print('*************************')
            print('* MANTENEDOR CATEGORIAS *')
            print('*************************')
            print()
            print('[1] - Agregar Categoria.')
            print('[2] - Editar categoria.')
            print('[3] - Eliminar Categoria.')
            print('[4] - Buscar Categoria.')
            print('[5] - Volver.')

            opc2 = int(input('Ingrese la opción que desea: '))

            if opc2 == 1:
                categoria_new=input('Ingrese el nombre de la nueva categoria: ')
                funciones.agregar_categoria(nombre=categoria_new)
                print('¡Cambio realizado con exito!')

            if opc2 == 2:
                funciones.editar_categoria(int(input('Ingrese el dato que desea editar: ')))
                print('¡Nombre editado de manera exitosa!')

            if opc2 == 3:
                funciones.eliminar_cate(int(input('Ingrese el ID a eliminar: ')))
                print('¡Categoria eliminada con exito!')

            if opc2 == 4:
                funciones.buscar_CATE()
            
            else:
                print('Regresando al menú anterior...')
                print()
                menu()    
    if opc == 2:
        print()
        print('************************')
        print('*     REPORTES         *')
        print('no me lo sé profe 😭😭😢😭😭😢😭😭😭😭😭😭😭')
        print('************************') 
        print()

    if opc == 3:
        print('Salir.\n¡Hasta luego!')  
        print()

menu()




