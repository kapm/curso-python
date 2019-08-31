
bd=open("biblioteca.txt","r")
canciones=[]
for linea in bd:
        canciones=linea.strip().split("|")
        diccionario_canciones={
            "ID":canciones[0],
            "Artista":canciones[1],
            "Canción":canciones[2],
            "Duración":canciones[3],
            "Link":canciones[4]
        }

def ver_biblioteca():

    for linea in bd:
        canciones=linea.strip().split("|")
        print (canciones)

'''def ver_cancion_id():
    bd=open("biblioteca.txt","r")
    cancion ="0"
    for linea in bd:
        canciones=linea.strip().split("|")
        if cancion=input'''

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
    
opcion_elegida=0
while opcion_elegida!="5":
    opcion_elegida=mostrar_menu()
    if opcion_elegida=="1":
        ver_biblioteca()
    elif opcion_elegida=="2":
        print("ver_cancion_id()")
    elif opcion_elegida=="3":
        print("crear_cancion()")
    elif opcion_elegida=="4":
        print("eliminar_cancion()")
print("Bye")
