#En este ejemplo se estan consultando o consumiendos dos funciones diferentes, aun que la variable de cada funcion
#obtenga el valor diferente, esto se debe al alcance de esta funcion es decir, solo se muestra lo que esta dentro de cada funcion

def saludar():
    saludo="Hola Mundo"
    print(saludo)

def saludarChanchito():
    saludo="Hola Chanchito"
    print(saludo)

saludar()
saludarChanchito()
saludar()

#En el siguiente ejemplo va ser de una variable global es decir que se declara fuera de la funcion
#y es utilizada por cada funcion con valor diferente, aqui si cambia el valor de la variable saludo
#es recomendable no utilizar variables globales, ya que se valor puede ser 
# cambiado por alguna funcion es decir: puede pasar de entero a string o a otro tipo de dato
saludo = "Hola sol"
def saludar():
    global saludo
    print(saludo)
    saludo="Hola Mundo"    
    print(saludo)

def saludarChanchito():
    saludo="Hola chanchito"
    print(saludo)




saludar()
saludarChanchito()


