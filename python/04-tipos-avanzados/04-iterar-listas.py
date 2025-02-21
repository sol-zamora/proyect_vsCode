#En este ejemplo se va mostrar como iterar una lista
#La funcion de enumerate muestra las tuplas de las listas en este ejemplo muestra: (0,Pelusa), (1, Pulgas)
mascotas = ["Pelusa", "Pulga", "Felipe", "chanchito feliz"]
#Este for es para obtener el nombre de cada mascota en forma de listado
for mascotita in mascotas:
    print(mascotita)

#En este for lo que se obtiene es la tupla de la lista, es decir el indice y la descripcion
for mascota in enumerate(mascotas):
    print(mascota) #Aqui se muestran todas las columnas
    print(mascota[1]) #Aqui se muestra solo la columna seleccionada