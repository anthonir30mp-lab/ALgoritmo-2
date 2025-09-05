def merge_sort(cursos):
    if len(cursos)>1:
        mid=len(cursos)//2
        mitad_izquierda=cursos[:mid]
        mitad_derecha=cursos[mid:]

        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)


        i=0
        j=0
        k=0

        while i<len(mitad_izquierda) and j<len(mitad_derecha):
            if mitad_izquierda[i]['hora_inicio']<mitad_derecha[j]['hora_inicio']:
                cursos[k]=mitad_izquierda[i]
                i+=1
            else:
                cursos[k]=mitad_derecha[j]
                j+=1
            k+=1
        while i<len(mitad_izquierda):
            cursos[k]=mitad_izquierda[i]
            i+=1
            k+=1
            
        while j<len(mitad_derecha):
            cursos[k]=mitad_derecha[j]
            j+=1
            k+=1
    return cursos

def busqueda_binaria(cursos_ordenados, hora_buscada): #la busqueda binaria
    inicio=0
    fin=len(cursos_ordenados)-1

    while inicio<=fin:
        mid=(inicio+fin)//2
        hora_actual=cursos_ordenados[mid]['hora_inicio']

        if hora_actual==hora_buscada:
            return cursos_ordenados[mid]
        elif hora_actual<hora_buscada:
            inicio=mid+1
        else:
            fin=mid-1
    return None

#Lista de cursos de la hoja
cursos=[
    {"codigo": "MAT101", "nombre": "Matemáticas I", "hora_inicio": "08:00"},
    {"codigo": "FIS202", "nombre": "Física II", "hora_inicio": "10:30"},
    {"codigo": "PROG305", "nombre": "Programación Avanzada", "hora_inicio": "09:15"},
    {"codigo": "HIST110", "nombre": "Historia Universal", "hora_inicio": "07:45"},
    {"codigo": "QUIM150", "nombre": "Química General", "hora_inicio": "14:00"}
]

cursos_ordenados=merge_sort(cursos)
print("Cursos ordenados por hora de inicio:")
for curso in cursos_ordenados:
    print(curso)

#para buscar
hora_usuario=input("Ingrese la hora de inicio a buscar (ej. 09:15): ")
curso_encontrado=busqueda_binaria(cursos_ordenados, hora_usuario)

if curso_encontrado:
    print("\nCurso encontrado:")
    print(curso_encontrado)
else:
    print("\nNo se encontraron cursos a esa hora.")
