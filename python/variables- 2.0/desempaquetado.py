#Desempaquetado de variables:
   #es una técnica que permite extraer valores de una colección (como una lista o una tupla) y asignarlos a variables individuales de manera rápida y sencilla.
#1. Se puede coupar para: tupla, lista y objetso.
#2. No permite desempaquetar numeros


#Ejemplo con dupla
#Creando una dupla
datos_en_tupla = ("delfis", "maldonado")
datos_en_lista = ["delfis", "maldonado"]
#desempaquetando
nombre, apellido = datos_en_tupla
#Mostrando resultado
print(nombre)