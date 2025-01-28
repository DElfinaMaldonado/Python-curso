#get(key, default=None)
#Definición: Devuelve el valor asociado con la clave key. Si la clave no existe, devuelve default (si no se proporciona, es None).
diccionario = {'a': 1, 'b': 2}
valor = diccionario.get('a')
print(valor)  # 1
valor_no_existente = diccionario.get('c', 'No encontrado')
print(valor_no_existente)  # 'No encontrado'


#setdefault(key, default=None)
#Definición: Devuelve el valor de la clave key si existe. Si no existe, la agrega con el valor default y luego devuelve ese valor.
diccionario = {'a': 1, 'b': 2}
valor = diccionario.setdefault('b', 10)
print(valor)  # 2 (porque 'b' ya existe)
valor_nuevo = diccionario.setdefault('c', 3)
print(valor_nuevo)  # 3 (porque 'c' no existía, se agregó con valor 3)
print(diccionario)  # {'a': 1, 'b': 2, 'c': 3}


#keys()
#Definición: Devuelve un objeto vista de las claves del diccionario.
diccionario = {'a': 1, 'b': 2, 'c': 3}
claves = diccionario.keys()
print(claves)  # dict_keys(['a', 'b', 'c'])


#values()
#Definición: Devuelve un objeto vista de los valores del diccionario.
diccionario = {'a': 1, 'b': 2, 'c': 3}
valores = diccionario.values()
print(valores)  # dict_values([1, 2, 3])


#items()
#Definición: Devuelve un objeto vista de los pares clave-valor del diccionario.
diccionario = {'a': 1, 'b': 2, 'c': 3}
elementos = diccionario.items()
print(elementos)  # dict_items([('a', 1), ('b', 2), ('c', 3)])


#update(other)
#Definición: Actualiza el diccionario con los pares clave-valor de otro diccionario o iterable. Si las claves ya existen, sus valores serán reemplazados.
diccionario = {'a': 1, 'b': 2}
diccionario.update({'b': 6, 'c': 4})
print(diccionario)  # {'a': 1, 'b': 3, 'c': 4}


#pop(key, default=None)
#Definición: Elimina y devuelve el valor asociado con la clave key. Si la clave no existe, devuelve default (si no se proporciona, lanza un KeyError).
diccionario = {'a': 1, 'b': 2}
valor = diccionario.pop('b')
print(valor)  # 2
print(diccionario)  # {'a': 1}


#popitem()
#Definición: Elimina y devuelve un par clave-valor aleatorio del diccionario. Si el diccionario está vacío, lanza un KeyError.
diccionario = {'a': 1, 'b': 2}
par = diccionario.popitem()
print(par)  # ('b', 2) (esto puede variar si el diccionario tiene más elementos)
print(diccionario)  # {'a': 1}


#clear()
#Definición: Elimina todos los elementos del diccionario.
diccionario = {'a': 1, 'b': 2}
diccionario.clear()
print(diccionario)  # {}


#copy()
#Definición: Devuelve una copia superficial del diccionario.
diccionario = {'a': 1, 'b': 2}
copia = diccionario.copy()
print(copia)  # {'a': 1, 'b': 2}



#fromkeys(iterable, value=None)
#Definición: Crea un nuevo diccionario con las claves de iterable y asigna el valor value a todas las claves (el valor predeterminado es None).
claves = ['a', 'b', 'c']
diccionario = dict.fromkeys(claves, 0)
print(diccionario)  # {'a': 0, 'b': 0, 'c': 0}


#del (no es un método, pero se usa frecuentemente con diccionarios)
diccionario = {'a': 1, 'b': 2}
del diccionario['a']
print(diccionario)  # {'b': 2}
