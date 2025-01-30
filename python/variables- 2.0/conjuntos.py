#Los conjuntos se pueden crar con una funcion set
#Creando un conjunto con set ()
conjunto = set(["Dalto 1", "Dalto2"])
print(conjunto)

#Cuando queremos poner un elemento modificable en otro no modificable
conjunto1 = frozenset(["dato1", "dato2"]) #frozenset: Sirve para meter un cinjunto dentro de otro cinjunto
conjunto2 ={conjunto1, "dato 3"}
print(conjunto2)


#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
#verificando si es un conjunto o no
resultado = conjunto. issubset(conjunto1)
print(resultado)

