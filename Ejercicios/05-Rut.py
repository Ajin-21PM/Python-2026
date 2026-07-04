rut_original = "   19.543.872-K   "

rut_sin_espacios = rut_original.strip()

rut_limpio = rut_sin_espacios.replace(".", "")

largo_rut = len(rut_limpio)

print(f"RUT original: '{rut_original}'")
print(f"RUT limpio: '{rut_limpio}'")
print(f"Largo del RUT limpio: {largo_rut}")