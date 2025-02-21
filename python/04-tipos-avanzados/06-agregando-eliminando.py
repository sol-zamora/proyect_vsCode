#Agregar y eliminar elementos de una lista
mascotas = ["Pelusa", "Pulga", "Felipe", "chanchito feliz", "Wolfgang"]

mascotas.insert(1, "Melvin") #El insert sirve para agregar un elemento a la lista indiciando el indice en donde se va agregar y el nombre del nuevo elemento
mascotas.append("Chanchito triste") #El append sirve para agregar un elemento al final de la lista, esto es sin tener que indicar el indice

mascotas.remove("Wolfgang") #En remove se debe indicar el elemento que se va eliminar, sin el indice
mascotas.pop() #Pop sirve para eliminar el ultimo elemento de la lista sin indicarle nada
mascotas.pop(2) #Si quiero eliminar un elemento en especial le debo indicar el indice a eliminar
del mascotas[0] #La palabra reservada "del" sirve tambien para eliminar el elemento indicado 
mascotas.clear() #clear es para limpiar una lista
print(mascotas)