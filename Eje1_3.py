#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

x=1
conti = 0
contM = 0
contm = 0

for x in range(1,11):

   x=x+1
   nota = float(input("ingrese su nota: "))
   if nota > 7:
      contM = contM +1
   elif nota <7:
      contm = contm+1
   else:
      conti = conti+1

print()
print("las notas mayores a 7 son: ", contM)
print("las notas menores a 7 son: ", contm)
print("las notas iguales a 7 son: ", conti)