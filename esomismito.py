def menu():
    print("1: Coca-Cola")
    print("2: Pepsi")
    print("3: Fanta")
    print("4: Sprite")
    print("5: Dr.Pepper")



def validar_producto():
 while True:
    try:
        menu
        n = int(input("Ingrese numero de producto (Entre 1 y 5): "))
        if n < 0 or n > 5:
            print("Producto invalido (entre 1 y 7)")
        else:
            break
    
    except ValueError:
        print("Producto invalido (solo numeros) ")
 return n
