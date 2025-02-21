#Las listas se declaran con "[]"
#Para hacer un desempaquetar una lista se debe utilizar el "*", operador de desempaquetamiento
lista = [1,2,3,4]
print(lista) #De esta manera para los valores como listas
print(*lista) #Si le pasamos el operados de desempaquetamiento, debemos pasarle el "*" seguido del nombre de la lista y con esto nos muestras sus valores asi 1,2,3,4

#Esto mismo se puede hacer con las tuplas solo se cambia a parentesis
tuplas = (1,2,3,4)
print(*tuplas) #El cual es lo mismo que las listas

#Si tenemos una funcion definida y esta recibe los arguntos n1,n2,n3.
#Le debemos pasar el argunto como un operador de sempaquetamiento y con esto ya nos mostraria su valor real
#Ejemplo: def n(*lista):

#Tambien podemos combinar listas con el operador de desempaquetamiento
lista2 = [1,2,3,4]
lista3 = [5,6,7,8]
combinar = [*lista2, *lista3] #Esto es para combinar listas con el operador de desempaquetamiento
print(combinar)

#Tambien se pueden agregar elementos al comienzo de las listas
combinar = ["Hola", *lista2, "mundo", *lista3, "sol zamora"]
print(combinar)

#esto mismo se puede hacer con los diccionarios, se van a crear dos DICCIONARIO, utilizando el operador de desempaquetamiento "**"
diccionario = {"x": 1}
diccionario2 = {"y": "sol Zamora"}
combinarDiccionarios = {**diccionario, **diccionario2} #Aqui se combina el diccionario con el diccionario2, utilizando llave "{}" y seguido de dos "**" con el nombre del diccionario
#Aqui nos va mostrar las propiedades de ambos diccionarios en una misma lista es decir: {'x':1, 'y':'sol Zamora}
print(combinarDiccionarios)

#Tambien se le pueden agregar mas llaves a los diccionarios combinados, como se muestra a continuación
combinacionDiccionariosConMasLlaves = {**diccionario, **diccionario2, "z":"29"}
print(combinacionDiccionariosConMasLlaves)

#Tambien se pueden agregar nuevas llave en medio de los diccionarios ejemplo:
combinacionDiccionariosConMasLlaves2 = {**diccionario, "lala":"Hola como estas lala", **diccionario2, "z":"29"}
print(combinacionDiccionariosConMasLlaves2)

print("FIN DEL CURSO ULTIME PYTHON PARA PRINCIPIANTES, GRACIAS SOL")
print("PARA TERMINAR VIENDO EL CURSO COMPLETO DEBO BUSCAR LA DESCRIPCION DEL VIDEO")