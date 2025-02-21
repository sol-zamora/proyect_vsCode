#este ejemplo no indica si el texto ingresado en la funcion es un palindromo o no
#palindromo es la misma palabra pero leida al reves, si es lo mismo se indica que es palindromo o no
#Este ejercicio fue hecho con una sola funcion.

def es_palindromo(texto):
    resultado =""
    texto = texto.replace(" ","")    
    i=1
    for textoComparado in texto:
        resultado += texto[len(texto)-i]
        i+=1
    
    if resultado.lower() == texto.lower():
        print("Es palindromo")
    else:
        print("No es palindromo") 

es_palindromo("hola mundo")

#Esta es otra forma de saber si la palabra ingresada es palindromo o no, utilizando mas de una funcion
def no_space(texto):
    nuevo_texto=""
    for char in texto: #Aqui estamos iterando char(es decir la estamos recorriendo)         
        if char !=" ":   #Aqui entra solo si no es un espacio
            nuevo_texto += char #Aqui se va concatenando cada uno de los caracteres encontrados
    return nuevo_texto #Aqui retorna el valor de la variable nuevo_texto

def reverse(texto):
    texto_al_reves=""
    for char in texto: #Aqui se esta iterando la palabra texto para ordenar cada uno de los caracteres pero al reves
        texto_al_reves = char + texto_al_reves #Aqui se hace esta instruccion para obtener el ultimo caracter
    return texto_al_reves #Aqui retorna el texto al reves obtenido

def es_palindromo2(texto):
    texto = no_space(texto) #Aqui se consulta la funcion que quita los espacios
    texto_al_reves = reverse(texto) #Aqui se consulta la funcion que ordena el texto al reves
    resultado=""
    if texto.lower() == texto_al_reves.lower() : #Aqui se compara que ambos textos sean iguales para poder saber si es palindromo o no
          resultado = "Es palindromo"
    else:
        resultado = "No es palindromo"

    return resultado #Aqui se devuelve el resultado

print(es_palindromo2("marisol"))
print(es_palindromo2("reconocer"))






