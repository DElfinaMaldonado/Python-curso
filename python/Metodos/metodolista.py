#append(x)
#Definición: Añade un elemento x al final de la lista.
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]


#extend(iterable)
#Definición: Añade todos los elementos de un iterable (como otra lista o un conjunto) al final de la lista.
lista = [1, 2, 3]
lista.extend([4, 5])
print(lista)  # [1, 2, 3, 4, 5]


#insert(i, x)
#Definición: Inserta el elemento x en la posición i. Los elementos a la derecha de i se desplazan una posición hacia la derecha.
lista = [1, 2, 3]
lista.insert(1, 'a')
print(lista)  # [1, 'a', 2, 3]


#remove(x)
#Definición: Elimina la primera aparición del valor x de la lista. Si no se encuentra, lanza un ValueError.
lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)  # [1, 3, 2]


#pop([i])
#Definición: Elimina y devuelve el elemento en la posición i. Si no se pasa un índice, elimina y devuelve el último elemento de la lista.
lista = [1, 2, 3]
elemento = lista.pop(1)
print(elemento)  # 2
print(lista)     # [1, 3]


#clear()
#Definición: Elimina todos los elementos de la lista.
lista = [1, 2, 3]
lista.clear()
print(lista)  # []


#index(x[, start[, end]])
#Definición: Devuelve el índice de la primera aparición del valor x en la lista. Si el valor no se encuentra, lanza un ValueError. Puede buscar en un rango específico de la lista si se proporcionan start y end.
lista = [1, 2, 3, 2]
indice = lista.index(2)
print(indice)  # 1


#count(x)
#Definición: Devuelve el número de veces que x aparece en la lista.
lista = [1, 2, 3, 2, 2]
conteo = lista.count(2)
print(conteo)  # 3


#sort(key=None, reverse=False)
#Definición: Ordena los elementos de la lista en su lugar. key es una función que especifica una clave para ordenar, y reverse si es True invierte el orden (de mayor a menor).
lista = [3, 1, 2]
lista.sort()
print(lista)  # [1, 2, 3]


#reverse()
#Definición: Invierte el orden de los elementos en la lista.
lista = [1, 2, 3]
lista.reverse()
print(lista)  # [3, 2, 1]


#copy()
#Definición: Devuelve una copia superficial de la lista.
lista = [1, 2, 3]
copia = lista.copy()
print(copia)  # [1, 2, 3]


#len()
#Definición: La función len() devuelve la cantidad de elementos que tiene la lista (o cualquier otro objeto iterable, como tuplas o cadenas).
lista = [1, 2, 3, 4]
longitud = len(lista)
print(longitud)  # 4


