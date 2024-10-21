
def pro(numeros): #Promedio
    return sum(numeros) / len(numeros)


def max_n(n, name, esp):
    # Encontrar la nota maxima y guardarla con el nombre del estudiante y la especialidad
    max_score = max(n)
    max_index = n.index(max_score)
    return max_score, name[max_index], esp[max_index]


def score_v(): #Validar notas
 while True:
    try:
        n = float(input("Ingrese nota valida (Entre 1 y 7): "))
        if n < 0 or n > 7:
            print("Nota invalida (entre 1 y 7)")
        else:
            break
    
    except ValueError:
        print("Nota invalida (solo numeros) ")
 return n


def mes_v(): #Validar mesada
    while True:
        try:
         me = int(input("Ingrese mesada valida (Entre 0 y 20000): "))
         if me < 0 or me > 20000:
            print("Mesada invalida (Entre 0 y 20000): ")
         else:
            break
        except ValueError:
            print("Mesada invalida (Solo numeros) ")
    return me

def age_v(): #Validar edad 
    while True:
        try:
            age = int(input("Ingrese edad valida (Entre 10 y 20): "))
            if 10 <= age <= 20:
                return age
            else:
                print("La edad debe ser entre 10 y 20, intentelo denuevo: ")
        except ValueError:
            print("Invalido, porfavor ingrese un numero ")

def ge_v(): #Validar genero
    while True:
        try:
            ge = input("Ingrese genero (H o M): ")
            if ge == "H" or ge == "M" or ge == "h" or ge =="m":
                return ge
            else:
                print("Genero invalido, porfavor ingrese H o M: ")
        except ValueError:
            print("Invalido, porfavor ingrese un caracter")

def esp_v(): #Validar especialidad
    while True:
        try:
            esp = input("Ingrese especialidad valida (contabilidad, administracion, programacion): ")
            espl = esp.lower()
            if espl == "administracion" or espl == "contabilidad" or espl == "programacion":
               return espl
            else:
                print("Especialidad invalida, ingrese una valida: ")
        except ValueError:
            print("Invalido, ingrese una especialidad valida ")

esp=[]
age=[]
g=[]
m=[]
n=[]
name=[]
#Definir arreglos arriba

for i in range(3): #Ciclo para, usando los arreglos para guardar datos
    print("")
    print(f"Datos alumno: {i+1}")
    name.append(input("Ingrese nombre: "))
    age.append(age_v())
    n.append(score_v())
    m.append(mes_v())
    g.append(ge_v())
    esp.append(esp_v())
    print("")
    print("***************************************")

for i in range(3):
 print("")
 print("Resumen alumnos: ")
 print("")
 print(f"Alumno: {i+1}")
 print(f"Nombre: {name[i]}")
 print(f"Edad: {age[i]}")
 print(f"Nota: {n[i]}")
 print(f"Mesada: {m[i]}")
 print(f"Genero: {g[i]}")
 print(f"Especialidad: {esp[i]}")
 print("")
 print("*****************************************")
print("Promedio de notas tres alumnos: ",pro(n))
print("Promedio de edad tres alumnos: ",pro(age))
print("Promedio de mesada tres alumnos: ",pro(m))
print("******************************************")
print("Alumno mejor calificado: ")
print("")
max_score, max_name, max_esp = max_n(n, name, esp)
print(f"Nombre: {max_name}")
print(f"Nota: {max_score}")
print(f"Especialidad: {max_esp}")
print("")