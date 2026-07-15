censo_2017 = {
    14: {
        "nombre_region": "Los Rios",
        "Superficie" : 18429,
        "habitantes" : 404432
    },
    12 : {
        "nombre_region": "Magallanes",
        "Superficie" : 1382291,
        "habitantes" : 166533
    }
}
print(f"Diccionario inicial: {censo_2017}\n")

for id_region in censo_2017:
    densidad = round(censo_2017[id_region]["habitantes"] / censo_2017[id_region]["Superficie"], 1)
    censo_2017[id_region]["densidad"] = densidad

censo_2017[14]["Capital"] = "Valdivia"
censo_2017[14]["Comunas"] = ["Río Bueno", "La Unión", "Paillaco"]
censo_2017[14]["Coordenadas_simuladas"] = (-39.8, -73.2)
censo_2017[14]["Zonas_exclusivas"] = {"Urbana", "Rural", "Fronteriza"}

censo_2017[12]["Capital"] = "Punta Arenas"
censo_2017[12]["Comunas"] = ["Cabo de Hornos", "Puerto Williams", "Porvenir"]
censo_2017[12]["Coordenadas_simuladas"] = (-59.9, -90.2)
censo_2017[12]["Zonas_exclusivas"] = {"Urbana", "Rural", "Fronteriza"}

censo_2017[12]["nombre_region"] = "Magallanes y Antártica Chilena" 

while True:
    region = input("Ingrese el ID de la region para revisar sus comunas (12 o 14). Si desea salir escriba 'salir' o 0: ")
    
    if region.lower() == "salir" or region == "0":
        print("Adios")
        break
        
    elif region.isdigit() and int(region) in censo_2017:
        id_int = int(region)
        nombre = censo_2017[id_int]['nombre_region'] 
        comunas = censo_2017[id_int]['Comunas']
        print(f"El id {id_int} corresponde a la región de {nombre}, y sus comunas son: {comunas}\n")
        
    else:
        print("ID de región no válido. Intente otra vez.\n")

print(f"Las claves del diccionario final son: {list(censo_2017.keys())}")