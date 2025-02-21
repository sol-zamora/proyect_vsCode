#Para estos for anidados lo que se hace es primero tomar el valor de j en un rango de 3, y se pasa al for de k en un rango de 2
#Se recorre el segundo for hasta que termina su rango, despues regresa al for primero, por eso el valor de j dos veces aparece con 0 y el valor de k es diferente
#En este ejemplo se formateo el string con la "f" al inicio
for j in range(3):
    for k in range(2):
        print(f"{j}, {k}")