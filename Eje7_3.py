#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la
#medida de la base y la altura de un triángulo. El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.

#base = []
#alt = []

for x in range(1,4): 
    print("triangulo",x)
    bases = int(input("ingrese la base del triangulo: "))
    alts = int(input("ingrese la altura del triangulo: "))
    supf = bases*alts/2

    def leer():
        print("el triangulo",x)
        print("su base es:",bases)
        print("su altura es:",alts)
        print("su superficie es:",supf)
    
cont1 = 0

if supf>12:
    cont1 = cont1+1

leer()
print("la cantidad de triangulos que tiene una superficie>12 es:",cont1)

#no pude solucionarlo:(