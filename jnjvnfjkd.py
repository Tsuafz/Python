def control_presupuesto(presupuesto, sueldo):
    if presupuesto < sueldo:
        print("Se pasa del presupuesto. Por favor ingresar denuevo.")
        return None
    else:
        restante = presupuesto - sueldo
        return restante

def promedio(numeros):
    return sum(numeros) / len(numeros)

ORIGINAL_FECHA = ["17 Septiembre", "18 Septiembre", "19 Septiembre", "20 Septiembre"]
MAX_ATTEMPTS = 5
fecha_lista = ORIGINAL_FECHA.copy()  # Inicializa la variable fecha_variable

def fecha_v():
    global fecha_lista  # Usa la variable global fecha_lista
    for attempt in range(MAX_ATTEMPTS):
        if not fecha_lista:  #Revisa si la lista esta vacia
            fecha_lista = ORIGINAL_FECHA.copy()  #Reinicia la lista a la original
        for i, fecha in enumerate(fecha_lista, start=1):
            print(f"{i}: {fecha}")

        while True:
            try:
                selected_date_index = int(input("Ingrese la fecha del artista: "))
                if 1 <= selected_date_index <= len(fecha_lista):
                    selected_date = fecha_lista[selected_date_index - 1]
                    fecha_lista.remove(selected_date)  #Remueve la fecha seleccionada de la lista
                    return selected_date
                else:
                    print("Opción inválida. Por favor, ingrese un número entre 1 y", len(fecha_lista))
            except ValueError:
                print("Error: Por favor, ingrese un número.")

    print("Demasiados intentos fallidos. Saliendo...")
    return None

def personajes_v(n):
    while True:
        try:
            x = int(input("Ingrese su personaje: "))
            if not 1 <= x <= n:
                print(f"Opción invalida, recuerde ingresar entre un rango de 1 hasta {n}. ")
            else:
                return x
        except ValueError:
            print("Opción invalida, recuerde ingresar un numero entero. ")

def sueldo_v(presupuesto):
    while True:
        try:
            x = float(input("Ingrese sueldo: $"))
            if not 1000000 <= x <= presupuesto:
                print(f"Opción invalida, ingrese un valor entre el rango $1000000 hasta ${presupuesto}. ")
            else:
                return x
        except ValueError:
            print("Ingrese un número: $")

#arreglitos sisisi
personajes = []
sueldos = []

while True:
    try:
        presupuesto = int(input("Ingrese el presupuesto: $"))
        if not 1 <= presupuesto:
            print("Opción invalida, ingrese un valor mayor a 0: $")
        else:
            break
    except ValueError:
        print("Opción invalida, recuerde ingresar un número entero.")

while True:
    try:
        num_personajes = int(input("Ingrese cuantos personajes habrán: "))
        if not 3 <= num_personajes:
            print("Opción invalida, ingrese un valor mayor a 3: ")
        else:
            break
    except ValueError:
        print("Opción invalida, recuerde ingresar un número entero.")

print("")
for i in range(num_personajes):
    print("")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    print("")
    apodo = input("Ingrese apodo: ")
    print("")
    fecha = fecha_v()
    print("")
    sueldo = sueldo_v(presupuesto)
    print("")
    presupuesto_rest = control_presupuesto(presupuesto, sueldo)
    if presupuesto_rest is None:
        break
    print(f"Su presupuesto restante es: {presupuesto_rest}")
    presupuesto = presupuesto_rest
    print("*****************************************************************************************")
    sueldos.append(sueldo)
    personajes.append({"Nombre": nombre, "Apellido": apellido, "Apodo": apodo, "Fecha": fecha, "Sueldo": sueldo})

for i, personaje in enumerate(personajes):
    print(f"Personaje {i+1}:")
    for key, value in personaje.items():
        print(f" {key}: {value}")
    print("")
print(f"Promedio de sueldos: {promedio(sueldos)}")