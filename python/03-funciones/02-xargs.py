def suma(a,b):
    print(a+b)

suma(5,10)

#Para crear una funcion en donde se le asignan mas de dos argumentos, se debe de declarar
#la funcion con un * antes de su parametro, con esto se convierte en una funcion iterable

def sumas(*numeros):
    resultado=0
    for numero in numeros:  #Aqui hace el recorrido de cada numero que se le paso al parametro
        resultado += numero
    print(resultado)

sumas(5,6,8,9,85,105)
