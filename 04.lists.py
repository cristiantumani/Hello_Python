### Listas ###
my_list = list()
my_other_list = [] #  Crear una lista vacía usando la función list()
print(len(my_list)) # Longitud de la lista (debería ser 0)
my_list = [1,2,3,4,5]
print(len(my_list))
my_other_list = [40, 'Cris', 1.85, 'Cris', 'Cris']
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
