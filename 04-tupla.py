#duplas
#Creando una tupla de tipo string
estudiantes = ("Matias","francisco", "Alan")
print(type(estudiantes))

#Creando una tupla compleja con datos estructurados
datos = ([1,2,3,4,5], ("queilen","Castro")), ("Universidad de los lagos", "AIEP")
#Tambien se consultar la psicion de un elemnto al igual que la lista
print(datos[0])
print(f"TUPLA: {datos}\n")

lista_asignaturas = ["programcion", "quimica", "introduccion a matematicas"]
print(f"Lista:{lista_asignaturas}")
#Con las listas se puede eliminar elementos
lista_asignaturas.pop()
print(f"tupla con ultimo elemento eliminado: {estudiantes}")

"""estudiantes.pop
"""

print(estudiantes.index("Alan"))

#metodo sorted() para ordenar elementos de una tupla

print(sorted(estudiantes))
