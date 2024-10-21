def horas(hora_entrada, hora_salida):
    return hora_salida - hora_entrada

def tota_a_pagar(valor_hora, hora_entrada, hora_salida):
    return valor_hora * horas(hora_entrada, hora_salida)

def validar_v():
    while True:
        try:
            n = int(input("Ingrese valor por hora: "))
            if n < 0:
                print("Invalido, el valor no puede ser negativo, ingrese nuevamente: ")
            else:
                return n
        except ValueError:
            print("Invalido, el valor ingresado debe ser un número")

def validar_c():
    while True:
        try:
            n = int(input("Ingrese total de clientes: "))
            if n < 0:
                print("Invalido, el valor no puede ser negativo, ingrese nuevamente: ")
            else:
                return n
        except ValueError:
            print("Invalido, el valor ingresado debe ser un número.")

def validar_h_e():
    while True:
        try:
            n = int(input("Ingrese hora de entrada: "))
            if n < 0 or n > 24:
                print("Invalido, ingrese nuevamente: ")
            else:
                return n
        except ValueError:
            print("Invalido, el valor ingresado debe ser un número.")

def validar_h_s():
    while True:
        try:
            n = int(input("Ingrese hora de salida: "))
            if n < 0 or n > 24:
                print("Invalido, ingrese nuevamente: ")
            else:
                return n
        except ValueError:
            print("Invalido, el valor ingresado debe ser un número.")


print("Estacionamiento")

valor_hora = validar_v()
print("")
n = validar_c()
print("")

nombre = []
patente = []
hora_entrada = []
hora_salida = []
total_a_pagar = []

for i in range(n):
    print(f"Cliente {i+1}: ")
    nombre.append(input("Ingrese nombre del cliente: "))
    patente.append(input("Ingrese patente del vehiculo: "))
    print("")
    hora_entrada.append(validar_h_e())
    print("")
    hora_salida.append(validar_h_s())
    print("")
    total_valeur = tota_a_pagar(valor_hora, hora_entrada[i], hora_salida[i])
    total_a_pagar.append(total_valeur) 
    print(f"Total a pagar: ${total_valeur:.2f}")