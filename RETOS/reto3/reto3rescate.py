entrada1 = input().split(' ')
n, m = int(entrada1[0]), int(entrada1[1])

cantidades_iniciales = []
for i in range(n):
    dosis = []
    cantidades_iniciales.append(i)

cantidades_solicitadas = []

cantidades_inventario_final = []

for i in range():
    cantidades_solicitadas.append(i)
    cantidades_inventario_final.append(i)

for i in range(1, n):
    entrada1 = input().split(' ')
    central_medicamentos, ps, pd = int(entrada1[0]), int(entrada1[1]), int(entrada1[2])

    if ps<80 and pd<60:
        cantidades_solicitadas[central_medicamentos-1] += 5
    elif 80<=ps<120 and 60<=pd<80:
        cantidades_solicitadas[central_medicamentos-1] += 0
    elif 120<=ps<130 and 80<=pd<85:
        cantidades_solicitadas[central_medicamentos-1] += 0
    elif 130<=ps<140 and 85<=pd<90:
        cantidades_solicitadas[central_medicamentos-1] += 2
    elif 140<=ps<160 and 90<=pd<100:
        cantidades_solicitadas[central_medicamentos-1] += 5
    elif 160<=ps<180 and 100<=pd<110:
        cantidades_solicitadas[central_medicamentos-1] += 10
    elif ps>=180 and pd>=110:
        cantidades_solicitadas[central_medicamentos-1] += 30
    elif ps>140 and pd<90:
        cantidades_solicitadas[central_medicamentos-1] += 20

for i in range(n):
    cantidades_solicitadas[i]=cantidades_iniciales[i]-cantidades_solicitadas[i]

print(cantidades_inventario_final.index(min(cantidades_inventario_final))+1, min(cantidades_inventario_final))
print(cantidades_inventario_final.index(max(cantidades_inventario_final))-1, max(cantidades_inventario_final))

#TERMINAR LA PROPORCION PORCENTUAL
for i in range(n):
    print(i+1, n+1)



