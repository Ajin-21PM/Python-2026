consumos_ram = [
    float(input("ingrese el primer consumo: ")),
    float(input("ingrese el segundo consumo: ")),
    float(input("ingrese el tercer consumo: ")),
    float(input("ingrese el cuarto consumo: "))
]

ram_mañana = consumos_ram[0]
ram_mediodia = consumos_ram[1]
ram_tarde = consumos_ram[2]
ram_noche = consumos_ram[3]
promedio = (ram_mañana + ram_mediodia + ram_tarde + ram_noche)/4

print(f"el promedio es de {promedio}")

diferencia = max(consumos_ram)- min(consumos_ram)

print(f"el rango de los consumos es de {diferencia}")
