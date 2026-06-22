n = int(input("Ingrese la cantidad de cubos que quieres calcular: "))
impar = 1

for i in range(1, n + 1):
    suma = 0
    terminos = []
    
    for _ in range(i):
        suma += impar
        terminos.append(str(impar))
        impar += 2
        
    ecuacion = " + ".join(terminos)
    print(f"{i}^3 = {ecuacion} = {suma}")