
#Gerardo, inicializo la listaglobal de biblioteca como canciones=[]
#después creo una función para crear diccionario

#función que lee el archivo que lee biblioteca y crea la lista del diccionario
from os import system
bd=open("biblioteca.txt","r")
biblioteca_musica=[]
for linea in bd:
    valores=linea.strip().split("|")
    diccionario_canciones={
        "ID":valores[0],
        "Artista":valores[1],
        "Canción":valores[2],
        "Duración":valores[3],
        "Link":valores[4]
    }
    biblioteca_musica.append(diccionario_canciones)

def ver_biblioteca():
    print(biblioteca_musica)

def clear_console():
    system("clear")

def crear_cancion():
    clear_console()
    nuevo_id=input("ID de la canción:")
    id_existente=False
    for valores in biblioteca_musica:
        if nuevo_id==valores["id"]:
            id_existente=True
    if id_existente ==True:
        print("El id existe")
        input("presiona cualquier tecla para continuar")
    else:
        nombre_cancion=input("nombre:")
        artista=input("artista)")
        duracion=input("duracion")
        link=input("link")
        nueva_cancion= {
            "id":nuevo_id,
            "nombre_cancion":nombre_cancion,
            "artista":artista,
            "duración":duracion,
            "link":link
        }
        biblioteca_musica.append(nueva_cancion)
        print("Tu cancion se creo con exito")
        input("Presiona cualquier tecla para continuar")
    #pedir nuevo ID
    #VEr si ya existe en la lista el ID (puede ser con banderas, true, false)
    #nombre,artista duracion link
    #crearla como diccionario
    #agregar el diccionario a la lista

def eliminar_cancion():
    clear_console()
    id_a_eliminar=input("ID de la canción a eliminar:")
    id_existente=False
    for valores in biblioteca_musica:
        if id_a_eliminar==valores["id"]:
            id_existente=True
    if id_existente ==True:
                
    else:
        ""
        biblioteca_musica.append(nueva_cancion)
        print("Tu cancion se creo con exito")
        input("Presiona cualquier tecla para continuar")

def mostrar_menu():
    print("{}Menú de opciones{}".format("-"*5,"-"*5))
    print("1. Ver biblioteca")
    print("2. Ver canción por ID")
    print("3. Crear canción")
    print ("4. Eliminar canción por ID")
    print("5. TERMINAR")
    print("-"*25)
    opc=input("Opción: ")
    return opc

def guardar_cambios():
    archivo_de_texto=open("biblioteca.txt","w")
    for cancion in biblioteca_musica:
        cancion_str=("{}|{}|{}|{}|{}".format(cancion["id"],cancion["artista"],cancion["nombre_cancion"],cancion["duracion"],cancion["link"]))
        archivo_de_texto.write(cancion_str)
        archivo_de_texto.write("?n)")
        print("se guardaron los cambios")
    
opcion_elegida=0
while opcion_elegida!="5":
    opcion_elegida=mostrar_menu()
    if opcion_elegida=="1":
        ver_biblioteca()
    elif opcion_elegida=="2":
        print("ver_cancion_id()")
    elif opcion_elegida=="3":
        crear_cancion()
    elif opcion_elegida=="4":
        print("eliminar_cancion()")
    elif 
print("Bye")
