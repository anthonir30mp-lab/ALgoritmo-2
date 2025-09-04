##########FALTA CORREGIR ALGUNOS ERRORES 


def merge_sort(cursos): # definimos la funcion y llamamos a la lista cursos
    if len(cursos) > 1: # verificamos q la lista tenga mas de un elemento
        #Aca sirve para dividir la lista en 2
        mid = len(cursos) // 2 # divide la lista en 2 para calcular el punto medio de la lista
        mitad_izquierda = cursos[:mid] # Crea una sublista con la mitad izquierda de la lista principal
        mitad_derecha = cursos[mid:] # Crea una sublista con la mitad derecha de la lista principal

        #Se usa la recursividad para ordenar cada mitad
        merge_sort(mitad_izquierda) # se llama a si misma para ordenar la mitad izquierda
        merge_sort(mitad_derecha) # se llama a si misma para ordenar la mitad derecha

        # Fusionar las mitades ordenadas
        #inicializmos los indices en 0
        i =0 #izquierda
        j =0 #derechha
        k =0 #lista original.
        ##TOCA EXPLICAR PORQUE ES MENOR IGUAL O MAYOR IGUAL EN CADA WHILE NO SOLO EXPLICAR CADA PARTE CON LA PRIMERA EXPLICACION DEL WHILE

        while i<len(mitad_izquierda) and j < len(mitad_derecha): #Mientras  queden objetos q procesar en ambas sublistas 
            if mitad_izquierda[i]['hora_inicio'] < mitad_derecha[j]['hora_inicio']: # Se compara sus horas de curso de ambas mitades
                cursos[k] = mitad_izquierda[i] # si el curso de la izquierda es menor lo pone en la lista original
                i += 1 #incrementa el indice i para pasar al siguiente curso de la mitad izquierda.
            else: # Si el de la derecha es menor o igual.
                cursos[k] = mitad_derecha[j] # Lo coloca en la lista original.
                j += 1 #incrementa el indice  j para pasar al siguiente curso de la mitad derecha.
            k += 1 #incrementa el índice k para la lista original, moviéndose al siguiente espacio.
#PORQUE PASA ESTO 
        while i < len(mitad_izquierda): # Después del bucle principal, este bucle se ejecuta si la mitad izquierda aún tiene elementos.
            cursos[k] = mitad_izquierda[i] # Copia los elementos restantes de la mitad izquierda a la lista original.
            i += 1
            k += 1
#PORQUE PASA ESTO 
        while j < len(mitad_derecha): # Se ejecuta si la mitad derecha tiene elementos restantes.
            cursos[k] = mitad_derecha[j] # Copia los elementos restantes de la mitad derecha a la lista original.
            j += 1
            k += 1
    return cursos # Retorna la lista de cursos ya ordenada.

def busqueda_binaria(cursos_ordenados, hora_buscada): # Define la función que recibe la lista ordenada y la hora a buscar.
    inicio = 0 # Inicializa el índice de inicio en 0.
    fin = len(cursos_ordenados) - 1 # Inicializa el índice de fin en el último elemento de la lista.

    while inicio <= fin: # El bucle continúa mientras el rango de búsqueda sea válido.
        mid = (inicio + fin) // 2 # Calcula el índice del elemento del medio.
        hora_actual = cursos_ordenados[mid]['hora_inicio'] # Accede a la hora de inicio del curso en el punto medio.

        if hora_actual == hora_buscada: # Si la hora del medio es igual a la hora buscada.
            return cursos_ordenados[mid] # Retorna el curso que fue encontrado.
        elif hora_actual < hora_buscada: # Si la hora del medio es menor que la hora buscada.
            inicio = mid + 1 # Ignora la mitad izquierda y ajusta el 'inicio' al siguiente elemento del medio.
        else: # Si la hora del medio es mayor que la hora buscada.
            fin = mid - 1 # Ignora la mitad derecha y ajusta el 'fin' al elemento anterior al medio.
    return None # Si el bucle termina sin encontrar el curso, retorna 'None'.
# Lista de cursos original 
cursos = [
    {"codigo": "MAT101", "nombre": "Matemáticas I", "hora_inicio": "08:00"},
    {"codigo": "FIS202", "nombre": "Física II", "hora_inicio": "10:30"},
    {"codigo": "PROG305", "nombre": "Programación Avanzada", "hora_inicio": "09:15"},
    {"codigo": "HIST110", "nombre": "Historia Universal", "hora_inicio": "07:45"},
    {"codigo": "QUIM150", "nombre": "Química General", "hora_inicio": "14:00"}
]

# a) Ordenar la lista de cursos usando Merge Sort
cursos_ordenados = merge_sort(cursos)
print("Cursos ordenados por hora de inicio:")
#FALTA EXPLICA ESTO
for curso in cursos_ordenados:
    print(curso)

# b) Buscar un curso por hora usando Búsqueda Binaria
hora_usuario = input("Ingrese la hora de inicio a buscar (ej. 09:15): ")
curso_encontrado = busqueda_binaria(cursos_ordenados, hora_usuario)

if curso_encontrado:
    print("\nCurso encontrado:")
    print(curso_encontrado)
else:
    print("\nNo se encontraron cursos a esa hora.")
