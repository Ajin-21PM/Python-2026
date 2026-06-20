paciente = {
    "nombre": "Benjamin",
    "edad": 18, 
    "ciudad": "Ancud",
    "fechas_atencion": [5,8,12],
    "Diagnostico": ("resfriado comun"),
    "informacion_extra":{
        "tipo_de_sangre":"A",
        "hemograma": False
    }
}
print(type(paciente))
print(f"===Ficha Paciente===\n{paciente}")

medico= dict(
    nombre="ignacio saes",
    edad=19,
    especialidades="cardiologo"
)
print(type(paciente))
print(f"---Ficha Paciente --- \n{paciente}")

#como consulto solo el nombre del paciente sin traer el diccionario completo
print(f"Nombre del paciente a consultar: {paciente["nombre"]}")

print(paciente.get("nombre"))

#none es un tipo de dato

print(paciente.get("rut", "N/D (No Data)"))

#retornar las claves, los valores o ambas como pares

print(paciente.keys()) #dict_keys(["nombre", "edad",....... ]) solo claves

print(paciente.values()) #dict_values(["Benjamin", "18", ......])

print(paciente.items()) #dict_items([("nombre", "Benjamin"),.....])

#retorna el numero de claves que tiene el diccionario
print(len(medico))
print(len(paciente))

#modificacion del diccionario

#agregar una clave nueva al diccionario paciente "%Importante%"
paciente["telefono"] = "+56912345678"
print("---FICHA PACIENTE CON TELEFONO--- \n")
print(paciente)
#sobreescribir valor de una clave existente (Forma n°1)

paciente["edad"] = 21
print("\n---Ficha de paciente con edad actualizada--\n")
print(paciente)

#Fusiona otro diccionario (o pares clave-valor) en el actual
#Util para actualizar varios campos a la vez (actualizar varias campos)

paciente.update({"edad": 21, "ciudad": "Castro"})
print(paciente["edad"])
print(paciente["ciudad"])
print(paciente)

#Eliminar una clave sin retorno
del(paciente["informacion_extra"])
print(paciente)

#eliminar una clave y retornar su valor(a diferencia de del, que no lo retorna -> pop())
edad_eliminada = paciente.pop("edad")
print(f"edad eliminada: {edad_eliminada}")  #se recupera el valor antes de borrarla
print(paciente)

#otras utilidades del diccionario

#Con in se verifica si una clave existe en el diccionario (sin usar condicionales todavia)
print("nombre" in paciente)
print("rut" in paciente)

# con copy() se crea una copia independiente del diccionario

paciente2 = paciente.copy()
paciente2["nombre"] = "javiera"
print(paciente["nombre"])
print(paciente2["nombre"])
print(paciente2)

#Con clear() elimina todos los elementos del diccionario,  dejandolo vacio (a diferencia del())
medico2 = medico.copy()
print(medico2)
medico2.clear()
print(medico2) # -> {}

n= [1,2, 3, 4, 5]
n_str= list(map(str,n))
print(f"Lista de numeros como strings: {", ".join(n_str)}") #metodo map reemplaza un bucle

ramos = ["programacion", "fisica", "Calculo", "habilidades comunicativas"]
long = list(filter(lambda x: len(x) > 7, ramos))
print(long)

a = [1, 2, 3, 4]
b = ["A", "B", "C", "D"]
comprimir = list(zip(a,b))
print(comprimir)