#Programa que determine si en una lista hay elementos repetidos
lista1=[1,2,3,4,8]
lista2=[1,2,3,4,3]
def repeticion(lista):
    contador=0
    for i in range(len(lista)):
        x = lista.count(lista[i])
        if x>1:
            print("hay elementos repetidos")
            contador=1
            break
    if contador==0:
        print("no hay elementos reptidos")      
print(f"La lista 1 es {lista1}")
print(f"La lista 2 es {lista2}")
print(f"En la primer lista: ")
repeticion(lista1)
print(f"En la segunda lista: ")
repeticion(lista2)