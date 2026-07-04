codigo_identificador = input("Porfavor, ingrese su codigo identificador: ")

codigo_sin_espacios = codigo_identificador.strip()
print(f"El codigo inicial sin espacios es: {codigo_sin_espacios}")

codigo_sin_bajo = codigo_sin_espacios.replace("_","")
print(f"El codigo sin el guion es: {codigo_sin_bajo}")

codigo_mayuscula = codigo_sin_bajo.upper()
print(f"El codigo con mayusculas es: {codigo_mayuscula}")

codigo_caracteres = len(codigo_mayuscula)
print(f"Los caracteres del codigo son: {codigo_caracteres}")
