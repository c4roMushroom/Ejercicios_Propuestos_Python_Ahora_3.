#Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos
#valores fueron pares y cuántos impares. Emplear el operador “%” en la condición de la
#estructura condicional (este operador retorna el resto de la división de dos valores, por
#ejemplo 11%2 retorna un 1):

par = 0
impar = 0  

for x in range(1,11): 
    num = int(input("ingrese un numero: "))

    if num % 2 == 0:
        par = par+1
    else :
        impar = impar+1

print("la cantidad de numeros pares es:",par)
print("la cantidad de numeros impares es:",impar)