notas=[
float(input("Ingrese la primera nota: ")),
float(input("Ingrese la segunda nota: ")),
float(input("Ingrese la tercera nota: "))
]
lista = [notas]

promedio_final = [( lista[0] * 40/100) + (lista[1] * 40/100) + (lista[3] * 20/100)]

print(f"Primer laboratorio: {promedio_final[0]}")
print(f"segundo laboratorio: {promedio_final[1]}")
print(f"tercer laboratorio: {promedio_final[1]}")