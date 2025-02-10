#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales
def prom(Arreglo):
    s=0
    for x in Arreglo:
        s+=x
    promedio=s/len(Arreglo)
    return promedio
print(prom({5,10,15,20,25}))

