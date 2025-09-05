class Pagina:
    def __init__(self,url,titulo,fecha_hora):
        self.url=url
        self.titulo=titulo
        self.fecha_hora=fecha_hora
        self.siguiente=None
        self.anterior=None


class Historial:
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.actual=None

    #a
    def agregar_pagina(self,url,titulo,fecha_hora):
        nueva_pagina=Pagina(url,titulo,fecha_hora)
        if(not self.cabeza):
            self.cabeza=nueva_pagina
            self.cola=nueva_pagina
            self.actual=nueva_pagina
        else:
            self.cola.siguiente=nueva_pagina
            nueva_pagina.anterior=self.cola
            self.cola=nueva_pagina
            self.actual=nueva_pagina
        print(f"Página '{titulo}' agregada al historial.")

    #b
    def retroceder(self):
        if(self.actual and self.actual.anterior):
            self.actual=self.actual.anterior
            print(f"Retrocediendo a: {self.actual.titulo} ({self.actual.url})")
        else:
            print("No hay página anterior para retroceder.")

    #c
    def avanzar(self):
        if(self.actual and self.actual.siguiente):
            self.actual=self.actual.siguiente
            print(f"Avanzando a: {self.actual.titulo} ({self.actual.url})")
        else:
            print("No hay página siguiente para avanzar.")

    #d
    def eliminar_pagina(self,url):
        pagina_actual=self.cabeza
        while(pagina_actual):
            if(pagina_actual.url==url):
                if(pagina_actual.anterior):
                    pagina_actual.anterior.siguiente=pagina_actual.siguiente
                else:
                    self.cabeza=pagina_actual.siguiente
                
                if(pagina_actual.siguiente):
                    pagina_actual.siguiente.anterior=pagina_actual.anterior
                else:
                    self.cola=pagina_actual.anterior
                    
                if(self.actual==pagina_actual):
                    self.actual=pagina_actual.anterior
                    
                print(f"Página '{pagina_actual.titulo}' eliminada.")
                return
            pagina_actual=pagina_actual.siguiente
        print(f"No se encontró la página con la URL: {url}")

    #e
    def buscar_pagina(self,busqueda):
        pagina_actual=self.cabeza
        while(pagina_actual):
            if(busqueda.lower() in pagina_actual.url.lower() or busqueda.lower() in pagina_actual.titulo.lower()):
                print("Página encontrada:")
                print(f"URL: {pagina_actual.url}")
                print(f"Título: {pagina_actual.titulo}")
                print(f"Fecha/Hora: {pagina_actual.fecha_hora}")
                return
            pagina_actual=pagina_actual.siguiente
        print(f"No se encontraron resultados para: {busqueda}")

    #f
    def mostrar_historial(self):
        if(not self.cabeza):
            print("El historial está vacío.")
            return
            
        print("Historial de Navegación:")
        pagina_actual=self.cabeza
        while(pagina_actual):
            print(f"-> URL: {pagina_actual.url}, Título: {pagina_actual.titulo}, Hora: {pagina_actual.fecha_hora}")
            pagina_actual=pagina_actual.siguiente

def menu_historial():
    mi_historial=Historial()

    #paginas de ejemplo
    mi_historial.agregar_pagina("google.com","Google","10:00 AM")
    mi_historial.agregar_pagina("wikipedia.org","Wikipedia","10:05 AM")
    mi_historial.agregar_pagina("github.com","GitHub","10:10 AM")
    mi_historial.agregar_pagina("stackoverflow.com","Stack Overflow","10:15 AM")
    print("\n")

    while(True):
        print("\n--- Menú de Historial de Navegación ---")
        print('a. Agregar nueva página')
        print('b. Retroceder')
        print('c. Avanzar')
        print('d. Eliminar página')
        print('e. Buscar página')
        print('f. Mostrar historial completo')
        print('s. Salir')

        opcion=input("Seleccione una opción: ").lower()

        if(opcion=='a'):
            url=input("Ingrese la URL: ")
            titulo=input("Ingrese el título: ")
            fecha_hora=input("Ingrese la fecha y hora: ")
            mi_historial.agregar_pagina(url,titulo,fecha_hora)
        elif(opcion=='b'):
            mi_historial.retroceder()
        elif(opcion=='c'):
            mi_historial.avanzar()
        elif(opcion=='d'):
            url=input("Ingrese la URL de la página a eliminar: ")
            mi_historial.eliminar_pagina(url)
        elif(opcion=='e'):
            busqueda=input("Ingrese la URL o título a buscar: ")
            mi_historial.buscar_pagina(busqueda)
        elif(opcion=='f'):
            mi_historial.mostrar_historial()
        elif(opcion=='s'):
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el menú interactivo
if(__name__=="__main__"):
    menu_historial()
