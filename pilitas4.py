# Crear la pila vacía
pilaFia = []
# Crear la pila con números del 1 al 15
for i in range(1, 16):
    pilaFia.append(i)

print(" Pila original:")
print(pilaFia)

# Índices a eliminar 
tercero = 2   # 3er
septimo = 6   # 7mo

# Eliminar primero el índice mayor para no alterar el orden
pilaFia.pop(tercero)
pilaFia.pop(septimo)

print("\n Pila después de eliminar el 3.º y 7.º elemento:")
print(pilaFia)