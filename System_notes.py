#Constantes

STUDENTS = 15
MIN_PASS = 6.0
GRADO_A = 9.0
GRADO_B = 8.0
GRADO_C = 7.0
GRADO_D = 6.0
PORCENTAJE = 100
LINEAS = 54

#Variables y listas
acumulador = 0
aprobados = 0
reprobados = 0
nota = 0
nombre = []
grados = []
status =[]
nota_general = []
total = 0.0

#La base que determina si aprueba o no aprueban los estudiantes.
while acumulador < STUDENTS: #como el conteo inicia desde el 0, seran 16 numeros si pongo <= en vez de 15
    nombre = nombre + [input("Escribe el nombre de un estudiante: ")]
    nota = float(input("Escribre la nota que obtuvo(con decimal): "))

#Aqui tenemeos acumuladores, uno de lista y otra que tiene el total de calificaciones para el promedio.
    nota_general += [nota]
    total = total + nota

    if nota > MIN_PASS:
        print("El estudiante aprobo")
        status = status +["Aprobado"]
        aprobados +=1

        if nota > GRADO_A:
            print("El alumno obtuvo el grado A")
            grados += ['A']
            print()

        if nota > GRADO_B and nota < GRADO_A:
            print("El alumno obtuvo el grado B")
            grados += ['B']
            print()

        if nota > GRADO_C and nota < GRADO_B:
            print("El alumno obtuvo el grado C")
            grados += ['C']
            print()

        if nota > GRADO_D and nota < GRADO_C:
            print("El alumno obtuvo el grado D")
            grados+=['D']
            print()


    else:
        print("El estudiante reprobo")
        print("Obtuvo el grado F")
        print()
        grados+=["F"]
        status = status + ["Reprobado"]
        reprobados += 1
    acumulador += 1

#AQUI COMIENZA EL REPORTE FINAL
print('='* 20,"Reporte final ", "="*18)
print()

#Nota: cuando se trata de dar espacios entre columnas, no uso constante porque varia 
# mucho la cantidad de espacios que se da a cada uno para tener que usar constantes, es decir,
#no puede ser constante porque nunca sera el mismo valor cada espacio, y si lo fuera, queda mal.
print(f'{"Alumnos " :<10}{"Nota" :>15}{"Estado":>12}{'Letra':>13}')

print('-' *LINEAS)

for i in range(len(nombre)) :
    notas = float(nota_general[i])
    estado = status[i]
    grade = grados[i]
    print(f"{nombre[i]:<10}{notas:>15}{estado:>14}{grade:>7}") 
print()
print('-'*LINEAS)

#SEGUNDA PARTE DEL REPORTE FINAL: PORCENTAJE, PROMEDIO Y CANTIDAD DE APROBADOS
promedio = total / STUDENTS
print(f"Promedio grupal {promedio:.1f}")
print('Cantidad de aprobados ', aprobados, " | ",' Cantidad de reprobados ', reprobados)
print("-"*LINEAS)

nota_alta = nota_general[0]
nota_baja = nota_general[0]
nombre_alto = nombre[0]
nombre_bajo = nombre[0]

porcentaje = (aprobados / STUDENTS) * PORCENTAJE

#SIRVE PARA DETERMINAR CUAL ES VALOR MAS ALTO Y MAS BAJO DE LOS CHICOS.
for a in range(len(nota_general)):
        puntajes = nota_general[a]
        if puntajes > nota_alta:
            nota_alta = puntajes
            nombre_alto = nombre[a]

        if puntajes < nota_baja:
            nota_baja = puntajes
            nombre_bajo = nombre[a]

print(f'Mejor calificacion: {nombre_alto:>7} con {nota_alta:.1f}')
print(f"Peor calificacion: {nombre_bajo:>7} con {nota_baja:.1f}")
print(f"Porcentaje de aprobacion: {porcentaje:.1f}%")