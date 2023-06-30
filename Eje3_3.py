#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un
#programa que lea los sueldos que cobra cada empleado e informe cuántos empleados
#cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá
#informar el importe que gasta la empresa en sueldos al personal.

sueldos = []
cont1 = 0
cont2 = 0  

for x in range(1,11): 
    sueld1 = int(input("ingrese su sueldo: "))
    sueldos.append(sueld1)

    if sueld1>=100 and sueld1<=300:
        cont1 = cont1+1
    elif sueld1>300:
        cont2 = cont2+1

suma = 0
for valor in sueldos:
    suma = suma + valor

print("cantidad de empleados que cobran entre $100 y $300:",cont1)
print("cantidad de empleados que cobran más de $300:",cont2)
print("la empresa gasta en sueldos: $",suma)

