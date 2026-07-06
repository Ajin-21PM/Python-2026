def multiplicacion(x):
    return x * 1.0
y = multiplicacion(67)
print(f"El resultado de la funcion es {y}")

def saludo(nombre):
    print(f"Holaaaa, mi nombre es {nombre}")

saludo("Miguel")

def suma(a, b):
    return a + b
resultado = suma(2, 3)
print(resultado)

def Resta(a, b=5):
    return a - b
resultado1 = Resta(6)
print(resultado1)

resultado2 = Resta(4, 4)
print(resultado2)

def calcular_potencia(base, exponente):
    return base **exponente

resultadoexp = calcular_potencia(exponente=3, base=2)
print(resultadoexp)

"""Pregunta parcial: tecnica de programacion, funcion que se llama asi mismo
caso base: Ancla de la funcion, sirve para problemas mas complejos.
Para que sirve: simplifica problemas complejos que tienen una estructura repititiva"""

def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
        return r
    print(factorial_normal(5))


def fibonacci_recursivo(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_recursivo (n-1) + fibonacci_recursivo(n-2)

print(f"5to numero de fibonacci: {fibonacci_recursivo(5)}")