#Dato Numericos - 07 de mayo de 2026

#Numeros Enteros
edad = 20
annio = 2005

#Numeros Flotantes (reales)
estatura = 1.75
peso = 90.5

#Numeros Complejos
#numero complejo utilizando la notación de j para la parte imaginaria
numero_complejo = 2 + 3j
#Otro numero complejo con la función complex 
otro_numero_complejo = complex(4, 3)

print(numero_complejo)
print(otro_numero_complejo)

#operacion aritmetica basica 
base = 8

altura = 12.5

PI= 3.14159

area = (base * altura) / 2

print(f"El area del triangulo es: {area} cm")

#formato  de salida de numeros
print(f"el numero PI tiene un valor de {PI: .4f}")

#el metodo de redondeo
print(round(area))
print(f"el area del trinagulo es de {round(area)} cm")

#Transformaciones
print(float(edad)) #Transforma el numero entero a flotante

#Cadenas de texto
carrera = "Ingenieria en Informatica"
institucion = "Universidad de los Lagos"
print(carrera[0:11]) #Imprime los caracteres desde el indice 0 hasta el 10 (11 no incluido)
print("hola" * 3)

#metodo Len() permite contar caracteres de una cadena de texto
print(len(institucion)) #Imprime la cantidad de caracteres que tiene la variable institucion





#arreglos (listas)
print("-------Arreglos (Listas)------- ")
colores = ["rojo", "verde", "azul", "amarillo"] #arreglo de stings
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #arreglo de numeros enteros
lista_mixta = [1, "hola", 3.14, True] #arreglo de diferentes tipos de datos

print(colores[0]) #Imprime el color en el indice 0 del arreglo colores
print(numeros[-1]) #Imprime el ultimo numero del arreglo numeros
print(lista_mixta)
