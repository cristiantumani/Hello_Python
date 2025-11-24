### Listas ###
my_list = list()
my_other_list = [] #  Crear una lista vacía usando la función list()
print(len(my_list)) # Longitud de la lista (debería ser 0)
my_list = [1,2,3,4,5]
print(len(my_list))
my_other_list = ['40', 'Cris', 1.85, 'Cris', 'Cris']
print(type(my_list))
print(type(my_other_list))

# Acceder a elementos de la lista
print(my_other_list[0])  # Primer elemento
print(my_other_list[1])  # Segundo elemento
print(my_other_list[-1]) # Último elemento
print(my_other_list[-2]) # Penúltimo elemento
#print(my_other_list[5]) # IndexError: list index out of range
print(my_other_list.count('Cris')) # Contar ocurrencias de un elemento
# Slicing (rebanado) de listas

age, name, height, name, name = my_other_list
print(age)
print(name)
print(my_list + my_other_list) # Concatenación de listas

#insertat elementos en listas#
my_other_list.append('Product Manaer') # Agregar al final de la lista
print(my_other_list)
my_other_list.insert(2, 'España') # Insertar en una posicion especifica
print(my_other_list)

my_other_list.remove('Cris') # Eliminar la primera ocurrencia de un elemento
print(my_other_list)
my_other_list.pop() # Eliminar el último elemento

my_other_list.pop() # Eliminar el último elemento
print(my_other_list)
print(my_other_list.pop())

my_pop_element = my_other_list.pop(0)
print(my_pop_element)
print(my_other_list)

print(my_other_list)
del my_other_list[1]
print(my_other_list)

# Modificar elementos de la lista
my_other_list[0] = 40.5
print(my_other_list)
my_other_list.append('Cris')
my_other_list.append('Tumani')
my_other_list.append('Chile')
my_other_list.append('España')
my_other_list.append('1985')
print(my_other_list)
del my_other_list[4]
print(my_other_list)
my_other_list[3] = 'Argentina'
print(my_other_list)

###Copy###
my_new_list = my_other_list.copy()
print(my_new_list)
my_other_list.clear()
print(my_other_list)
print(my_new_list)

###Reverse###
my_new_list.reverse()
print(my_new_list)

###Sort >> ordenar###
my_new_list.sort() #solo funciona si todos los elementos son del mismo tipo

my_number_list = [8,4,1,29,0,5,22]
my_number_list.sort()
print(my_number_list)






