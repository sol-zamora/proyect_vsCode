#una tupla es lo mismo que una lista, solo que las tuplas no se pueden modificar o eliminar las tuplas que ya existen
#para declarar una tupla se deben utilizar los parentesis redondos
#Las operaciones que no permiten las tuplas son pop, append
numeros = (1,2,3,4,5,6) #esta es una tupla creada con numeros
print(numeros)

#a una tupla se le puede agregar otra tupla ejemplo
#Las tuplas se utlizan cuando no se quiere modificar nungun elemento de estas
numeros2 = (1,2,3,4,5,6) + (8,9,10)
print(numeros2)

#Para transformar un listado a un tupla se debe llamar a la funcion TUPLE
#EJEMPLO: aqui se crea una tupla de una lista
punto = tuple([1,2]) #Convertir una lista a una tupla
print(punto)
menosNumeros = numeros[:2] #esta operacion lo que hace es crear una nueva lista atraves de una tupla, ya que la tupla original no se puede modificar
print(menosNumeros)

#Tambien se puede desempaquetar las tuplas
primero, segundo, *otros = numeros
print(primero, segundo, otros)

#Tambien se puede iterar una tupla
for n in numeros:
    print (n)

#Si por alguna razon se quiere modificar una tupla, se debe pasar a una lista, para que pueda se modifica
listaNumeros = list(numeros)  #Aqui se convierte una tupla a una lista

#Despues de convertir la tupla a una lista, ya se puede modificar pero la lista no la tupla
listaNumeros[0]= "como estas"
print(listaNumeros) 