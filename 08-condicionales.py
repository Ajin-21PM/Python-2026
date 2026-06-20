from colorama import init, Fore
init()
print(Fore.RED + "Texto Rojo")
print(Fore.BLUE + "Texto Azul")
print(Fore.MAGENTA + "Texto Magneta")
print(Fore.YELLOW + "Texto Amarillo")

print(Fore.MAGENTA + "\n ==== Utilizando IF y ELSE ====")
licencia = True
edad= 19
automovil = True

if license:
    print(Fore.YELLOW + "Puede conducir un automovil ya que es mayor de edad y tiene licencia")
else:
    print(Fore.YELLOW + "No puede conducir un automovil porque no es mayor de edad y no tiene licencia")

#Utilizar el comando ELIF
if licencia and edad >= 18: 
    print("puede conducir porque es mayor de edad")
elif automovil: #en otros lenguajes como C, elif = else if
    print("Tegno automovil, pero no tengo licencia ni la edad necesaria para conducir")
else:
    print("No puedo conducir, ya que no tengo la edad, ni la licencia, ni el automovil")


if licencia and edad >= 18: 
    print(Fore.BLUE + "puede conducir porque es mayor de edad")
elif automovil: #en otros lenguajes como C, elif = else if
    print(Fore.CYAN + "Tegno automovil, pero no tengo licencia ni la edad necesaria para conducir")
else:
    print(Fore.GREEN + "No puedo conducir, ya que no tengo la edad, ni la licencia, ni el automovil")