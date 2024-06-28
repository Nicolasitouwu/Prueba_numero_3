#AGREGAR CATEGORIA
import json

def agregar_categoria(nombre:str):
    with open("biblioteca.json",mode="r") as LECTURA_JSON:
        LEER_JSON = json.load(LECTURA_JSON)
        nueva_categoria = {
            "CategoriaID": len(LEER_JSON["Categoria"])+1,
            "Nombre": nombre
        }
    LEER_JSON["Categoria"].append(nueva_categoria)

    with open("biblioteca.json",mode="w") as ESCRITURA_JSON:
        json.dump(LEER_JSON,ESCRITURA_JSON,indent=4)

####################################################################    

def editar_categoria(BUSCAR_ID:int):
    with open("biblioteca.json", mode="r") as LECTURA_JSON:
        LEER_JSON =json.load(LECTURA_JSON)
        contador = 0
        for i in LEER_JSON["Categoria"]:
            if i ["CategoriaID"] == BUSCAR_ID:
                break
            contador = contador+1
        LEER_JSON["Categoria"][contador]["Nombre"]= input('Ingrese el nuevo nombre para la categoria: ')
    with open("biblioteca.json", mode="w") as ESCRITURA_JSON:
        json.dump(LEER_JSON, ESCRITURA_JSON, indent=4)

####################################################################    

def eliminar_cate(eliminarCAT:int):
    with open("biblioteca.json",mode="r") as LECTURA_JSON:
        LEER_JSON = json.load(LECTURA_JSON)
        contador = 0
        for i in LEER_JSON["Categoria"]:
            if i ["CategoriaID"] == eliminarCAT:
                print(i)
                break
            contador = contador +1
        del LEER_JSON["Categoria"][contador]
    with open("biblioteca.json",mode="w" ) as ESCRITURA_JSON:
        json.dump(LEER_JSON,ESCRITURA_JSON, indent=4)

####################################################################    

def buscar_CATE():
    with open("biblioteca.json", mode="r") as LECTURA_JSON:
        LEER_JSON =json.load(LECTURA_JSON)
        for i in LEER_JSON["Categoria"]:
            print(i)

####################################################################    
