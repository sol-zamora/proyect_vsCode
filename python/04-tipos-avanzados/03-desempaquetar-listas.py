#En este ejemplo se muestra como se esta desempaquetando una lista con varios elementos
numeros = [1,2,3,4,5,6,7,8,9,10]
primero, *otros = numeros  #Esta es una opcion de como asignarle a una variable el valor de cada elemento en este caso el valor de primero = 1
print(primero, otros) #Aqui se muestra el primer elemento seguido de los otros elementos que contiene la lista
primero, *otros, penul,ultimo = numeros #Aqui se indica que elementos se van a obtener
print(primero, penul, ultimo, otros)

