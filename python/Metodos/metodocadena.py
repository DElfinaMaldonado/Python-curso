#Los metodos son DATO . metodo
cadena1 = "Hola soy delfis"
cadena2 = "Hola mundo"
#dir
resultado = dir(cadena1) #(dir) Es una funcion Te da una visión de lo que puedes hacer con un objeto o en un entorno en particular.
#Imprimir resultado
print(resultado)


#upper Es un metodo y se ejecuta de la siguiente manera
resultado1 = cadena1.upper() #(upper) Devuelve el valor de la variable pero en mayusculas.
#Imprimir resultado
print(resultado1)


#lower
resultado2 = cadena1.lower() #(lower) Conveierte todo en minusculas
#Imprimir resultado
print(resultado2)


#capitalize
resultado3 = cadena2.capitalize() #(capitalize) Pone la primera letra en mayusucula
#Imprimir resultado
print(resultado3)


#find, si no encuentra nada devuelve -1
resultado4 = cadena1.find("Hola") #(find) Devueleve la psoicion en donde se enecuntra el valor en este caso 0
resultado5 = cadena2.find("o") #Devueleve la psoicion en donde se enecuntra el valor en este caso 1
resultado6 = cadena1.find("D")
#Imprimir resultado
print(resultado6) #Devueleve -1 ya que python es sensible a mayusculas y minusculas y como no se tiene D mayucusla devuelve -1 es lo que hace cuando no esta ese valor. 


#index, si no hay coincidencias lanza auna excepcion
resultado7 = cadena1.index("a")
print(resultado7) #Me devuelve la posicion en donde se encuntra el valor.


#isnumeric = Si es numerico devuelve True, sino devuelve False
es_numerico = cadena1.isnumeric()
print(es_numerico) #Devuelve false porque si no tenemos datos numeriocs en la cadena1


#isalpha = Si es alfanumerico devuelve True, sino devuelve False.
#El isalpha, devuelve True si todos los caracteres son letras del alfabeto (az).
#No sebe de tener espacio, acarceteres especiales o numeros
cadena3 = "Holamundo"
es_alpha = cadena3.isalpha()
print(es_alpha) #Devuelve true


#Count. Contamos las coincidencias de una cdea, dento de otra cadena, evuelbe la cantidad de coincidecias.
contar_coincidencias = cadena1.count("s")
print(contar_coincidencias) #Devuelve 2 porque hay 2 coicnidencias.


#len. Contamos cuanto scaracteres tiene una cdena.
#Es una funcion no un metodo
contar_caracteres = len(cadena1)
print(contar_caracteres) #DEvuelve 15 porque hay 15 caracteres contando los espacios


#Verificamos si una cadena empieza con otra caadena, si es asi devuelbe True
empieza_con = cadena1.startswith("H")
print(empieza_con) #Devuelve True porque si emepiza con H


#Verificamos si una cadena termina con otra caadena, si es asi devuelbe True
termina_con = cadena1.endswith("H")
print(termina_con) #Devuelve False porque no termina con H


#Remplaza un pedazo de la cadena dad, por otra dada
cadena_nueva = cadena1.replace("la","lu") #Remplazamos la por lu
print(cadena_nueva) #Devuelve Holu soy delfis

#Para separar la cadena que tenga comas por espacios
cadena4 = "hola,soy,delfina"
separar = cadena4.replace(","," ")
print(separar)

#Separar  cadenas con la cadena que le pasemos
cadena_separada = cadena4.split(",")
print(cadena_separada) #Devueleve esto ya que lo separo por cadenas ['hola', 'soy', 'delfina']
