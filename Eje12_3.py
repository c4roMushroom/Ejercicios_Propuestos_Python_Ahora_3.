#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 15.
#d) El valor acumulado de los números ingresados que son pares.

contN = 0
contP = 0
contM = 0
valors = []

for x in range(1,11):
    valor = int(input("ingrese un valor entero: "))
    valors.append(valor)

    if valor < 1:
        contN = contN + 1
    elif valor >= 1:
        contP = contP + 1
    elif valor % 15 == 0: #falla
        contM = contM + 1
    
suma = 0
for z in valors: 
    if z % 2 == 0:
        suma = suma + z

print("Cantidad de valores negativos:", contN)
print("Cantidad de valores positivos:", contP)
print("Cantidad de multiplos de 15:", contM)
print("Valor acumulado de numeros pares:", suma)