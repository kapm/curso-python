print("Bienvenido al ahorcado")
print("comencemos")
print("Presiona cualquier tecla para continuar")
input()
palabra_secreta="python"
oportunidades=10
letras_correctas=[]
restantes=[]

for letra in palabra_secreta:
    if letra not in restantes:
        restantes.append(letra)

def mostrar_casillas(correctas):
    for letra in palabra_secreta:
        if letra in correctas:
            print(letra,end="")
        else:
            print(" _ ", end ="")
    print("\n")



while oportunidades>0 and len(restantes)>0:
    mostrar_casillas(letras_correctas)
    adivinanza=input("Adivina una letra: ")
    if adivinanza in palabra_secreta:
        letras_correctas.append(adivinanza)
        restantes.remove(adivinanza)
    else:
        oportunidades-=1
    print("Te quedan ",oportunidades)

if len(restantes)==0:
    print("Ganaste!")
else:
    print("Perdiste")


'''palabra="cuadro"
letra=""
palabra_adivinada=[]

#pedir a usuario que adivine
def preguntar_letra(letra):
    while palabra!=palabra_adivinada:
        letra=input("Adivina una letra: ")
        if letra in palabra:
            print("adivinaste una letra!")
            letra_adivinada(letra)
        else:
            print("vuelve a intentar:")
    return letra

def letra_adivinada(letra):
    i=0
    while letra in palabra[i]:
        palabra_adivinada.append(letra)
    

print("Comenzar ahorcado")
print("_"*len(palabra))
preguntar_letra(letra)'''