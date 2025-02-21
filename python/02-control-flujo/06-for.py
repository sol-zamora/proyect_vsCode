#El for se utiliza para buscar elementos o realizar operaciones matematicas

for numero in range(8): #El range sirve para crear un rango de numero desde el 0 hasta el numero 4
    print(numero, numero * 'hola mundo ') #Si yo le coloco la variable numero seguida de una cadena, lo que va ser es que va multiplicar el valor del numero por la cadena escrita a su lado

#El siguiente codigo busca el numero 3 en un rango de 0 al 4, si lo encuentra nos avisa y termina la busqueda
#La palabra reservada "range()" es iterable, lo que significa que recorre cada uno de sos elementos, dependiendo el rango que se coloque
buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontre el numero buscado")


for char in "Ultimate python":
    print(char)