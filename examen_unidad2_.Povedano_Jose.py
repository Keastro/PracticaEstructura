COMISION_3 = 0.03
COMISION_5 = 0.05
COMISION_8 = 0.08
COMISION_12 = 0.12

nombre = []
lista_montos = []
lista_porcentaje = []
lista_comision = []

total = 0
total_comision = 0
acum = 1

# La base de todo, ingresar la total de ventas
total_ventas = int(input("Escribe total de ventas: "))

# Bloque para ingresar datos, tanto del nombre, y del monto
while acum <= total_ventas:
    print("-"*20, "Venta:", acum, "-"*20)
    vendedor = input("Nombre del vendedor: ")
    monto = float(input("Monto de la venta: "))

    ##lista que acumulan nombres, montons, y el total para el reporte final.
    nombre += [vendedor]
    lista_montos += [monto]
    total += monto
#Bloque if que permite determinar que porcentaje de comision se le asigna a cada vendedor dependiendo del monto de su venta, y acumula el total de comisiones para el reporte final.
    if monto < 500:
        lista_porcentaje += ["3%"]
        comision = monto * COMISION_3
    elif monto < 2000:
        lista_porcentaje += ["5%"]
        comision = monto * COMISION_5
    elif monto < 5000:
        lista_porcentaje += ["8%"]
        comision = monto * COMISION_8
    else: 
        lista_porcentaje += ["12%"]
        comision = monto * COMISION_12
#Acumuladores que dan final al bucle, al igual igual que enlistar la comision.
    lista_comision += [comision]
    total_comision += comision
    acum += 1

#Aqui comienza el reporte final
print()
print('='*15, "Reporte de comisiones", '='*15)
print(f'{"Vendedor":<10}{"Monto":>15}{"Comision %":>12}{"Comision $":>13}')
print('-'*55)

for i in range(len(nombre)):
    print(f"{nombre[i]:<10}{lista_montos[i]:>15.2f}{lista_porcentaje[i]:>12}{lista_comision[i]:>13.2f}")

#Aqui tenemos el total de comisiones, ventas, y del mejor vendedor.
print("\nTotal de ventas: ", total)
print("Total de comisiones: ", total_comision)

print("Mejor vendedor: ", nombre[0], "con", lista_montos[0])
