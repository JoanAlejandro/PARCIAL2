#Desarrollar un programa que determine la mediana de un arreglo de enteros
def Mediana(Arreglo):
    lista=list(Arreglo)
    lista.sort()
    if ((len(lista)% 2) == 0):
        x=int((len(lista)/2)-1)
    else:
        x=int((len(lista)/2))
    print(lista[x])
A1={4,5,6,1,2,3,7,8,9,10}
A2={50,1,100}
Mediana(A1)
Mediana(A2)