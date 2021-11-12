print ("Bienvenido, ¿Qué conversión desea hacer?")
Divisas = input("DÓLARES A PESOS, PRESIONE [1]. PESOS A DÓLARES, PRESIONE [2]: ")
if Divisas == "1":
    precioDolar = float(input("Ingrese el precio actual del Dolar: "))
    dolar=precioDolar
    cantidad_USD = float(input("Intruce la cantidad en dólares que desea convertir a pesos: "))
    print("La cantidad de {} dólares convertidas a pesos, son: {} pesos".format(cantidad_USD, cantidad_USD * dolar))

elif Divisas == "2":
    precioPeso = float(input("Ingrese el precio actual del Peso: "))
    pesos = precioPeso
    cantidad_pesos = float(input("Intruce la cantidad en pesos que desea convertir a dólares: "))
    print("La cantidad de {} pesos convertidas a dólares, son: {} dólares".format(cantidad_pesos, cantidad_pesos * pesos))
print("Gracias por utilizar mi programa. Angel Zabaleta")
