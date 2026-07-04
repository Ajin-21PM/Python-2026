precipitaciones=[
float(input("ingrese la primera precipitacion: ")),
float(input("ingrese la segunda precipitacion: ")),
float(input("ingrese la tercera precipitacion: ")),
float(input("ingrese la cuarta precipitacion: ")),
float(input("ingrese la quinta precipitacion: ")),
]
registro_lluvia = list(precipitaciones)


promedio = (precipitaciones[0] + precipitaciones[1] + precipitaciones[2] + precipitaciones[3] +precipitaciones[4])/5
print(f"el promedio de la lista es de {promedio} mm de agua")

registro_alto = max(registro_lluvia)
print(f"el registro mas alto es de {registro_alto}mm de agua")
registro_bajo = min(registro_lluvia)
print(f"el registro mas bajo es de {registro_bajo}mm de agua")

brecha_pluvial = registro_alto - registro_bajo
print(f"La brecha pluvial del registro mas alto y el registro mas bajo es de {brecha_pluvial}") 