productos = [ 
"Pan", "Leche", "Pan", 
"Queso", "Leche", 
"Jugo", "Pan" 
] 
total=(len(productos))
print(total)
elementos_sinreep=(set(productos))
print(elementos_sinreep)

for i in elementos_sinreep:
    print(f"La cantidad de productos: {elementos_sinreep}")

