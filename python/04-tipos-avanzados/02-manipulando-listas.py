#Ejemplo de manipulacion de listas
mascotas  = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
mascotas[0] ="Perro" #De esta manera se cambia el valor del elemento de la lista, solo se debe colocar el indice de la lista que se quiere cambiar
mascotas[3] = "Capibara"
#Para obtener solo algunos elementos de la lista, se le debe indicar los indices de los elementos a obtener
print(mascotas[1:3])
print(mascotas[2:]) #Si no le indico el elemento al cual va tomar toma todo lo que esta a la derecha
print(mascotas[-1]) #Este obtiene el ultimo valor de la lista
print(mascotas[1::2]) #Esto es para que muestre el valor de dos en dos
print(mascotas)

numeros = list(range(21)) #Aqui se crea una lista que contiene 21 elementos del 0 al 20
numeros = list(range(1,21)) #Aqui se crea una lista que contiene 21 elementos del 1 al 20

print(numeros) 
print(numeros[::2]) #Aqui muestra la lista de los elementos pero de 2 en 2, osea numeros pares
print(numeros[1::2]) #Aqui muestra la lista de los elementos impares