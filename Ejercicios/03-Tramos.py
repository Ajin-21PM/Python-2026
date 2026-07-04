
tramo_1 = 50 + 30j
tramo_2 = 40 - 10j

impedancia_total = tramo_1 + tramo_2

print(f"Impedancia total: {impedancia_total}")

parte_real = int(impedancia_total.real)
parte_imaginaria = int(impedancia_total.imag)

print(f"Parte real (Resistencia): {parte_real}")
print(f"Parte imaginaria (Reactancia): {parte_imaginaria}")