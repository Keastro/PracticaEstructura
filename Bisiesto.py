#Tu turno: Crea una condicion que verifique si un año es bisiesto.
# Un año es bisiesto si es divisible entre 4.
# También si es divisible entre 100, y entre 400. Pista: usa el operador % (módulo).
año = int(input("Ingresa un año: "))
divisible = año // 4 
tiempo_anual = divisible * 4

if tiempo_anual == año :
    print("Es bisiesto")
else:
    print("No es bisiesto")
#if int(dias_year / 4) and dias_year / 100:
    #print("")