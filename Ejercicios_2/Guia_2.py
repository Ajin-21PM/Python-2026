num = 0

termino1 = 500
termino2 = 456  

print("De 500 + 456 + 510 + 454 + 520 + 452 + ... hasta + 800")
while termino1 <= 800:
    num += termino1
    
    if termino1 == 800:
        break
        
    num += termino2

    termino1 += 10
    termino2 -= 2
print(f"La sumatoria total de la serie es: {num}")