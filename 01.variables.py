#el sistema ya tiene cargadas ciertas variables por defecto#
'Las variables se nombran solamente con texto, numeros y guion bajo'
'Buenas Practicas'
'escribir todo en minusculas y separar palabras con guion bajo'
'ejemplo my_string_variable'
my_string_variable = "Hola mundo"

#ejemplos de variables
my_string = "Hola mundo" #cadena de texto
my_int = 5 #entero
my_float = 3.43 #flotante
my_bool = True #booleano
#imprimir las variables
print(my_string)
print(my_int)
print(my_float)
print(my_bool)

#Concatenacion de cadenas de texto
'se puede impromir varias variables en una sola linea si separamos cada variable con una coma'
print(my_string, my_int, my_float, my_bool)
print(type(print(my_string, my_int, my_float, my_bool)))
print("El valor de la variable my_string es:", my_string)

#Funciones del sistema
print(len(my_string)) #len() nos devuelve la longitud de una cadena de texto

#Variables en una sola linea
name, surname, edad = 'Cristian', 'Tumani' , 40
print(name)
print(name, surname, edad)

#Inputs
#uno de los inconvenientes de py es que se pueden cambiar los types de las variables

#forzar el tipo de dato
address : str = "mi_direccion"
print(address) 
type(address)

#pero igual se puede cambiar
address = 45 
print(address)
print(type((address)))


