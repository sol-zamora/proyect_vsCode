#upper() es un metodo que existe dentro de un objeto, este metodo sirve
#para convertir el valor de la variable animal en mayusculas
#lower() lo que hace es pasar todo el valor de la variable animal a minuscula
#capitalize() convierte la primera letra del valor de la variable animal a mayuscula, dejando el resto en minusculas
#strip() lo que hace es quitar los espacios en blanco que hay al inicio del valor de la variable
animal = "SOL ZAMORA feliz"
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("z"))
print(animal.replace("ZAM","CAM"))
print("cam" in animal)
print("cam" not in animal)