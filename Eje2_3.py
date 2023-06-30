#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

altC = []

for x in range(1,8): 
    alt = int(input("ingrese su altura: "))
    altC.append(alt)
   
suma = 0
for valor in altC:
    suma = suma + valor

cant = len(altC)
prom = suma//cant
print("la altura promedio es:",prom)








