# Ingresando los valores de la cantidad de sucursales (n) y la cantidad de pacientes (m)
linea= input().split(' ')
*** , *** = (int(linea[***]), int(****)

c= []  # Vector de cantidades iniciales
*** i in range(***):
  d= ***
  c.append(***)

# Inicializando Vector para cantidades solicitada
b= []
# Inicializando vector para cantidades de inventario final
d= []

for i in ***:
  b.append(0) 
  d.*** 


for *** in range(***):
  linea= input().split(' ')
  # Ingresando la sucursal o central de medicamentos y las presiones sistolica y diastolica por paciente
  central, ps, pd= (int(linea[***]), int(linea[1]), int(***)

  if ps<83 and pd<48:
    b[central-1] += ***
  elif 83<=ps<124 and 48<=pd<66:
    b[central-1] += 0
  elif ************ :
    b[central-1] += 0
  elif 141<=ps<158 and 83<=pd<97:
    ******
  elif ************ :
    b[central-1] += 6
  elif 186<=ps<197 and 112<=pd<128:
    ******
  elif ************:
    b[central-1] += 30
  elif 159<=ps and 94<pd:
    ******

# Obteniendo las cantidades del inventario final, restando las cantidades iniciales menos las cantidades solicitadas
for i in range(n):
  d[i]= c[***] - b[***]


# Minimo y maximo
print(d.index(min(d))+1, min(d))
print(***, ***)

# Central por porcentaje solicitadas/iniciales
for i in range(n):
  # Generar salida por cada sucursal con proporción porcentual de existencia solicitada sobre las iniciales
  print(i+1, ***)