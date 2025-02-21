mascotas = ["Pelusa", "Pulga", "Felipe", "chanchito feliz"]

#Aqui se valida primero que la palabra que estamos buscando existe dentro de la lista
if "Pelusa" in mascotas:
    print(mascotas.index("Pelusa")) #Si no se realiza la validacion marca error
else:
    print("No existe")
    