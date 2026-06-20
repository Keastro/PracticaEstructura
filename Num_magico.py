#Tu turno: crea un programa que pida el usuario adivinar un numero secreto (define
#tu el número con una constante). Con while, sigue pidiendo hasta que lo adivine e 
# imprime cuantos intentos necesito.
MAGICO = 777
print('Advina el numero')
resultado = 0
errores = 0

while resultado != MAGICO:
    resultado = int(input("Escribe un numero "))

    if resultado != MAGICO:
        print('Vuelve a intentarlo') 
        errores+=1  
    if resultado == MAGICO:
        print("¡Acertaste!")
        print("Cantidad de errores ", errores)