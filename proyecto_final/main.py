def suma_lista(lista):
    return sum(lista)

num=0
lista_numeros=[]
while num!=-1:
    num=int(input("Num(-1 para terminar): "))
    if num!=-1:
        lista_numeros.append(num)

suma=suma_lista(lista_numeros)

print("la lista es: ")
print(lista_numeros)
print("Y su suma es: ",suma)
