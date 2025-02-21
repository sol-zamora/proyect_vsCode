#Set significa grupo o conjunto
#No se puede repetir y tampoco esta ordenado. 
#Para declar un set se deben de utilizar llaves que abren y cierran
#ejemplo

#Si un set tiene numero duplicados como en ejemplo lo que hace python es solo mostra uno de esos numero duplicados
primer = {1,1,2,2,3,4,5,6} #creacion de un set
print(primer)

#Los set se trabajan como se trabajan las listas
primer.add(7) #Se pueden agregar elementos a un set
primer.remove(1) #Se pueden quitar elementos a un set
print(primer)

#una lista se puede convertir en un set, como en el ejemplo siguiente
segundo = [3,4,8] #Creacion de lista
segundo = set(segundo) #De esta manera se convierte una lista en un set
print(segundo)

#con los set se pueden hacer uniones de mas de un set, para obtener todos los elementos de estos
#en python este signo "|" se le conoce como unión
#en python este signo "&" se le conoce como interseccion
#en python este signo "-" se le conoce como diferencia
#ejemplo
print(primer | segundo) #Cuando se une set se quitan los numeros que estan suplicados, solo muestra lo de ellos

#Operador de interseccion, este lo que devuelve solo son los elementos que se encuentran en ambos set
print(primer & segundo)

#Operador de diferencia, calcula la diferencia entre dos set, es decir quita los elementos que se encuentran en ambos set
#pero tomando en cuenta el primer set que se pase es decir el de la izquierda, tambien si hay un elemento que solo se encuentra en un set
#no se toma en cuenta, los elementos que se muestran deben de estar en ambos
print(primer - segundo)

#Operador de diferencia simetrica, este simbolo se llama karet "^" el cual se obtiene con la tecla alt gr y tecla donde esta el acento
#Lo que hace la diferencia simetrica es devolver solo los elementos que no se encuentran en ninguno de los set que se estan pasando
#Los que se encuentran en ambos set se eliminan y no se muestra
print(primer ^ segundo )

#con los set no se puede acceder a un elemento que contenga
#para saber si un elemento esta dentro de un set, se debe hacer una validacion, preguntando por el valor buscado, si se entra se indica la isntruccion que se va ejecutar
if 4 in primer:
    print("Hola mundo")