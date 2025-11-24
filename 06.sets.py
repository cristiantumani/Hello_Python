### Sets ###
# Un conjunto es una colección desordenada de elementos únicos.
my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set)) # Esto crea un diccionario, no un set
my_other_set = {'Cris', 40, 1.85, 'Tumani'}
print(type(my_other_set))

print(len(my_other_set)) # Longitud del set

my_other_set.add('Chile') # Agregar un elemento
print(my_other_set)
#un Set no es una estructura ordenada, por lo que no se puede acceder a sus elementos mediante un índice
# print(my_other_set[0]) # Esto generaría un error
my_other_set.add('Cris') # Agregar un elemento duplicado (no se añadirá)
print(my_other_set)

print('Cris' in my_other_set) # Verificar si un elemento está en el set (True   o False
print('Argentina' in my_other_set)
my_other_set.remove('Chile')
my_other_set.clear() # Eliminar todos los elementos del set
print(my_other_set)
del my_other_set # Eliminar el set completo

my_set = {'Cris', 40, 1.85, 'Tumani'}
my_list = list(my_set) # Convertir set a lista
print(my_list)

my_other_set = {'Español', 'Ingles', 'Portugues'}
my_set = my_set.union(my_other_set) # Unión de sets
print(my_set)
my_set = my_set.union({'Aleman', 'Frances'}) # Unión con otro set
print(my_set)
print(my_set.difference(my_other_set)) # Diferencia entre sets


