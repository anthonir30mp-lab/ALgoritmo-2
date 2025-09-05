def merge_sort(cursos):
    if len(cursos)>1:
        mid=len(cursos)//2
        mitad_izquierda=cursos[:mid]
        mitad_derecha=cursos[mid:]
        #Usa la recursividad ara dividir cadalista
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        #los indices para las listas
        i=0
        j=0
        k=0

        while i<len(mitad_izquierda) and j<len(mitad_derecha):#para verificar que haya elementos que procesar en ambas sublistas 
            if mitad_izquierda[i]['hora_inicio']<mitad_derecha[j]['hora_inicio']: #se compara los horas de curso de mabas mitades
                cursos[k]=mitad_izquierda[i]
                i+=1
            else:
                cursos[k]=mitad_derecha[j]
                j+=1
            k+=1
        while i<len(mitad_izquierda):#se ejecuta siaun tiene elementos
            cursos[k]=mitad_izquierda[i]
            i+=1
            k+=1
            
        while j<len(mitad_derecha):#se ejecuta siaun tiene elementos
            cursos[k]=mitad_derecha[j]
            j+=1
            k+=1
    return cursos

def busqueda_binaria(cursos_ordenados, hora_buscada): #la busqueda binaria es ams eficiente para listas ordenadas
    inicio=0
    fin=len(cursos_ordenados)-1#se inicializa en el ultimo elemento de la lista

    while inicio<=fin: #mientras el rango de busqueda sea validad
        mid=(inicio+fin)//2
        hora_actual=cursos_ordenados[mid]['hora_inicio']#hora de inicio de hora en punto medio

        if hora_actual==hora_buscada:
            return cursos_ordenados[mid]
        elif hora_actual<hora_buscada:
            inicio=mid+1#ignora la mitad izquierde y ajusta el inicio al siguiente
        else:
            fin=mid-1#ignora la mitad derecha y ajusta el fin al siguiente
    return None

#Lista de cursos de la hoja
cursos=[
    {"codigo": "MICRO204", "nombre": "Microeconomia", "hora_inicio": "10:15"},
    {"codigo": "FIS202", "nombre": "Física II", "hora_inicio": "03:45"},
    {"codigo": "AEDIG305", "nombre": "Algoritmo y Estructura de datos II", "hora_inicio": "09:30"},
    {"codigo": "TI110", "nombre": "Tecnologias de informacion II", "hora_inicio": "08:45"},
    {"codigo": "EPR150", "nombre": "Estadistica y Probabilidad II", "hora_inicio": "17:00"}
]
#para ordenar
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
