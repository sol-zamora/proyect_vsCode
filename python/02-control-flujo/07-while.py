# Este loop es para recorrer la variable de numero hasta que este sea menor a 100, cada que entra al while se imprime el valor y
# se multiplica el valor por 2 hasta que el valor sea menor a 100 
#Ejemplo numero 1
numero = 1
while numero < 100:
    print(numero)
    numero *=2


#Ejemplo numero 2
#En este ejemplo se muestra se asigna el valor a la variable comando que ingreso el usuario, se va ir mostrando cada valor
#hasta que el usuario ingrese la palabra Salir.
# si se coloca la siguiente linea en el while se vuelve infinito while comando.lower() != "Salir": 

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower()== "salir":
        break