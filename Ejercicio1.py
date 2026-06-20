# Python usa la sangría (espacios al inicio de la línea)
# para delimitar bloques de código. {}, Python usa 4 espacios por nivel
#Esta es la diferencia visual más importante entre python y otros lenguajes

#if condition:

#instruccion1
#else:
#        instruccion2 
# Toda estructura de control termina su primera línea con dos puntos ':'. Los dos
# puntos le dice a Python : el bloque de esta estructura comienza en l asiguiente
# línea. Si se omiten, Python genera SyntaxError: expected ':'

#= asignar un valor
#== comparar dos valores igual que
#!= Diferente de
# > Mayor que / >= mayor o igual
# < Menor que / <= Menor o igual
# and Ambas condiciones True / or al menos una es true / not Negacion lógica

#IF ejecuta un bloque únicamente si la condición es True. Si la condición es False,
#el bloque se salta por completo y el programa continúa. Solo tiene una rama posible.

#Si condiciones Entonces
#   Instrucción
#Fin Si
#   Si FALSE -> SE OMITE EL BLOQUE

#Condicion simple

nota = 8.5

if nota >= 6.0:
    print("El alumno aprobó")

print("Fin del programa")

#condicion doble - if/ else
#El else garantiza que siempre se ejecuta algo. Sin importa si la condicion es true
# o false, el programa toma uno de los dos caminos. Nunca quedan casos sin respuesta

CALIFICACION_MINIMA = 7.0

nota = float(input('Ingresa tu calificación'))

if nota>= CALIFICACION_MINIMA:
    print(f'Aprobado con {nota:.1f}')
else:
    print(f"Reprobado con {nota:.1f}")
    faltaron = CALIFICACION_MINIMA - nota
    print(f'Te faltaron {faltaron:.1f} puntos para aprobar')


#Condiciones compuestas: and / or en accion
edad = int(input('Tu edad: '))
tiene_ine = input("Tienes INE (si/no): ")

if edad>= 18 and tiene_ine == "si":
    print("Puedes votar")
else:
    print("NO puedes votar aun")

#Validación de rango con "and" or input
califacion = float(input("Calificacion (0-10) "))
if califacion <0 or califacion>10:
    print("Califiación fuera de rango")
else:
    print(f"Calificación registrada {califacion:.1f}")
