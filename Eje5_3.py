#Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.

for mult in range(1,500): 
    if mult % 8 == 0:
        print("los multiplos de 8 son: ",mult)