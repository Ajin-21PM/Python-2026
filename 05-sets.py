#SETS (CONJUNTOS)

#Creando los primeros conjuntos

colores_primarios = {"Azul", "Rojo", "Amarillo"}
colores_secundarios = set({"Naranja", "Verde", "Violeta" })

print(type(colores_primarios))

colores_nuevos = {"azul", "rojo", "celeste", "azul", "rojo"}
colores_nuevos.add("cafe")
colores_nuevos.discard("cafe")
print(f"Conjuno 1: {colores_primarios}")
print(f"Conjuno 2: {colores_secundarios}")
colores_nuevos.intersection(colores_nuevos)
print(f"conjunto 3 actualizado sin el color cafe: {colores_nuevos}")
