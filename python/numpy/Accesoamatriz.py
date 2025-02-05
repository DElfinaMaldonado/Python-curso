#Obtener el pirmer elemento del array
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0]) #Salida: 1

#Obtenga el tercer y cuarto elemento de la siguiente matriz y súmelos.
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3]) #Salida: 7. ya que suma la posicion 2 y la 3 que es 2+3 =7




#Acceso a matrices 2D
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2do elemento en la 1ra fila: ', arr[0, 1]) #Salida 2

#Acceda al elemento en la 2.ª fila, 5.ª columna:
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('55to elemento en la 2da fila: ', arr[1, 4])



#Indexación negativa #
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Último elemento del segundo array: ', arr[1, -1]) # 10