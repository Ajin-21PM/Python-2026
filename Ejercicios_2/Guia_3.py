sueldo_chile = 529000

ventas_de_vendedores = {
    "Francisco": [350000, 400000, 200000, 300000, 350000],
    "Miguel": [200000, 250000, 250000, 200000, 200000],
    "Lyan": [100000, 100000, 150000, 100000, 100000]
}


for vendedor, ventas_diarias in ventas_de_vendedores.items():
    ventas_final = sum(ventas_diarias)
    promedio_ventas = ventas_final / len(ventas_diarias)
    
    bono = 0
    if ventas_final > 1500000:
        bono = sueldo_chile * 0.20
    elif ventas_final > 1000000:
        bono = sueldo_chile * 0.10
    elif ventas_final > 500000:
        bono = sueldo_chile * 0.05
        
    sueldo_total = sueldo_chile + bono
    
    print(f"-Reporte de {vendedor}-")
    print(f"Total ventas semanales: ${ventas_final}")
    print(f"Promedio diario: ${promedio_ventas:.0f}")
    print(f"Bono correspondiente: ${bono:.0f}")
    print(f"Sueldo final a pagar: ${sueldo_total:.0f}")