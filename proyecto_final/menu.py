def imprimir_nombre():
    nombre=input("DAme un nombre: ")
    print(nombre)

def listar_del_1_al_100():
    print(list(range(1,101)))

def imprimir_asteriscos():
    print("*"*1000)

def numero_par_impar():
    n=int(input("Dame un numero:"))
    if n%2==0:
        print("Número Par")
    else:
        print("número impar")

def mostrar_menu():
    print("{}Menu{}".format("*"*10,"*"*10))
    print("1. Imprimir nombrre")
    print("2. Lista del 1 al 100")
    print("3. Imprimir 1000 asteriscos")
    print ("4. Encontrar si un número es par o impar")
    print("5. TERMINAR")
    print("*"*25)
    opc=input("Opción: ")
    return opc
    
opcion_elegida=0
while opcion_elegida!="5":
    opcion_elegida=mostrar_menu()
    if opcion_elegida=="1":
             imprimir_nombre()
    elif opcion_elegida=="2":
        listar_del_1_al_100()
    elif opcion_elegida=="3":
        imprimir_asteriscos()
    elif opcion_elegida=="4":
        numero_par_impar()
print("Bye")
