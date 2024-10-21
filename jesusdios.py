def cantidad_kg_v():
    while True:
        try:
            n = float(input("Ingrese la cantidad que desea comprar: "))
            if n < 0:
                print("Cantidad invalida, ingrese un número positivo")
            else:
                break
        except ValueError:
            print("Invalido, solo números")
    return n

def precio_fruta_v():
    while True:
        try:
            n = float(input("Ingrese el valor de la fruta por kilo: "))
            if n < 0:
                print("Cantidad invalida, ingrese un número positivo")
            else:
                break
        except ValueError:
            print("Invalido, solo números")
    return n

def paga_cliente_v():
    while True:
        try:
            n = float(input("Ingrese la cantidad que el cliente pagó: "))
            if n < 0:
                print("Cantidad invalida, ingrese un número positivo.")
            else:
                break
        except ValueError:
            print("Invalido, solo números.")
    return n

def total_a_pagar(cantidad_kg,precio_fruta):
    return cantidad_kg * precio_fruta

def calculo_vuelto(total_a_pagar, paga_cliente):
    if paga_cliente < total_a_pagar:
        print("El cliente no pagó lo suficiente. Por favor pagar la cantidad restante.")
        return 0
    else:
        vuelto = paga_cliente - total_a_pagar
        return vuelto

def menu_fruta():
    print("1: Manzana")
    print("2: Sandia")
    print("3: Kiwi")
    print("4: Naranja")
    print("5: Platano")

def fruta_v():
    while True:
        try:
            menu_fruta()
            n = int(input("Elija una opción: "))
            if n < 1 or n > 5:
                print("Opción invalida, ingrese un número entre 1 y 5")
            else:
                break
        except ValueError:
            print("Invalido, recuerde ingresar solo números")
    return n


#Arreglos
nombre_vendedor = []
nombre = []
apellido = []
cantidad_kg = []
fruta = []
precio_fruta = []
paga_cliente = []
total = []
vuelto = []


ventas = int(input("Ingrese la cantidad de ventas: "))
print("")
for i in range(ventas):
    print(f"Venta cliente {i+1}: ")
    nombre_vendedor.append(input("Ingrese nombre de vendedor: "))
    print("")
    nombre.append(input("Ingrese nombre del cliente: "))
    apellido.append(input("Ingrese apellido del cliente: "))
    print("")
    cantidad_kg_valeur = cantidad_kg_v()
    cantidad_kg.append(cantidad_kg_valeur)
    print("")
    fruta_valeur = fruta_v()
    fruta.append(fruta_valeur)
    print("")
    precio_fruta_valeur = precio_fruta_v()
    precio_fruta.append(precio_fruta_valeur)
    print("")
    total_valeur = total_a_pagar(cantidad_kg_valeur, precio_fruta_valeur)
    total.append(total_valeur)
    print("")
    paga_cliente_valeur = paga_cliente_v()
    paga_cliente.append(paga_cliente_valeur)
    print("")
    # Calcular el vuelto usando la funcion "calculo_vuelto"
    vuelto_valeur = calculo_vuelto(total_valeur, paga_cliente_valeur)
    vuelto.append(vuelto_valeur)
    print("")

for i in range(ventas):
    print("******************************************************")
    print(f"Venta cliente {i+1}: ")
    print("")
    print(f"Nombre de vendedor: {nombre_vendedor[i]}")
    print("")
    print(f"Nombre cliente: {nombre[i]} {apellido[i]}")
    print("")
    print(f"Fruta: {['Manzana', 'Sandia', 'Kiwi', 'Naranja', 'Platano'][fruta[i]-1]}")
    print(f"Cantidad (kg): {cantidad_kg[i]}kg")
    print(f"Precio: {precio_fruta[i]}")
    print("")
    print(f"Total: {total[i]}")
    print(f"Paga: {paga_cliente[i]}")
    print(f"Vuelto: {vuelto[i]}")
    print("*****************************************************")
    print("")