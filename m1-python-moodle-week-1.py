

# ESTE SERIA EL ENCABEZADO DEL PROGRAMA Y EL INCIO DE LA LOGICA
print("==========================================")
print("=====!!!BIENVENIDO A INGRESA TU ITEM!!====" )
print("========================================== ")

#AQUI INICIA LA LOGICA DEL PROGRAMA CON LAS VARIABLE DE INGRESOS  
#DECLARACION DE VARIABLES

while True:
    nombre=input( "Ingrese nombre del producto: ")
    try:
        if nombre.isalpha():
            break
        else:
            print( "El nombre del producto solo debe contener letras, por favor intente de nuevo!!")         
    except ValueError:
        print( "Ingrese un nombre valido solo letras!!")


#AQUI INICIA LA VALIDACION DE LA CANTIDAD CON UN CICLO WHILE 
while True:

    entrada_cantidad=input("Ingrese cantidad: ")
#EL bloque TRY EXCEPT PARA VALIDAR QUE EL USUARIO INGRESE UN NUMERO ENTERO
    try:

        cantidad = int(entrada_cantidad)
#VALIDACION DE QUE LA CANTIDAD SEA MAYOR O IGUAL A CERO 
        if cantidad >=0:
# SI LA CONDICION SE CUMPLE SE ROMPE EL CICLO
            break
# SI NO SE CUMPLE LA CONDICION SE MUESTRA UN MENSAJE DE ERROR
        else:
# SI LA CANTIDAD ES MENOR A CERO SE MUESTRA UN MENSAJE DE ERROR
            print( "La cantidad debe de ser un digito // porfavor intente de nuevo!!")
# SI EL USUARIO INGRESA UN VALOR NO NUMERICO SE MUESTRA UN MENSAJE DE ERROR
    except ValueError:
# SI EL USUARIO INGRESA UN VALOR NO NUMERICO SE MUESTRA UN MENSAJE DE ERROR
        print( "Ingrese una cantidad valida solo numeros enteros!!")


while True:
#AQUI INICIA LA VALIDACION DEL PRECIO CON UN CICLO WHILE
    entrada_precio=input( "Ingrese Precio: ")
#EL bloque TRY EXCEPT PARA VALIDAR QUE EL USUARIO INGRESE UN NUMERO FLOTANTE
    try:
        precio=float(entrada_precio)
#VALIDACION DE QUE EL PRECIO SEA MAYOR O IGUAL A CERO
        if precio >=0:
# SI LA CONDICION SE CUMPLE SE ROMPE EL CICLO
            break
# SI NO SE CUMPLE LA CONDICION SE MUESTRA UN MENSAJE DE ERROR
        else:
            print( "Debes de poner un precio valido!!")
# SI EL USUARIO INGRESA UN VALOR NO NUMERICO SE MUESTRA UN MENSAJE DE ERROR
    except ValueError:
# SI EL USUARIO INGRESA UN VALOR NO NUM
        print("Ingrese un precio valido!")
#AQUI INICIA EL CALCULO DEL COSTO TOTAL
#CALCULO DEL COSTO TOTAL
costo_total=precio*cantidad
#AQUI INICIA LA IMPRESION DE LOS RESULTADOS
print("="* 42)
#AQUI SE IMPRIMEN LOS RESULTADOS
print(f" Su producto es: {nombre}\n El precio fue: {precio}, \n El costo total es: {costo_total}")
#AQUI SE IMPRIME UNA LINEA DE SEPARACION
print("="* 42)
