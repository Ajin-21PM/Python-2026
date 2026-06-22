parrafo = input("Ingresar el parrafo: ")

if parrafo == "":
    print("El texto no puede estar vacío")
else:
    lista_palabras = parrafo.split()
    tup_palabras = tuple(lista_palabras)
    
    palabra_buscar = input("Ingrese la palabra a buscar: ")
    
    repeticiones = 0
    
    for palabra in tup_palabras:
        if palabra == palabra_buscar:
            repeticiones = repeticiones + 1
            
    if repeticiones > 0:
        print("La palabra aparece", repeticiones, "veces.")
    else:
        print("La palabra no esta en el texto ingresado.")