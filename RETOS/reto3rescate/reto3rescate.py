lista = []
#lista
# lista=[1,2,3,4,5,6,7,8,9,10]

#¿Cómo se rellena una lista?
n=3
for i in range(n):
    #para llamar la lista se usa .append(valor)
    valor = int(input())
    lista.append(valor)
print(lista)


#para hallar un maximo y minimo de una lista 
# el minimo min()
# el maximo max()
minimo = min(lista)
maximo = max(lista)
#para sumar un vector en su respectiva posicion
suma=lista[0] + 1
print(suma)
print(minimo, maximo)
