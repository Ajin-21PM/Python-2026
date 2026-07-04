
tiempo_de_respuesta = [
float(input("Ingrese el primer tiempo de respuesta: ")),
float(input("Ingrese el segundo tiempo de respuesta: ")),
float(input("Ingrese el tercer tiempo de respuesta: "))
]
primer_tiempo = tiempo_de_respuesta[0]
segundo_tiempo = tiempo_de_respuesta[1]
tercer_tiempo = tiempo_de_respuesta[2]

tiempo_promedio = (primer_tiempo + segundo_tiempo + tercer_tiempo)/3

tiempo_max = max(tiempo_de_respuesta)

tiempo_min = min(tiempo_de_respuesta)

brecha_de_rendimiento = tiempo_max - tiempo_min

print(f"el tiempo de respuesta mas alto es de {tiempo_max} ms")
print(f"el tiempo de respuesta mas bajo es de {tiempo_min} ms")
print(f"El tiempo promedio es de: {tiempo_promedio: .2f} ms")
print(f"La brecha de rendimiento de los del tiempo de respuesta mas alto y mas bajo es de: {brecha_de_rendimiento: .2f} ms")