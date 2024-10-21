print ("Jose Juan Perez")
print ("")
print ("Calculator si")
def suma (a, b):
    return a + b
def resta (a, b):
    return a - b
def multi (a, b):
    return a * b
def divi (a, b):
    return a / b
def pro(a,b,c):
    return (a+b+c)/3
def si(a,b,c):
    return max(a,b,c)
def no(a,b,c):
    return min(a,b,c)
# Ingreso de datos
print ("SUMA")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print ("RESTA")
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese otro numero: "))
print ("MULTIPLICACION")
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
print ("DIVISION")
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
print ("Promedio de 3 digitos")
s = float(input("Ingrese un numero: "))
d = float(input("Ingrese un segundo numero: "))
k = float(input("Ingrese un tercer numero: "))
print ("Nota maxima y nota minima")
c = float(input("Ingrese un numero: "))
v = float(input("Ingrese un segundo numero: "))
b = float(input("Ingrese un tercer numero: "))
print ("")
print ("RESPUESTAS")
print("1: Suma")
print("2: Resta")
print("3: Multiplicacion")
print("4: Division")
print("5: Promedio 3 digitos")
print("6: Nota maxima y nota minima")
print("")
op=int(input("Ingrese operatoria: "))
print("")
if op==1:
 print ("SUMA ", suma(num1, num2))

if op==2:
 print ("RESTA ", resta(x, y))

if op==3:
 print ("MULTIPLICACION ", multi(n1, n2))

if op==4:
 print ("DIVISION ", divi(numero1, numero2))
 
if op==5:
 print ("PROMEDIO ", pro(s,d,k))

if op==6:
 print ("Nota maxima: ",si(c,v,b))
 print ("Nota minima: ",no(c,v,b))