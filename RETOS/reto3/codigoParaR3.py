"""el primer imput que se haga va a capturar DOS datos en una misma linea, 
cantidad de sucursales y cantidad de pacientes separados de un espacio

luego la cantidad de existencias de medicamentos por cada sucursal

luego para cada paciente preguntar: 
en la misma linea 
sucursal sistolica y diastolica"""

#ESTE PRIMERO CUMPLE CON SU OBJETIVO, DE UNA MANERA SECUENCIAL E INTUITIVA.

entrada1=str(input())
lista_entradas = entrada1.split(' ')
lista_entradas[0] = int(lista_entradas[0])
lista_entradas[1] = int(lista_entradas[1])

print(lista_entradas[0])
print(lista_entradas[1])

#ESTE SEGUNDO CODIGO HACE EXACTAMENTE LO MISMO PERO MAS EFICIENTEMENTE.

entrada1 = input().split(' ')
n, m = int(entrada1[0]), int(entrada1[1])

#EJEMPLO DE UN CICLO PARA QUE REPITA ALGO INFINITAMENTE CUANDO NO SEA LO ESPERADO
#En este caso se hace con un numero positivo.
def leer_lista():
    nueva_lista = []
    tamano = int(input('digita la cantidad de elementos: '))

    for i in range(tamano):
        numero = -1

        while numero <= 0:
            numero = int(input('digite un numero entero positivo: '))
        
        nueva_lista.append(numero)
    
    return nueva_lista

print(leer_lista())