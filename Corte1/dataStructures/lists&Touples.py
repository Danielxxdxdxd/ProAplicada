#################LISTAS####################
#Es un tipo de dato que almacena de forma ordenada multiples tipos de datos, se define usando '[]'
#Es malneable para el usuario, osea se pueden alterar y editar en cualquier momento

print(" #########LISTAS#########", '\n')

my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Azul'] #Creando Lista de colores
print(my_lista) #Imprimiendo toda la lista
print(type(my_lista)) #Imprimiendo la clase "list"
print(my_lista[2]) #Imprimiendo el 3er elemento de la lista

print("my_lista size: ", len(my_lista)) #Imprimiendo la cantidad de elementos de la lista
print(my_lista[1:3]) #Imprimiendo los elementos de la lista que esten dentro del rango
print(my_lista[:3]) #Imprime los elementos desde el primero hasta el anterior al limite

my_lista.append('Blanco') #Agrega elemento al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro') #Agrea un elemento a la lista segun en que hubicacion se requiera
print(my_lista)


my_lista.extend(['Marron', 'Gris']) #Concatena a otra lista
print(my_lista)

print(my_lista.index('Azul')) #Imprime la hubicacion del elemento dentro de la lista

my_lista.remove('Marron') #Quita el elemento mencionado de la lista
print(my_lista)

my_lista.insert(8, 'Marron')
print(my_lista)

print(my_lista.pop()) #Imprime y elimina el ultimo elemento de la lista
print(my_lista)

my_lista_3 = my_lista*3 #Multiplica la lista
print("my_lista_3: ", my_lista_3)

print("Sort:")
my_lista.sort() #Ordena la lista (al ser String lo hace en forma alfabetica)
print(my_lista)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort() #Ordena la lista (al ser Int lo hace de menor a mayor)
print(my_NumList)
my_NumList.sort(reverse = True) #Ordena de manera inversa (en este caso de mayor a menor)
print("De mayor a menor: ", my_NumList)


#################TUPLAS####################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

print('\n', '\n', "############TUPLAS############", '\n')
my_tupla = tuple(my_lista) #Convierte una lista en tupla
print("my_tuple: ", my_tupla)

print(my_tupla[0]) #Imprime el elemento segun el valor ingresado
print(my_tupla[2])

print('Rojo' in my_tupla) #Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print(my_tupla.count('Azul')) #Cuenta la cantidad de elementos iguales al valor ingresado

my_tupla_unitaria = ('Blanco') #Crea una tupla con un solo elemento
print(my_tupla_unitaria)

my_tupla = 'Gaspar', 5, 8, 1999 #Tambien se puede crear una tupla sin el uso de '()'
print(my_tupla)

nombre, dia, mes, año = my_tupla #Desempaquetado de tupla, se guardan los valores en orden de las variables
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

my_lista2=list(my_tupla) #Convierte una tupla en una lista
print(my_lista2)
