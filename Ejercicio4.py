#CICLO WHILE - Repite un bloque mientras una condicion sea true.
#Se usa cuando no sabes de antemano cuantas veces necesitas repetir -
#el numero de repeticiones depende de lo que ocurra durante la ejecucion.

#REgla critica: algo dentro del while debe cambiar en cada iteracion para que la 
#condicion eventualmente sea false. Sin eso, el ciclo nunca se termina [break].

#Ejercicio - while básico: contador y acumulador
n =int(input('Suma del 1 hasta: '))
i = 1 #contador `Empieza en 0
suma = 0
while i <= n:
    suma = suma + i
    i = i + 1
print(f'Suma de 1 a {n}: {suma}')

#verificacion matematica: n * (n+1)/2
formula = n * (n +1 ) // 2
print(f'Verificacion con formula:{n} * ({n} + 1 )/ 2= {formula}')

#Tu turno: Reescribe el ejercico usando for en lugar de while. Cual version es mas
#natural para este problema? Explica por que con tus palabras.

n =int(input('Suma del 1 hasta: '))
i = 0 #contador `Empieza en 0

for i in range(n): #<-----Debo poner range o enumerate para que funcione
    i = 1 
    suma = 0
    if i <= n: 
        suma = suma + i
        i = i + 1
print(f'Suma de 1 a {n}: {suma}')

#Lo que pasa con el for es que si lo eliges, te arroja error por el tipo de variable 
# que tiene, y tienes que transformando con range or enumerate. Naturalmente, es mejor
#usar  while porque no tienes que transformar valores, porque no hay una lista.

#Ejercicio - while para validar entrada:: el patron de reitento

nota = float(input('Calificacion (0-10): '))

while nota < 0 or nota > 10:
    print('Calificacion invalida. Debe ser ser entre 0 y 10')
    nota = float(input('Califacion (0-10)'))

print(f'Calificacion registrada: {nota:.1f}')
print()

#while true + break
while True:
    edad = int(input('Tu edad(0-100): '))
    if 1 <= edad <= 100:
        break
    print('Edad invalida, intenta de nuevo.')

print(f'Edad registrada: {edad}')