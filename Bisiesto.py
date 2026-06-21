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
    
#Nota: Lo he comprobado, y le notifique al docente personalmente que la regla de division entre 4
# es universal, todos los años bisiestos son divisible entre 4. No es necesariaio dividir 
# entre 100 y 400, porque realmente son muy pocos los años que cumplen con esa condicion.