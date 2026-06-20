#Condicional múltilple y anidada

#elif (else if) - agrega rams intermedias

#Clasificador de calificaciones

#Tu turno: Agrega  un mensaje que diga cuántos puntos le faltan para subir de letra. 
# Por ejemplo, si obtuvo 7.2 (letra C), necesita 0.8 puntos para llegar a la B.
nota = float(input("Calificacion (0-10): "))

if nota <0 or nota> (10):
    print("Calificacion inválida")
elif nota >= 9.0:
    letra = "A - Excelente"
elif nota >= 8.0:
    letra = "B - Bien"
elif nota >= 7.0:
    letra = "C - Suficiente"
elif nota >= 6.0:
    letra = "D - Aprobacion minima"
else:
    letra = "F - Reprobrado"


if 0<= nota<= 10:
    print(f"Nota: {nota:.1f} -> {letra}")
if nota < 6.0:
    puntos_faltantes = (7.0 - nota)
    print(f"Puntos faltantes {puntos_faltantes:.1f}")

#Tu turno: Reescribe el Ejercicio  usando una sola condición con and 
# en lugar del if anidado. Luego compara las dos versiones: 
# ¿cuál da mensajes de error más específicos y por qué?
#Si no usamos el if anidado como en el segundo ejercicio, es mas complicado para 
# detallar todo el ejercio sin romper tener que romper la  regla de una sola condicion, 
# es decir un if

nota2 = float(input("Calificacion (0-10): "))
APROBACION_MINIMA = 7.0
if 0 < nota2 < 10 and nota2 > APROBACION_MINIMA:
    print("Valor aprobatorio ", nota2)