
#Ejercicio: for con enumarate(): indice y valor juntos.
#enumarete() te da la posicion y el valor en cada iteracion. Muy util reporter numerados.
#CICLO FOR// Repite un bloque para cada elemento de una secuencia. 
#Se usa cuando sabes de antemano cuantas veces repetir o cuando quieres recorrer
#los elementos de una lista, rango, o cadena.

#Ejercicio: variante de range()
#range(fin) - empieza en 0, termina antes del fin
print("range(5)")

for i in range(5):
    print(i, end=" ")
print()

#range(inicio, fin)- desde el inicio hasta fin.
print("range(1,6): ")
for i in range(1,6):
    print(i, end = ' ')
print()

#range(inicio, fin, paso) - paso personalizado
print("Pares del 0 al 10: ")
for i in range(0, 11, 2):
    print(i, end =' ')
print()

#cuenta regresiva con paso negativo
print("Cuenta regresiva: ")
for i in range(5,0,-1):
    print(i, end=" ")
    print("¡Despegue!")

#Tu turno: escribe un for que impida solo los múltiplos de 3 entre 3 y 30 usando range).
#NO USE IF DENTRO DEL FOR.
print("Números multiplos de 3: ")
for i in range(3,31,3):
    print(i, end=" ")
print()

#Ejercicio - for recorriendo una lista: promedio y conteo.
#El for no solo funciona con números. Puede recorrer cualquier y acumular resultados.

calificaciones = [8.5, 9.0, 6.5, 10.0, 7.5, 5.0, 8.0]

print("Calificaciones del grupo: ")
for calificacion in calificaciones:
    print(f"{calificacion:.1f}")

total = 0
aprobados = 0

reprobados = len(calificaciones) - aprobados

#Turno: encuentra e imprime la calificacion mas alta y la mas baja. Necesitaras
#dos variables
calificacion_alta = calificaciones[0]
calificacion_baja = calificaciones[0]

for calificacion in calificaciones:
    total = total + calificacion
    if calificacion >= 6.0:
        aprobados = aprobados + 1
    if calificacion > calificacion_alta:
        calificacion_alta = calificacion
    if calificacion < calificacion_baja:
        calificacion_baja = calificacion

promedio = total / len(calificaciones)

print(f"\nPromedio del grupo: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")  
print(f"Calificacion mas alta {calificacion_alta}")  
print(f"Calificacion mas baja {calificacion_baja}")  
print()
#-----------------------------
alumnos = ["Iran", 'Povedano', 'Gissel', 'Susana', 'Zeus', 'Carlos', 'Sulub']
notas = [9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 9.8]

#encabezado de la tabla

print(f'{'No. ':<5} {'Alumno ':<12} {'Nota':>6} {'Estado ':<10}')
print('-'*37)

grupal = 0
pasaron = 0

for i, alumno in enumerate(alumnos):
    nota = notas[i]
    estado = 'Aprobado' if nota >= 7.0 else 'Reprobado'
    print(f"{i+1:<5} {alumno:<12} {nota:>6.1f} {estado:<10}")
    grupal += nota
    pasaron += 1

promediogrupal = grupal / len(notas)
print("-"*36)

print(f'Promedio grupal {promediogrupal:.1f}')
print(f'Aprobados  {pasaron}')

print("_" * 36)

#Turno: Agrega al ejercicio un resumen al final del reporte: promedio del grupo y
# cantidad de aprobados, calculados dentro del mismo for que genera el reporte.

