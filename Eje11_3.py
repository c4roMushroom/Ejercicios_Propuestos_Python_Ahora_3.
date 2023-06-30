#Realizar un programa que lea los lados de n triángulos, e informar:
#a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles
#(dos lados iguales), o escaleno (ningún lado igual)
#b) Cantidad de triángulos de cada tipo.

for x in range(1,6):
    num = int(input("ingresa un numero: "))

    if num % 2 == 0:
        suma = num + num
        print(suma)