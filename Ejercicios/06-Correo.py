nombre= input("ingrese su nombre: ")

nombre_sin_espacios= nombre.strip()

nombre_en_minusculas = nombre_sin_espacios.lower()

nombre_correcto = nombre_en_minusculas.replace(" ", ".")

correo_institucional = nombre_correcto + "@alumnos.ulagos.cl"

print(f"Su correo ulagos es: {correo_institucional}")