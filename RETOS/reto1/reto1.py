salario_minimo = int(908526)
etnia = str(input())
estrato = int(input())
ingresos = float(input())
etnia_social = int(0)

if (etnia == "sin reconocimiento"):
    etnia_social = 0
elif (etnia == "afrodescendiente"):
    etnia_social = 9
elif (etnia == "indigena"):
    etnia_social = 10
elif (etnia == "raizal"):
    etnia_social = 11
elif (etnia == "palenquero"):
    etnia_social = 12
elif (etnia == "gitano"):
    etnia_social =13
else:
   print("se presento un error")

if (estrato == 1):
    estrato = 15
elif (estrato == 2):
    estrato = 13
elif (estrato == 3):
    estrato = 11
elif (estrato == 4):
    estrato = 7
elif (estrato == 5):
    estrato = 0
elif (estrato == 6):
    estrato = 0 
else:
   print("se presento un error")

if (ingresos < salario_minimo):
    ingresos = 20
elif (ingresos >= salario_minimo and ingresos < salario_minimo * 2):
    ingresos = 14
elif (ingresos >= salario_minimo * 2 and ingresos < salario_minimo * 4):
    ingresos = 12
elif (ingresos >= salario_minimo * 4 and ingresos < salario_minimo * 5):
    ingresos = 9
else:
    ingresos = 0

if(etnia_social + estrato + ingresos < 30):
    print("el candidato no continua en el proceso de seleccion")
elif (etnia_social + estrato + ingresos >= 30):
    print("el candidato continua en el proceso de seleccion")