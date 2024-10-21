def pro (a,b,c):
    return (a+b+c)/3
def g_validation(g):
  g_valid=[1,2]
  if g in g_valid:
   return True
  else:
   return False
c_m=0
n=int(input("Ingrese cantidad de alumnos: "))
for i in range(0,n,1):
 name=(input("Ingrese nombre: "))

 print("")

 print("Ingrese genero: ")
 print("1: Hombre")
 print("2: Mujer")
 g=int(input("Opción: "))
 if g==2:
  c_m=c_m+1
 else:
   c_h=c_h+1 
 n1=int(input("Ingrese primera nota: "))

 n2=int(input("Ingrese segunda nota: "))

 n3=int(input("Ingrese tercera nota: "))

 print("")

 print("Resumén alumno: ",name)
 print("Primera nota: ",n1)
 print("Segunda nota: ",n2)
 print("Tercera nota: ",n3)
 print("Promedio: ",pro(n1,n2,n3))

print("")

print("Cantidad de mujeres: ",c_m)
print("Promedio hombres: ")