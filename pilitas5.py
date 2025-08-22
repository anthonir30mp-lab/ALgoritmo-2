#Ingresar una pila con  20 nonbres y imprimes sacas 1 aplicando el concepto del lIFO
def nombre():
    nombre=str(input("Ingrese nombre:"))
    return nombre
pilaFia=[]
for i in range (1,4):
#for i in range (1,20):
    n=nombre()
    pilaFia.append(n)
print(pilaFia)
print("\nPila implementa LIFO")
pilaFia.pop()
print("Pila: ", pilaFia)

primero=0
pilaFia.pop(primero)
print("\nLa fila despues de eliminar el primero")
print(pilaFia)

