print("Ingreso de Notas")
nota1 = float(input("Ingresa la nota del Laboratorio 1: "))
nota2 = float(input("Ingresa la nota del Laboratorio 2: "))
nota3 = float(input("Ingresa la nota del Laboratorio 3: "))
nota_producto = float(input("Ingresa la nota de la Evaluación de Producto: "))

lista_notas = [nota1, nota2, nota3]

promedio_proceso = (lista_notas[0] * 0.40) + (lista_notas[1] * 0.40) + (lista_notas[2] * 0.20)

promedio_final = (promedio_proceso * 0.60) + (nota_producto * 0.40)

print("\n--- Reporte de Notas ---")
print(f"Laboratorio 1 (40% del Proceso): {lista_notas[0]}")
print(f"Laboratorio 2 (40% del Proceso): {lista_notas[1]}")
print(f"Laboratorio 3 (20% del Proceso): {lista_notas[2]}")
print(f"Promedio Final: {round(promedio_final, 1)}")