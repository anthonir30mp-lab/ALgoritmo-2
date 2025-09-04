###########FALTA CORREGIR Y EXPLICAR ALGUNAS COSAS COMO AGREGAR PÁGINA Y DAR OPCIONES UN MENU CREO Q EN LA PRIMERA TAMBIEN FALTA ESO CORRREGIR
# Definición del nodo (página)
class Pagina: # Crea la plantilla para un nodo en la lista.
    def __init__(self, url, titulo, fecha_hora): # El constructor del nodo. Se ejecuta al crear un objeto Pagina.
        self.url = url 
        self.titulo = titulo 
        self.fecha_hora = fecha_hora 
        self.siguiente = None #no apunta a nada.
        self.anterior = None #no apunta a nada.

# Definición del historial (lista doblemente enlazada)
class Historial: # Crea la clase que gestiona la lista enlazada.
    def __init__(self): # El constructor del historial.
        self.cabeza = None # Puntero al primer nodo de la lista. Inicialmente, la lista está vacía.
        self.cola = None # Puntero al último nodo de la lista.
        self.actual = None # Puntero a la página en la que el usuario está "ubicado".


    # a. Agregar una nueva página al final del historial.

    def agregar_pagina(self, url, titulo, fecha_hora): # Método para añadir una nueva página.
        nueva_pagina = Pagina(url, titulo, fecha_hora) # Crea una nueva instancia de la clase Pagina.
        if not self.cabeza: # Condición: ¿la lista está vacía? (self.cabeza es None)
            self.cabeza = nueva_pagina # Si está vacía, el nuevo nodo es el primero.
            self.cola = nueva_pagina # y también es el último.
            self.actual = nueva_pagina # El puntero de ubicación actual se establece en este nuevo nodo.
        else: # Si la lista ya tiene elementos.
            self.cola.siguiente = nueva_pagina # El 'siguiente' del último nodo actual apunta al nuevo nodo.
            nueva_pagina.anterior = self.cola # El 'anterior' del nuevo nodo apunta al viejo último nodo.
            self.cola = nueva_pagina # El nuevo nodo se convierte en el nuevo último nodo.
            self.actual = nueva_pagina # La ubicación actual se actualiza a la nueva página.

    # b. Retroceder en el historial.
    def retroceder(self): # Método para ir a la página anterior.
        if self.actual and self.actual.anterior: # Comprueba que haya una página actual y una anterior a ella.
            self.actual = self.actual.anterior # Mueve el puntero de ubicación 'actual' al nodo anterior.
            print(f"Retrocediendo a: {self.actual.titulo} ({self.actual.url})") # Muestra la página a la que se movió.
        else: # Si no hay página anterior (ej. estás en el inicio del historial).
            print("No hay página anterior para retroceder.") # Imprime un mensaje de error.

    # c. Avanzar en el historial.
    def avanzar(self): # Método para ir a la página siguiente.
        if self.actual and self.actual.siguiente: # Comprueba que haya una página actual y una siguiente a ella.
            self.actual = self.actual.siguiente # Mueve el puntero de ubicación 'actual' al nodo siguiente.
            print(f"Avanzando a: {self.actual.titulo} ({self.actual.url})") # Muestra la página a la que se movió.
        else: # Si no hay página siguiente (ej. estás en la última página).
            print("No hay página siguiente para avanzar.") # Imprime un mensaje de error.

    # d. Eliminar una página por su URL.
    def eliminar_pagina(self, url): # Método para eliminar un nodo por su URL.
        pagina_actual = self.cabeza # Inicia el recorrido desde el primer nodo.
        while pagina_actual: # Bucle que se ejecuta mientras no se llegue al final de la lista.
            if pagina_actual.url == url: # Si la URL del nodo actual coincide con la URL buscada.
                if pagina_actual.anterior: # Si el nodo no es la cabeza.
                    pagina_actual.anterior.siguiente = pagina_actual.siguiente # El nodo anterior ahora apunta al siguiente del que se eliminará.
                else: # Si el nodo SÍ es la cabeza.
                    self.cabeza = pagina_actual.siguiente # El segundo nodo se convierte en la nueva cabeza.

                if pagina_actual.siguiente: # Si el nodo no es la cola.
                    pagina_actual.siguiente.anterior = pagina_actual.anterior # El nodo siguiente ahora apunta al anterior del que se eliminará.
                else: # Si el nodo SÍ es la cola.
                    self.cola = pagina_actual.anterior # El penúltimo nodo se convierte en la nueva cola.

                if self.actual == pagina_actual: # Si el puntero de la ubicación actual está en el nodo a eliminar.
                    self.actual = pagina_actual.anterior # Mueve el puntero 'actual' hacia atrás.

                print(f"Página '{pagina_actual.titulo}' eliminada.") # Informa que la página fue eliminada.
                return # Termina la función.
            pagina_actual = pagina_actual.siguiente # Pasa al siguiente nodo en la lista.
        print(f"No se encontró la página con la URL: {url}") # Si el bucle termina, no se encontró el nodo.

    # e. Buscar una página por URL o título.
    def buscar_pagina(self, busqueda): # Método para buscar una página.
        pagina_actual = self.cabeza # Inicia el recorrido desde el primer nodo.
        while pagina_actual: # Bucle para recorrer la lista.
            if busqueda.lower() in pagina_actual.url.lower() or busqueda.lower() in pagina_actual.titulo.lower(): # Comprueba si la búsqueda está en la URL o título, ignorando mayúsculas y minúsculas.
                print("Página encontrada:") # Muestra el resultado.
                print(f"URL: {pagina_actual.url}")
                print(f"Título: {pagina_actual.titulo}")
                print(f"Fecha/Hora: {pagina_actual.fecha_hora}")
                return # Termina la función al encontrar el primer resultado.
            pagina_actual = pagina_actual.siguiente # Pasa al siguiente nodo.
        print(f"No se encontraron resultados para: {busqueda}") # Si el bucle termina, no hubo coincidencias.

    # f. Mostrar el historial completo.
    def mostrar_historial(self): # Método para imprimir la lista completa.
        if not self.cabeza: # Si la lista está vacía.
            print("El historial está vacío.")
            return # Sale de la función.

        print("Historial de Navegación:")
        pagina_actual = self.cabeza # Inicia el recorrido desde el primer nodo.
        while pagina_actual: # Bucle para recorrer la lista.
            print(f"-> URL: {pagina_actual.url}, Título: {pagina_actual.titulo}, Hora: {pagina_actual.fecha_hora}") # Imprime la información del nodo.
            pagina_actual = pagina_actual.siguiente # Pasa al siguiente nodo.

mi_historial = Historial() # instancia de la clase Historial.

# Agregar las páginas iniciales
mi_historial.agregar_pagina("google.com", "Google", "10:00 AM") # Llama al método para agregar la primera página.
mi_historial.agregar_pagina("wikipedia.org", "Wikipedia", "10:05 AM") # Agrega la segunda página, etc.
mi_historial.agregar_pagina("github.com", "GitHub", "10:10 AM")
mi_historial.agregar_pagina("stackoverflow.com", "Stack Overflow", "10:15 AM")

# a. Mostrar el historial completo inicialmente
print("--- Historial Inicial ---")
mi_historial.mostrar_historial() # Llama al método para mostrar todos los nodos en la lista.

print("\n--- Operaciones ---")

# b. Retroceder
mi_historial.retroceder() # Llama al método para mover la ubicación actual a la página anterior.

# c. Avanzar
mi_historial.avanzar() # Llama al método para avanzar una posición.
mi_historial.avanzar() # Vuelve a llamar para avanzar otra posición.

# d. Eliminar una página
mi_historial.eliminar_pagina("wikipedia.org") # Llama al método para eliminar el nodo con la URL de Wikipedia.
print("\n--- Historial después de eliminar Wikipedia ---")
mi_historial.mostrar_historial() # Muestra la lista para verificar que el nodo fue eliminado.

# e. Buscar una página
print("\n--- Buscando 'github' ---")
mi_historial.buscar_pagina("github") # Llama al método para buscar la cadena "github".

print("\n--- Buscando 'Google' ---")
mi_historial.buscar_pagina("Google") # Llama al método para buscar la cadena "Google".
