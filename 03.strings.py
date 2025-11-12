### Strings ###
# Strings are sequences of characters used to store and manipulate text.
# They can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

my_string = "Mi string"
my_string2 = 'Mi otro string'

print(len(my_string))
print(len(my_string2))  # Length of the string
print(my_string) 
print(my_string + my_string2)
my_new_line_string ='Este es un string\ncon salto de linea' 
my_string_tab = 'Este es un string\tcon tabulacion'
my_new_line_string = '\tEste es con tabulacion'
print(my_new_line_string)

# Formateo de strings#
name, surname, age = 'Cristian', 'Tumani', 40
print('Mi nombre es {} {} y mi edad es {} años'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d años' %(name, surname, age))
print(f'Mi nombre es {name} {surname} y mi edad es {age} años') #f-string (Python 3.6+)

#Desempaquetado de caracteres#
language = 'Python'
a, b, c, d, e, f = language 
print(a)
print(b)

