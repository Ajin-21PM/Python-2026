mis_notas =[
    float(input("Ingrese su primera nota: ")),
    float(input("Ingrese su segunda nota: ")),
    float(input("Ingrese su tercera nota: ")),
    float(input("Ingrese su cuarta nota: ")),
    float(input("Ingrese su quinta nota: ")),
]
mis_notas=list(mis_notas)
nota_maxima = max(mis_notas)
print(nota_maxima)
nota_minima = min(mis_notas)
print(nota_minima)
promedio = (mis_notas[0],mis_notas[1],mis_notas[2],mis_notas[3],mis_notas[4])