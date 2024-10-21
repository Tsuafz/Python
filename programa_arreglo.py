def pro(numeros):
    return sum(numeros)/len(numeros)

def prom(notas):
    return (20*notas[0]+30*notas[1]+50*notas[2])/100

def nota_v():
    while True:
        try:
            n = float(input("Ingrese nota: "))
            if n < 0 or n > 7:
                print("Invalido, ingrese una nota dentro del rango (1-7). ")
            else:
                return n  # solo devolver datos validos
        except ValueError:
            print ("Invalido, ingrese un número. ")    

#si
alumnos = []
promedios = []

print("Notas")
print("")
for i in range(5):
    print(f"Alumno {i+1}")
    print("")
    nombre = input("Ingrese el nombre del alumno: ")
    print("")
    notas = [nota_v(), nota_v(), nota_v()]
    print("")
    promediov = prom(notas)
    alumnos.append({"Nombre": nombre, "Notas": notas, "promedio": promediov})
    promedios.append(promediov)  #guarda promedio de cada alumno para sacar el promedio de curso
    print(f"Promedio alumno {i+1}: {promediov:.2f}")
    print(f"Mejor nota: {max(notas):.2f}")
    print("*****************************************************************")

promedio_curso = pro(promedios)
print("")
for i, alumno in enumerate(alumnos):
    print(f"Alumno {i+1}:")
    for key, value in alumno.items():
        print(f"  {key}: {value}")
    print("")
print("")
print(f"Promedio curso: {promedio_curso:.2f} ")
print("")
print(f"Mejor promedio: {max(promediov):.2f}")
