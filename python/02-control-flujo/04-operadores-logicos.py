#Operadores logicos and, or, not

gas = False
encendido= True
edad = 20

mensaje = "Puedes avanzar" if gas and encendido else "Prohibido avanzar"
mensaje1 = "Puedes avanzar" if gas or encendido else "Prohibido avanzar"
mensaje2 = "Puedes avanzar" if (gas and encendido) and (edad>17) else "No puedes avanzar"
mensaje3 = "Puedes avanzar" if not gas and (encendido or edad>17) else "No puedes avanzar"
mensaje4 = "Puedes avanzar" if not gas and encendido and edad>17 else "No puedes avanzar"

print (mensaje)
print(mensaje1)
print(mensaje2)
print(mensaje3)
print(mensaje4)

