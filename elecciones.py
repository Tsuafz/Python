def menu_lugar():
    print("Seleccione su lugar de voto (1 o 2): ")
    print("1. Estadio")
    print("2. Colegio")

def menu_genero():
    print("Seleccione su género:")
    print("1. Hombre")
    print("2. Mujer")
    print("3. Otro")

def validar_genero():
    menu_genero()
    while True:
        try:
            genero = int(input("Ingrese el genero (1, 2 o 3): "))
            if genero == 1:
                genero_n = "Hombre"
                break
            elif genero == 2:
                genero_n = "Mujer"
                break
            elif genero == 3:
                genero_n = "Otro"
                break
            else:
                print("Ingrese un valor valido (1, 2 o 3). ")
        except ValueError:
            print("Ingrese un valor numerico. ")
    
    return genero_n

def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 18:
                print("La edad debe ser mayor a 17 años. ")
            elif edad > 100:
                print("La edad debe ser menor a 100 años. ")
            else:
                break
        except ValueError:
            print("Ingrese un valor numerico. ")
    
    return edad

def validar_lugar():
    menu_lugar()
    while True:
        try:
            lugar = int(input("Ingrese el lugar (1 o 2): "))
            if lugar == 1:
                lugar_n = "Estadio"
                break
            elif lugar == 2:
                lugar_n = "Colegio"
                break
            else:
                print("Ingrese un valor valido (1 o 2). ")
        except ValueError:
            print("Ingrese un valor númerico. ")

    return lugar_n

def validar_voto():
    while True:
        try:
            voto = input("Vote por 'Azul' o 'Rojo': ").strip().lower()
            if voto == 'azul' or voto == 'rojo':
                return voto.capitalize()  # Regresa el voto con la primera letra en mayuscula
            else:
                print("Ingrese un voto válido ('Azul' o 'Rojo').")
        except ValueError:
            print("Ocurrió un error, intente de nuevo.")

def contar_votos(votantes):
    conteo = {"Azul": 0, "Rojo": 0}
    for votante in votantes:
        conteo[votante['Voto']] += 1
    return conteo

def declarar_ganador(conteo):
    if conteo["Azul"] > conteo["Rojo"]:
        return "Azul"
    elif conteo["Rojo"] > conteo["Azul"]:
        return "Rojo"
    else:
        return "Empate"

votantes = []
nombre = ""  # Inicializa el nombre para entrar al bucle

while nombre.lower() != "x":  # Revisa si el nombre es "x o "X"
    nombre = input("Ingrese el nombre del votante (o 'x' para salir): ")
    if nombre.lower() == "x":  # Rompe el bucle si el usuario ingresa por teclado "x" o "X"
        break
    apellido = input("Ingrese el apellido del votante: ")
    genero = validar_genero()
    edad = validar_edad()
    ciudad = input("Ingrese la ciudad del votante: ")
    lugar = validar_lugar()
    voto = validar_voto()  # Toma el voto
    votantes.append({"Nombre": nombre, "Apellido": apellido, "Genero": genero, "Ciudad": ciudad, "Lugar": lugar, "Voto": voto})

# Cuenta votos y declara ganador
conteo_votos = contar_votos(votantes)
ganador = declarar_ganador(conteo_votos)

# Imprime resultados
print("Resultados de la votación:")
print(f"Votos Azules: {conteo_votos['Azul']}")
print(f"Votos Rojos: {conteo_votos['Rojo']}")
print(f"El ganador es: {ganador}")

