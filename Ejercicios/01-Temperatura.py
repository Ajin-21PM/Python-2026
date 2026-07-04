#Temperatura y diferencia de Max y Min temperatura

temperatura = [12.5, 14.2, 11.8]

promedio = sum(temperatura) / len(temperatura)

print(f"El promedio de la temperatura es de {promedio: .1f}")

tem_max = max(temperatura)
tem_min = min(temperatura)

diferencia = (tem_max - tem_min)

print(f"La diferencia entre la temperatura del dia más alto y más bajo es{diferencia: .1f} grados celsius")