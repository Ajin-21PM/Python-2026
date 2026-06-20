a = 10
b = 5
c = 4
d = 10

print(f"La suma entre la varianle de a y b es: {a+b}")
print(f"La resta entre la varianle de a y b es: {a-b}")
print(f"La multiplicacion entre la varianle de a y b es: {a*b}")
print(f"La division entre la varianle de a y b es: {a/b}")
print(f"El modulo entre la varianle de a y b es: {a%b}")
print(f"La coeficiente entre la varianle de a y b es: {a//+b}")
print(f"La resultado de b elevado a c(5^4) es de: {b^c}")

print("hola" * (int(10*2))/2)

print(a=b)
print(a!=b)
print(a<b)
print(a>b)
print(c >= d)
print(c<=d)

bencina= True
encendido= True

edad=19

#if = si
#else= sino

#utilizando el operador AND

if bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehivulo no puede avanzar")

#utilizando el operador OR
if bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehivulo no puede avanzar")

#utlizando el NOT junto con el AND
if not bencina and encendido:
    print("el vehiculo puede arrancar")
else:
    print("el vehiculo no enciende")

#utilizando el operador NOT junto al operador AND y OR

if(not bencina or encendido) or (encendido and edad >= 18):
    print("el vehiculo puede arrancar")
else:
    print("el vehiculo no puede arrancar")