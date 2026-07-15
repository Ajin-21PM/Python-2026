conceptos_repetidos = ['inmutable', 'iterable', 'inmutable', 'hashable', 'interpretado', 'iterable']

lista_ordenada = sorted(set(conceptos_repetidos))
print("Conceptos limpios:", lista_ordenada)

glosario = {
    'hashable': 'Objeto cuyo valor hash nunca cambia y puede ser clave.',
    'inmutable': 'Objeto con un valor fijo que no se puede modificar.',
    'interpretado': 'Lenguaje donde el código se ejecuta línea a línea.',
    'iterable': 'Objeto capaz de devolver sus elementos uno a la vez.'
}

print("\n--- Buscador ---")
palabra_ingresada = input("Ingrese un concepto a buscar: ").strip().lower()

definicion_encontrada = glosario.get(palabra_ingresada, "Concepto no encontrado en el glosario.")
print(f"Resultado de la búsqueda: {definicion_encontrada}")

registro_busqueda = (palabra_ingresada, definicion_encontrada)
print(f"Registro guardado en el sistema: {registro_busqueda}")