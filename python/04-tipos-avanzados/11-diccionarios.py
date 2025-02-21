#Los diccionarios son un conjunto o grupo de datos que se encuentran almacenados con una llave y un valor
#Los diccionario son muy utilizados en python porque son como una base de datos
#Los diccionarios solo permite pasar una llave pero como estring no numeros
#Para declarar un diccionario se deben abrir llave que abren y cierran, simpre primero va la llave
#El valor despues de la llave puede ser cualquier cosa es decir numeros, letras, etc.
#Para declarar mas de una llave se deben de separar con ","
#cuando se ejecuta el diccionario muestra las llaves con comillas simples
#Ejemplo:

diccionario = {"x": 25, "y": "sol", "z": "Marisol Zamora Garcia"}
print(diccionario)
#Para acceder a un elemento se le debe pasar el valor de la llave pero como estring
print(diccionario["y"], diccionario["z"])

#Para agregar una nueva llave a un diccionario es indicando el nombre del diccionario ya lleve agregar y su valor
diccionario["w"] = 28 #Con esta instruccion se crea una nueva llave a un diccionario
print(diccionario)

#Para poder consultar una llave en un diccioario, primero se valida, si existe se indica las instrucciones a seguir, y asi evitamos errores
#Se le debe pasar la llave del diccionario
if "sol" in diccionario:
    print("Si existe")
else:
    print ("No existe")

#Para poder acceder a un elemento que se encuentra dentro de nuestro diccionario, para que no marque nuestra aplicacion un error o explote
#Se debe utilizar el metodo GET
#Esto es para poder acceder al valor de la llave que se le esta pasando al diccionario.
print(diccionario.get("z")) #Para acceder al valor del diccionario se debe pasar la llave siempre, si la llave no existe nos devuelve el valor de None

#Tambien se le puede pasar un valor por defecto si es que llave no existe, como un segundo argumento
#Para que no nos muestre None
print(diccionario.get("j", "No existe"))

#Para eliminar un elemento de un diccionario, se le debe pasar la llave y asi se eliminara todo el elemento incluyendo su valor
# del diccionario["w"] #esta es una manera de eliminar
del (diccionario["w"]) #Y esta es otra manera pero utilizando el metodo del entre parentesis
print(diccionario)

#Tambien se puede iterar todas las llaves con su valor dentro de python
for valor in diccionario:
    print(valor)  #Si hacemos esta validacion solo devuelve las llaves del diccionario pero no con sus valores

#Para obtener los valores que tienen las llaves se debe de pasar la llave en el for con el que estamos iterando
#Ejemplo
for valor in diccionario:
    print(valor, diccionario[valor]) #Le debemos pasar la variable valor y como otro parametro el diccionario con la variable valor que contiene la llave y entonces si muestar el valor que queremos con su llave

#Tambien hay otra manera de obtener el valor de la lleve, por medio del metodo items(), el cual nos devuelve tuplas
for valor in diccionario.items():
    print(valor)

#en las tuplas las podemos desempaquetar, para poder trabajar con sus valores, lo cual debemos indicar cada un de sus elementos
for llave, valor in diccionario.items():
    print(llave, valor)

#Estos son los usos mas reales de los diccionarios, para esto se va crear una lista para trabajar.
#Cuano se esta trabajando con una base de datos tiene que tener un identificador(key) unico, es lo mismo en python
usuarios = [
    {"id": 1, "nombre": "Marisol Zamora", "edad": 25, "pais": "Mexico"}, #Hasta aqui solo se esta agregando un registro, cuando se quieren agregar mas registros, se debe cerrar la llave y poner una "," para indicar el siguiente registro
    {"id": 2, "nombre": "Viktor Alfonso Zamora Calderon", "edad": 5, "pais": "Mexico"}, #Asi se indica que se estan agregando mas elementos o registros
    {"id": 3, "nombre": "Danna Victoria Zamora Calderon", "edad": 11, "pais": "Mexico"},
    {"id": 4, "nombre": "Evelyn Haydee Zamora Calderon", "edad": 19, "pais": "Mexico"},
]
print(usuarios)

#Para obtener la informacion de alguna propiedad o llave, tenemos que iterar el diccionario
for usuario in usuarios:
    print(usuario["nombre"]) #Aqui se le debe pasar la propiedad o la llave para obtener su valor


