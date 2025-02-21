numeros = [2,5,45,89,75,256,95,46,22,35,9,80]
numeros.sort() #sort es para ordenas nuestras listas de orden ascendente
numeros.sort(reverse=True) #Para ordenas nuestra lista de orden descendente se debe agregar dentro de sort(reverse = True) y con esto queda ordenada
numeros2 = sorted(numeros) #con sorted se crea una nueva lista a ordenar pero no afecta a la principal en este caso numeros
numeros3 = sorted(numeros, reverse=True) #Si se quiere ordenar las lista en orden descendente, debos de pasarle reverse = true, como un segundo parametro
print(numeros)
print(numeros2)
print(numeros3)

#Cuando se ordena un listado con id y descripcion lo que toma en cuenta para ordenar es ID osea el primer elemento que se pueda ordenar
usuarios = [[5,"Chanchito"],[8,"Peppa"], [10,"Hachi"], [3, "Negra"], [1, "sacha"]]
usuarios.sort()
print(usuarios)

#Pero si el primer el elemento de una lista no es ordenable ejemplo que la descripcion sea primero, no se va poder ordenar para este caso, se le tiene que pasar una funcion
usuarios2 = [["Chanchito", 5],["Peppa", 8], ["Hachi", 10], ["Negra", 3], ["sacha", 1]]
#Funcion para poder ordenar por id aun que no este en la primera posicion de la lista
def ordena(elemento):
    return elemento[1] #Le pasamos el indice del la columna que se quiere ordenar

usuarios2.sort(key=ordena) #Para que se ordene la lista debemos agregar en el metodo sort(key=ordena) la cual es la funcion nueva que se creo
usuarios2.sort(key=ordena, reverse=True)
print(usuarios2)

#para evitar estar creando funciones cada que se quiera ordenar los elementos de las listas, se va realizar de la siguiente manera
#esto es, para funciones que solo se van a utilizar solo una ves, funciones LAMBDA o anonimas
usuarios3 = [["Chanchito", 5],["Peppa", 8], ["Hachi", 10], ["Negra", 3], ["sacha", 1]]
usuarios3.sort(key = lambda elemento:elemento[1], reverse=False) #Aqui lo que se hace es evitar hacer la funcion de ordena, se pasa el key seguido del nombre del parametro dos : y el parametro con el id de la columna que se quiere ordenar
print(usuarios3)

