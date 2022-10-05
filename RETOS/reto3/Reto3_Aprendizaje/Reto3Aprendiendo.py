sucursales = 0
pacientes = int
medicamentos = 0

if sucursales < 1: 
    ingresoDeDatos= input().split(' ')
    sucursales= int (ingresoDeDatos[0])
    medicamentos= int (pacientes[1])

cantidades_Solicitadas= []
cantidades_de_Inventario_Final= []

existencias_Actuales_Medicamento= []

#Leer cantidad de existencias actuales de medicamento desde 1 hasta sucursales#

for i in range (1, sucursales):
    existencias_Actuales_Medicamento= input(i)

#Por cada paciente se debe leer el numero de la sucursal donde sera atendido
# seguido de info de presion sistolica y diastolica#

for i in range (1, sucursales):
    ingresoDeDatos= input().split(' ')
    sitio_de_atencion_paciente, presion_sistolica, presion_Diastolica= int(ingresoDeDatos[0]),
    + int(ingresoDeDatos[1]), int(ingresoDeDatos[1])   
    
#si Sucursales es menor a 1 Leer nuevamente ambos valores hasta
#que se ingrese mas de 1

#ya tengo los tres puntos principales
# -CONTINUAR CON LOS SIGUIENTES DESPUES DE LA TABLA DE 
# COMPARACIONES#