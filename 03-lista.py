#lista

#primera forma: declarar una lista utilizando corchetes []
lista1= ["Miguel", 20, 1.75, True]

#segunda forma: utilizando la función list()
lista2 = list(["Ana", 25, 1.65, False,102])

ramos = [] #lista vacia

n=[1,2,3,4,5]
print(lista1)
print(lista2)

#metodos para la listas
#01. Count()
print(lista1.count(1))

#contar la cantidad de concurrencias de un elemento
print(lista1.count("Miguel"))

#agregar un elemento al final de la lista
ramos.append("Quimica")
print(ramos)
ramos.append("Habilidades comunicativas")
print(ramos)
ramos.append("Programacion")
print(ramos)


#otra forma de insertar un elemnto a las lista(forma especifica)
ramos.insert(0, "Introduccion a la matematica")
print(ramos)


#modificar un elemento en especifico
ramos [2]= "Habilidades comunicativas para inginerieros/as"
print(ramos)

#Eliminar el ultimo elemento de la lista
ramos.pop()
print(ramos)

#ordenar los elementos de una lista de forma descendiente a ascendente (a, b, c, d........, z)
#print(ramos.sort())
ramos.sort()
print(ramos)

n.sort()
print(n)

#ordenas elemntos de una lista segun la cantidad de caracteres de cada elemnto
ramos.sort(key=len)
print(ramos)

#extender una lista a partir de otra
ramos_segundo_semestre = ["Ciudadania", "Algebra", "Introduccion a la Fisica"]
print(ramos_segundo_semestre)

ramos.extend(ramos_segundo_semestre)
print(ramos)

print(ramos_segundo_semestre.index("Algebra"))
