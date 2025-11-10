#Operadores en Python#
#Operadores Aritmeticos
a = 10
b = 3  
print (a+b) #suma
(a-b) #resta
(a*b) #multiplicacion
(a/b) #division
(a%b) #modulo
(a**b) #potencia
print (a % b) #el modulo nos devuelve el resto de una division
print (a // b) #division entera nos devuelve la parte entera de una division 
print (a ** b) #potencia

print ("Hola " + "Mundo") #concatenacion de cadenas de texto
#print ('Hola ' - 'Mundo') #error no se puede restar cadenas de texto
print ('Hola ' * 3) #repeticion de cadenas de texto

#Operadores de Comparacion
x = 5
y = 10
print (x == y) #igualdad
print (x<y) #menor que
print (x>y) #mayor que
print (x<=y) #menor o igual que
print (x>=y) #mayor o igual que
print (x!=y) #diferente que

print ('Hola' == 'Python') #igualdad
print ('Hola'<'Python') #menor que
print ('Hola'>'Python') #mayor que
print ('Hola'<='Python') #menor o igual que
print ('Hola'>='Python') #mayor o igual que
print ('Hola'!= 'Python') #diferente que
print ('aaaa' == 'aaaa') #True
print ('aaaa' == 'aaab') #False
#lo que compara es ordenacion alfabetica por ASCII (que es ASCII? investigar)

###Operadores Logicos###
print ( 3>4 and 'Hola' > 'Python') #AND ambas condiciones deben ser True
print ( 3>4 or 'Hola' > 'Python')

print (3<4 and 'Hola' < 'Python') #AND ambas condiciones deben ser True
print (not(3>4)) #NOT invierte el valor de la condicion
