#Ejercicio de calculadora
print("Bienvenidos a la calculadora")
print("Las operacion son: suma, resta, multi y div ")
print("Para salir escriba salir")

resultado=""

while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es: {resultado}")




# while True:
#     if resulto != "":
#         numero = resulto
#     else:
#         numero = input("Ingresa un numero")
#     if numero != "":
#         operacion = input("Ingresa una operacion")
#         if operacion != "":
#             numero2 = input("Ingresa un segundo numero")
#             if operacion=="+":               
#                 resulto = int(numero)+int(numero2)
#             else:
#                 if operacion == "-":
#                     resulto = int(numero) - int(numero2)
#                 else:
#                     if operacion == "*":
#                         resulto = int(numero) * int(numero2)
#                     else:
#                         resulto = int(numero) / int(numero2)

#             print("El resultado es:", int(resulto))
#     else:
#         numero = input("Ingresa un numero")    
#     if numero.lower() == "Salir":
#         break




