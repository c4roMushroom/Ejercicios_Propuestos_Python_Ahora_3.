#Se cuenta con la siguiente información: las edades de 5 estudiantes del turno mañana.
#Las edades de 6 estudiantes del turno tarde Las edades de 11 estudiantes del turno noche.
#Las edades de cada estudiante deben ingresarse por teclado. Obtener el promedio de las edades de cada turno (tres promedios)
#Imprimir dichos promedios (promedio de cada turno)
#Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un
#promedio de edades mayor.

edadM = []
edadT = []
edadN = []

print("Turno de la mañana____________________________")
for x in range(1,6):
    mañana = int(input("ingrese su edad: "))
    edadM.append(mañana)

print("Turno de la tarde_____________________________")
for x in range(1,7):
    tarde = int(input("ingrese su edad: "))
    edadT.append(tarde)

print("Turno de la noche_____________________________")
for x in range(1,12):
    noche = int(input("ingrese su edad: "))
    edadN.append(noche)

def prom(prome):
    suma = 0
    for valor in prome:
        suma = suma + valor

    cant = len(prome)
    pro = suma//cant
    return pro

promM = prom(edadM)
promT = prom(edadT)
promN = prom(edadN)

print("promedios de cada turno______________________________\n")
print("el promedio de las edades de la mañana:",promM)
print("el promedio de las edades de la tarde:",promT)
print("el promedio de las edades de la noche:",promN)
print()
print("Turno con el mayor promedio_______________________")
if promM > promT and promM > promN:
    print("turno de la mañana")
elif promT>promN:
    print("turno de la tarde")  
elif promM == promT:
    print("el turno de la mañana y la tarde")
elif promM == promN:
    print("el turno de la mañana y la noche")
elif promT == promN:
    print("el turno de la tarde y la noche")
else:
    print("turno de la noche")  

