#En este ejemplo se creo una funcion en donde se pasan diferentes argumentos pero indicando el nombre del campo con su valor que va tener
#cuando queremos consultar el parametro se debe indicar el nombre del parametro a consultar, ya se id, name o desc en este caso,
#cuando se crea este tipo de casos se deben declarar el parametro en la funcion con doble **(asterisco)
#ya que es una funcion kwargs
def get_product(**datos):
    print(datos["id"] , datos["name"], datos["desc"])

get_product(id="1", name="iPhone", desc="Esto es un iphone")