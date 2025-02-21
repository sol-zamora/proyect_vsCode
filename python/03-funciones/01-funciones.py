#Se va crear una funcion nuestra con la palabra reservada def

def hola():
    print("Hola Mundo!")
    print("Uktimate Python")


hola()

#La variable dentro de la funcion son los parametros
def hola2(nombre, apellido="Feliz"):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")

#Y el valor que se le asigna a la funcion al llamarla nos referimos como argumentos
hola2("Marisol", "Zamora")
#Cuando la funcion contiene dos parametros y solo se le esta pasando un argumento, lo que se hace dentro de la funcion es indicar que valor va tener por defecto el segundo parametro, en este caso va ser Feliz
hola2("Chanquito feliz")  
hola2(apellido="garcia", nombre="sol") #Aqui se le indica a la funcion cual argumento va ser el nombre y cual va ser el apellido, para que no marque error