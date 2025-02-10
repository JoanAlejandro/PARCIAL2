#Desarrolar un programa que dadas dos listas determine que elemntos tiene la primera lista que la segunda no tenga
def repeticion(lista,lista2):
    contador=0
    for i in range(len(lista)):
        if lista[i] not in lista2:
            print(f"{l1[i]} no esta en la segunda lista", end=". ")
            contador=1
    if contador==0:
        print("Todos los elementos de la lista uno estan en la segunda lista")
l1=["Alejo","Luis","Pedro"]
l2=["Alejo","Luis","Ojo"]
repeticion(l1,l2)