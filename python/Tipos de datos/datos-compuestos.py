#LISTAS
#Permite duplicar los lementos
lista = ["lucas", "delfis", 1.56, True, "lucas"]
print(lista)
#Si queremos mandar a llamar a un elemento se pone en tre corchetes
lista = ["lucas", "delfis", 1.56, True]
print(lista[1]) #Salida: delfis (ya que empieza en 0 )
#SI SE PUEDE MODIICAR
lista[2] = 3.45
print(lista[2])

#TUPLAS#
#Son estructuras que permiten almacenar  una coleccion de datos ordenada, pero son inmutables, es decir, no se puede eliminar, o cambiar
#En lugar de utilizar corchetes se ocupan parentesis
#Permite duplicar los lementos
tupla = ("lucas", "delfis", 1.56, True, "lucas")
print(tupla[2])
#NO SE PUEDE MODIFICAR
# tupla[2] = 3.45
#print(tupla[2])


#CREAR UN CONJUNTO (set)
#Se utiliza llaves en lugar de corchetes o celular
# 1.- Elementos únicos: No permite duplicados.
# 2.-No ordenados: El orden de los elementos no está garantizado.
# 3.-Mutables: Puedes agregar o eliminar elementos.
# 4.- Tipo de elementos: Los elementos deben ser inmutables (ej., no listas).
# 5.- No se puede acceder a elementos por medio del indice como las listas.
conjunto = {"lucas", "delfis", 1.56, True}
print(conjunto)


#CREANDO UN DICCIONARIO (dict)
#La estrcutura es key : value
#1.- Clave-Valor: Los diccionarios almacenan datos como pares de clave y valor.
#2.- Desordenado: No mantiene un orden específico (antes de Python 3.7).
#3.- Mutables: Puedes modificar, agregar y eliminar pares de clave-valor.
#4.- Claves únicas: Cada clave debe ser única, no se pueden duplicar.
#5.- Acceso rápido: La búsqueda de valores es eficiente mediante sus claves.
#6.- Tipos de claves: Las claves deben ser de tipos inmutables (ej., cadenas, números, tuplas).
#7.- En el diccionario se pide por medio de nombre en lugar de por numero
diccionario = {
    "nombre" : "delfis",
    "canal" : "delfismaldonado",
    "estas_emocionado" : True,
    "altura" : 1.56
}
print(diccionario["canal"])