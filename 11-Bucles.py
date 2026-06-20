from colorama import init, Fore
init()
print(Fore.YELLOW + "===Bucles===")

# Bucle while
edad = 15
num = 0
#while edad < 18:
#    print("Eres menor de edad, no puedes manejar") #bucle Infinito


#while True:
#    print(num)
#    num = num + 2    #num +=2

#Bucle While
#Impresion de numeros de 0 al 100 (Incrementando de 2 en 2)
while num <= 100:
    print(num)
    num += 2
print(Fore.RED + "PRIMER BUCLE TERMINADO")

#IMPRESION DE NUMEROS DE 100 AL 200 + condicion ELSE
#el else esta igual al while
while num <= 200: 
    print(num)
    num += 2
else:
    print("Mi condicion es igual o mayor a 200")
print(Fore.BLUE + "Segundo bucle terminado")

# Combinar while con un IF dentro

while num <= 300: 
    print(num)
    num +=2
    if num == 250:
        print("mi condicion es igual a 250")
print(Fore.GREEN + "Tercer bucle terminado")

# Utilizar el Break
while num <= 400:
    print(num)
    num += 2
    if num == 350: 
        print(Fore.MAGENTA + "Se detiene el bucle")
        break
print(num)
print(Fore.MAGENTA + "cuarto bucle terminado")


#Utilizar el continue

num = 0
while num <= 50:
    print(num)
    num += 1
    if num == 40:
        continue
    print(num)

#while True:
#    parametro = input(">>> Ingrese la palabra secretas:")
#    if parametro == ("exit"):
#        break
#    else:
#        print(parametro)

credits
#Bucle FOR
#For n° 1 
print(Fore.GREEN + "====BUCLE FOR====")
for i in (1,2,3,4,5,6,7,8,9,10): 
    print(i)

#Iterando una lista (2° for)
listita = [1,2,3,4,5,6,7,8,9,10] 
for i in listita: 
    print(i)

#Iterando de una tercera forma(3° For)

print(Fore.MAGENTA + "n\3° BUCLE FOR ")
for i in range(1,101):
    print(i)
    