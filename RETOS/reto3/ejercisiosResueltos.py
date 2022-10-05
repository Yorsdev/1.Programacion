def numpares(cadena):

    contador = 0
    for c in cadena:
        digito=int(c)
        if digito % 2 == 0:
            contador += 1
    return contador

num = int(input('digite un numero: '))
cadena = str(num)
print('el numero de digitos pares es: ', numpares(cadena))


