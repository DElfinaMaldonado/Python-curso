#Cortar los elementos del índice 1 al índice 5 de la siguiente matriz:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #Salida: [2,3,4,5]
#Nota: El resultado incluye el índice inicial, pero excluye el índice final.

#Cortar elementos desde el índice 4 hasta el final de la matriz:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:]) #Salida:[5,6,7]

#Rebanar elementos desde el inicio hasta el índice 4 (no incluido):
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4]) #Salida: [1,2,3,4]

#Corte negativo #
#Rebanada desde el índice 3 desde el final hasta el índice 1 desde el final:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) #Salida: [5 6]