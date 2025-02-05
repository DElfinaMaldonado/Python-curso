#np es una librería muy utilizada para trabajar con matrices


#Con este codigo se imprime una matriz de una sola dimension
import numpy as np
mi_arry = np.array([1,2,3])
print(mi_arry)
print(type(mi_arry)) #type() se utiliza para obtener el tipo de un objeto. #Salida: <class 'numpy.ndarray'>
print("/*************/")

#Con este codigo se imprime una matriz sin dimension
import numpy as np
mi_arry1 = np.array(23)
print(mi_arry1) #Salida: 23
print("/*************/")

#Juntar varias matrices de dimension cero
import numpy as np
mi_arry2 = np.array([23, 81, 34])
print(mi_arry2) #Salida: arreglo unidimensional en pocas palabras es una lista o vector de elementos organizados en una sola fila
print("/*************/")

#Juntar dos matrices, es un arrgel bidimensional.
import numpy as np
mi_arry2 = np.array([[23, 81, 34],[12,5, 52]])
print(mi_arry2) #Salida: [[23 81 34] # [12  5 52]]   #tienes un arreglo que contiene dos listas dentro de una lista principal, lo que crea una estructura de dos filas y tres columnas.
print("/*************/")




#NMID #
#nmid en los arreglos en una parametros que imprime la dimension (es decir, cuántas dimensiones tiene el arreglo)
import numpy as np
#arreglo una dimension
mi_arry3 = np.array([1, 2, 3, 4, 5])
print(mi_arry3.ndim)  # Salida: 1, ya que es un arreglo unidimensional
# arreglo de dos matrices de una dimension
mi_arry4 = np.array([[1, 2, 3], [4, 5, 6]])
# Imprimir la dimensión
print(mi_arry4.ndim)  # Salida: 2, ya que es un arreglo bidimensional
print("/*************/")



# IMPRIMIR ELEMENTO QUE QUIERO Y RANGOS #
#Imprimir el elemento que quiero
import numpy as np
mi_array5 = np.array([1,2,3,4,5,6])
print(mi_array5[4]) #Salida: 5 ya que mepieza del 0
print("/*************/")

#Utilizando rangos, nos permiten agarrar varios elementos
#Si quiero agarra del elemento 2 al 5
#Se toma la posiicon del elemnto 2
import numpy as np
mi_array6 = np.array([1,2,3,4,5,6])
print(mi_array6[1:5]) #Salida: [2 3 4 5]
#Si se hiciera de esta manera no toma el ultimo elemento
print(mi_array6[1:4]) #Salida: [2 3 4] #el valor en el índice de fin no se incluye en el resultado.
print("/*************/")



#SHAPE se usa en la librería NumPy para obtener las dimensiones (tamaño) de un arreglo. Este atributo te dice cuántas filas y columnas (en el caso de matrices) o cuántas dimensiones tiene el arreglo.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)  # Salida: (5,) son los elemento que tiene el array

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.shape)  # Salida: (2, 3), 2: se teienen dos arreglos y 3: Son los elementos que tiene cada arreglo

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3.shape)  # Salida: (2, 2, 2) 2: Se teiene dos matrices bidiemnsional, 2: cada matriz teiene dos arreglos, 2:cada arreglo tiene dos elemenetos



#reshape Es un meetodo que permite reorganizar un arreglo de una forma a otra, siempre que el número total de elementos sea el mismo antes y después de la operación.
import numpy as np
arrays = np.array([[1,2,3,4], [5,6,7,8]])
print(arrays)
arrays = arrays.reshape(4,2) #Al impmirmir esto estamos diciendo que tendremos una matriz de 4 filas y 2 columnas.
print(arrays)  #Salida:[[1 2]
                       #[3 4]
                       #[5 6]
                       #[7 8]]
                       
                       
#Recorrer las filas de mi array
import numpy as np
arrayss = np.array([[1,2,3,4], [5,6,7,8]])
for fila in arrayss:
    print(fila) #Salida: [1 2 3 4]
                         #[5 6 7 8]