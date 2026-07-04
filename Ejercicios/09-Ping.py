valores_de_ping = [
int(input(f"Ingrese el primer ping: ")),
int(input(f"Ingrese el segundo ping: ")),
int(input(f"Ingrese el tercer ping: "))
]

valores_de_ping[1] = valores_de_ping[1] + 25
print(f"el pico de lag fue {valores_de_ping[1]}")
registro_ping = [valores_de_ping[0], valores_de_ping[1], valores_de_ping[2]]

promedio = (valores_de_ping[0] + valores_de_ping[1] + valores_de_ping[2])/3

print(f"el promedio de de los valores de la lista es de: {promedio: .2f}")
ping_maximo = max(valores_de_ping)
print(f"El ping maximo es de {ping_maximo}")
