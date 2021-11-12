print("¡Hola! Hágamos el cálculo del promedio de estudiantes de los cursos mencionados en la actividad 7.")
n = int(input("Ingrese la cantidad de cursos a promediar "))
suma = 0
i = 1
while (i <=n):
    print("Ingrese el número de estudiantes del curso",i)
    curso = int(input())
    suma = suma+curso
    i+=1
prom = suma / n
print("El promedio de estudiantes es: ",prom)
print("¡Gracias!")
