class ColaCircular:
  def __init__(self, capacidad):
    self.queue = [None] * capacidad
    self.capacidad = capacidad
    self.front = 0
    self.rear = -1
    self.size = 0

  def enqueue(self, element):
    if self.size == self.capacidad:
      return "La cola está llena"
    self.rear = (self.rear + 1) % self.capacidad
    self.queue[self.rear] = element
    self.size += 1

  def dequeue(self):
    if self.isEmpty():
      return "La cola está vacía"
    elemento = self.queue[self.front]
    self.queue[self.front] = None
    self.front = (self.front + 1) % self.capacidad
    self.size -= 1
    return elemento

  def peek(self):
    if self.isEmpty():
      return "La cola está vacía"
    return self.queue[self.front]

  def isEmpty(self):
    return self.size == 0

  def getSize(self):
    return self.size



# Crear cola circular con capacidad 5
miColaCircular = ColaCircular(5)

miColaCircular.enqueue('Aldo')
miColaCircular.enqueue('Bianca')
miColaCircular.enqueue('Carlos')

print("Cola:", miColaCircular.queue)
print("Primer elemento:", miColaCircular.peek())
print("Elimina:", miColaCircular.dequeue())
print("Cola después de eliminar:", miColaCircular.queue)
print("Está vacía:", miColaCircular.isEmpty())
print("Tamaño:", miColaCircular.getSize())

miColaCircular.enqueue('Diana')
print("Cola después de agregar un nuevo elemento:", miColaCircular.queue)
print("Nuevo primer elemento:", miColaCircular.peek())
print("Tamaño:", miColaCircular.getSize())

