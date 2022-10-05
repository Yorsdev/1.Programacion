salario_minimo = int(908526)
etnia_social = int(0)
total_usuario = int
contador = 1
c_becarios = 0
c_sinreconocimiento = 0
c_afrodescendiente = 0
c_indigena = 0
c_raizal = 0
c_palenquero = 0
c_gitano = 0
c_etnia = 0

cantidad_personas = int(input())

while (contador <= cantidad_personas):
        etnia = str(input())
        estrato = int(input())
        ingresos = float(input())

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
                contador += 1
                continue

        if (etnia == "sin reconocimiento"):
                etnia_social = 0
                c_sinreconocimiento += 1
        elif (etnia == "afrodescendiente"):
                etnia_social = 1
                c_afrodescendiente += 1
        elif (etnia == "indigena"):
                etnia_social = 10
                c_indigena += 1
        elif (etnia == "raizal"):
                etnia_social = 11
                c_raizal += 1
        elif (etnia == "palenquero"):
                etnia_social = 12
                c_palenquero += 1
        elif (etnia == "gitano"):
                etnia_social =13
                c_gitano += 1
        else:
                contador += 1
                continue 
                    
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

        total_usuario = estrato + etnia_social + ingresos
        total_usuario += 1
        contador += 1
        
        if (total_usuario >= 30 and c_sinreconocimiento >= 1):                
                c_becarios += 1
        elif (total_usuario >= 30 and c_afrodescendiente >= 1):
                c_becarios += 1
        elif (total_usuario >= 30 and c_indigena >= 1):
                c_becarios += 1
        elif (total_usuario >= 30 and c_raizal >= 1):
                c_becarios += 1
        elif (total_usuario >= 30 and c_palenquero >= 1):
                c_becarios += 1
        elif (total_usuario >= 30 and c_gitano >= 1):
                c_becarios += 1
       
print(c_becarios)
print("sin reconocimiento", c_sinreconocimiento)
print("afrodescendiente", c_afrodescendiente)
print("indigena", c_indigena)
print("raizal", c_raizal)
print("palenquero", c_palenquero)
print("gitano", c_gitano)