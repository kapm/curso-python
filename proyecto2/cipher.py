# Pedir palabra secreta
def pedir_palabra():
    palabra_secreta=input("palabra secreta:")
    return(palabra_secreta)

#Eliminar letras repetidas
def obtener_key(palabra_secreta):
    key=""
    for letra in palabra_secreta:
        if letra not in key:
            key+=letra
    return(key)

#crear alfabeto
def crear_alfabeto_real(key):
    alfabeto_real=list("abcdefghijklmnñopqrstuvwxyz")
    alfabeto_secreto=list(key)
    return(alfabeto_real,alfabeto_secreto)

def crear_alfabeto_secreto(alfabeto_real):
    for letra in alfabeto_real:
        if letra not in alfabeto_secreto:
            alfabeto_secreto.append(letra)
    return(alfabeto_secreto)

#crear diccionario que mapee
def crear_diccionario(alfabeto_real,alfabeto_secreto):
    cipher={}
    indice=0
    for letra in alfabeto_real:
        cipher[letra]=alfabeto_secreto[indice]
        indice += 1
    return cipher

def encriptar_mensaje(mensaje,cipher):
    mensaje_encriptado=""
    for letra in mensaje:
        if letra==" ":
            mensaje_encriptado+=" "
        else:
            mensaje_encriptado += cipher[letra]
    print(mensaje_encriptado)

def desencriptar_mensaje(mensaje_encriptado):
#crear key
#crear diccionario
#desencriptar con el diccionario que acaba de desencriptor
#return mensaje desencriptado
diccionario_desencriptar={}
for key in cipher:
    diccionario_desencriptar[cipher[key]]=key
mensaje_original=""
for letra in mensaje_encriptado:
    if letra==" ":
        mensaje_original+=" "
    else:
        mensaje_original+= diccionario_desencriptar[letra]
print(mensaje_original)



#Menú
def mostrar_menu_y_capturar():
    print("1. Encriptar mensaje")
    print("2. Desencriptar")
    print("3. Salir")
    return input("opcion")

opcion=mostrar_menu_y_capturar()

if opcion=="1":
    print("encriptar mensaje")
    palabra_secreta=pedir_palabra()
    key=obtener_key(palabra_secreta)
    alfabeto_real=crear_alfabeto_real(key)
    alfabeto_secreto=crear_alfabeto_secreto(alfabeto_real)
    cipher=crear_diccionario(alfabeto_real,alfabeto_secreto)
    mensaje=input("Escribe mensaje para incriptar: ")
    encriptar_mensaje(mensaje,cipher)
    
elif opcion=="2":
    
    #Pedir mensaje encriptado
    #pedir palabra secreta
    #desencriptar mensaje
    #mostrar
else:
    pass