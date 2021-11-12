print ("¡Hola! Bienvenido al ejercicio número 3: Jugando con números. ")
print ("Primero determinemos si el número es par o impar. ")


numero = int(input("Escriba un número de tres cifras cualquiera: "))
dato = str(numero)
if numero % 2 == 0:
   numero = print("%i Es un número par. " % numero)
   dato = dato [::-1]
   print ("Valor invertido: ", dato)
   
   
 
else: 
    print("Es impar y la suma de sus extremos es: ")
    lista = list (dato)
    lista = [int(c) for c in lista]
    suma = lista [0:2]
    suma = lista[0] + (lista[2]); (print(suma))
    suma = str (suma)
    suma = suma [:: -1]; (print("Que invertido es", suma))


n = int (dato)
def evaluar_primo(n):
   contador = 0
   resultado = True
   for i in range(1,n+1):
      if (n%i==0):
          contador+=1
      if (contador >2):
         resultado = False
         break
   return resultado
if (evaluar_primo(n)==True):
   print("El número es primo y su cuadrado es: ", n**2)
   print ("El cuadrado de sus extremo es: ", lista[0]**2, "y", lista[2]**2 )
else :
   print("☻")    
