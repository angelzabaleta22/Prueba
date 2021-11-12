print (f"\n¡Hola! Vamos a hacer la operación matemática que escojas ingrensando el símbolo de dicha operación después de ingresar dos números cualquiera. ")
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))

operacion = input("Ingrese el símbolo de la operación que desea realizar: ")
if operacion == "+":
    suma = numero1+numero2
    print(f"\nLa suma de los dos números da: {suma}")
elif operacion == "-":
    resta = numero1-numero2
    print(f"\nLa resta de los dos números da: {resta}")

elif operacion == "*":
    mult = numero1*numero2
    print(f"\nLa multiplicación de los dos números da: {mult}")

elif operacion == "/":
    div = numero1/numero2
    print(f"\nLa división de los dos números da: {div}")
else:
    print("\nIntroduzca un símbolo válido.")
