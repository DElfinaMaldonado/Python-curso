
#Se les conoce como variables poruqe su valor puede cambiar
#Las variables se dceclaran y despues de definen

a = 5
b = 4
c = a + b
print (c)


nombre = "Delfis Maldonado"
print (nombre)

#Si realizo lo siguientge la varaible nombre tomara el utimo valor que se le da porque puede cambiar
#En este caso la varaiable nombre tendra el valor de maldonado
nombre = "anita"
nombre = "delfis"
nombre = "maldonado"
print (nombre)

#Ejemplo con numero #
#El (+) adlentae del ihual, significa que el valor que ya tiene mas lo que este despues del =
numero = 10
numero += 1
print (numero)


#CONCATENAR CON + #
#CONCATENAR: Es unir dos strings #
nombre = "Lucas"
#Ya se hizo la concatenacion
#El espacio que se le da es otro caracter
bienvenida = "Hola " + nombre + " Como estas"
print(bienvenida)

#CONCATENAR CON f.strings #
#.format #
#Esto se puede ocupar para dar espacio (f strings)
#Pero si agrego un numero o un true no genera error. Ya que toma un dato y lo convierte en texto
nombre = "Lucas"
bienvenida = f"Hola {nombre} Como estas"
print(bienvenida)

nombre = 5
bienvenida = f"Hola {nombre} Como estas"
print(bienvenida)

nombre = True
bienvenida = f"Hola {nombre} Como estas"
print(bienvenida)

# (del) se ocupa para borrar datos #
nombre = "Lucas"
bienvenida = f"Hola {nombre} Como estas"
del bienvenida
print(bienvenida)


# OPERADORES DE PERTENCIA #
# Para buscar se ocupa lo siguiente #
nombre =  True
bienvenida = f"Hola {nombre} Como estas"
print("ola" in bienvenida) #Da como salida True porque si esta ola en bienvenida

nombre =  True
bienvenida = f"Hola {nombre} Como estas"
print("Delfis" in bienvenida) #Da como salida Falseporqu no (Delfis) no esta en bienvenida

nombre =  True
bienvenida = f"Hola {nombre} Como estas"
print("hola" in bienvenida) #Da como salida False porque no esta en bienvenida con minusculas la h



# Para buscar se ocupa lo siguiente
nombre =  True
bienvenida = f"Hola {nombre} Como estas"
print("ola" not in bienvenida) #Da como salida False porque si esta ola en bienvenida

nombre =  True
bienvenida = f"Hola {nombre} Como estas"
print("Delfis" not in bienvenida) #Da como salida True porque no esta en bienvenida

#DEFINIENDO VARIABLE CON camelCase esto solo es bueno en Javascript
nombreCompletoDeTuAmiga = "Delfis"
print (nombreCompletoDeTuAmiga)
#DEFINIENDO VARIABLE CON snake_case esto solo es bueno en Python
nombre_completo_de_tu_amiga = "Delfis"
print (nombre_completo_de_tu_amiga)