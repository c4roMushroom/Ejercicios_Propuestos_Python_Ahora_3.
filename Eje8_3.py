#Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los
#últimos 5 valores ingresados.

nums = []

for x in range(1,11): 
    num = int(input("ingrese un numero: "))
    nums.append(num)

suma = 0
for valor in nums[5:11]:
    suma = suma + valor

print("la suma de los ult. valores ingresados es:",suma)