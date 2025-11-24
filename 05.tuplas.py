###Tuplas###
my_tuple = tuple()
my_other_tuple = ()

#una Tupla es un conjunto de valores agrupados e inmutables

my_tuple = (40, 1.85, 'Cris' ,'Tumani', 'Chile')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0]) #acceder a un elemento de la tupla
print(my_tuple[-1]) #acceder al ultimo elemento de la tupla

print(my_tuple.count('Cris')) #contar cuantas veces aparece un elemento en la tupla
print(my_tuple.index('Tumani')) #devuelve la posicion del elemento en la tupla  

#my_tuple[1] = 1.90 #TypeError: 'tuple' object does not support item assignment

#si quiero que sea mutable, la debo transformar en una lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple = tuple(my_tuple)
print(type(my_tuple))
# --- IGNORE ---


