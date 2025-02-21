#En este ejemplo se van a utilizar los nombre sin usar el id
usuarios = [["Chanchito", 5],["Peppa", 8], ["Hachi", 10], ["Negra", 3], ["sacha", 1]]

nombres = [] #Asi se crea una lista vacia
#Para obtener solo la descripcion de la lista y no el id, vamos a crear una funcion para obtener este dato agrendola a la nueva lista de nombres que se creo,
#pasandole el index de la lista usuarios que queremos obtener
for usuario in usuarios:
    nombres.append(usuarios[0])
print(nombres)

#La forma anterior es un mas larga, hay otra forma mas simple, que es la siguiente
# estos son los valores que tenemos que pasar "expresion for item in items", en el ejemplo usuario[0] es el nombre del item que se creo para el usuario buscando en la lista de usuarios
#esta es una transformacion = map, obtener solo el elemento que queremos
nombres2 = [usuario2[0] for usuario2 in usuarios]
print(nombres2)

#aqui se va filtrar los elementos de la lista de usuarios, pero solo si el id de la lista es mayor a 2, los otros descartarlos
#esto es un filtrado = filter
nombres3 = []
nombres3 =[usuario3 for usuario3 in usuarios if usuario3[1] > 2]
print(nombres3)

#A continuacion de va filtrar y transformar una lista, aqui solo se obtienen los nombres de los elementos que tiene el id mayor a 5
nombres4 = []
nombres4 =[usuario4[0] for usuario4 in usuarios if usuario4[1] > 5]
print(nombres4)

#En el siguiente codigo se muestra como utilizar el MAP para poder transformar
nombres5 = list(map(lambda usuario5: usuario5[0], usuarios))
print(nombres5)

#En el siguiente codigo se muestra como utilizar FILTER para el filtrado de la lista
nombres6 = list(filter(lambda usuario6: usuario6[1]>=8, usuarios)) #Aqui se va obtener una lista en donde el id del usuario sea mayor a 2
print(nombres6)