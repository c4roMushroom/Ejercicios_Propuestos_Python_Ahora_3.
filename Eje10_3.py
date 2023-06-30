#Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla
#de multiplicar del mismo (los primeros 12 términos)

num = int(input("ingrese un numero del 1 al 10: "))

if num >= 1 and num<=10:
    for x in range(1,13):
        resultado = x*num
        print("la tabla de multiplicar:",x,"x",num,":",resultado)
else:
    print("no es un numero del 1 al 10. Ingrese otro nuevamente")   