print("1. Hamburguesa")
print("2. Pizza")
print("3. Completo Italiano")

opcion = input("Ingrese una de las 3 opciones: ")

match opcion:#Esta funcion match funciona de la 3.9
    case "1":
        print("Has seleccionado una hamburguesa. Precio: $5000")
    case "2":
        print("Has seleccionado una pizza. Precio: $7500")
    case "3":
        print("Has seleccionado una completo italiano. Precio: $2500")
    case _:
        print("Opcion no valida, Ingrese una de las 3 opciones: ")

mes = 4 
match mes: 
    case 12|1|2: 
        print("Verano")
    case 3|4|5:
        print("Otoño")
    case 6|7|8:
        print("Invierno")
    case 9|10|11:
        print("Primavera")
    case _:
        print("Mes invalido crack")

hora = 18 
match hora:
    case h if 0 <= h < 6:
        print("Buenas madrugradas")
    case h if 6 <= h < 12:
        print("Buenas dias")
    case h if 12 <= h < 18:
        print("Buenas tardes")
    case h if 18 <= h < 24:
        print("Buenas noches")
    case _:
        print("Hora invalida")

x=[1,2,3]
match x:
    case [a,b,c]: #desagrupado valores de la lista x
        print(f"Elemntos de la lista x: {a}, {b}, {c}")

datos = {
    "nombre": "Victor", 
    "edad": 31
}
match datos:
    case{"nombre": n, "edad": e}:
        print(f"Nombre: {n}, Edad: {e}")

#guards
#ejemplos: saber si un numero es par o impar
