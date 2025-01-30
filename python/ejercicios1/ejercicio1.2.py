frase = input("Diem un apalabara y te calculo cuanto tiempo te daraias si tuevieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabaras, y te tardaraias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Delfis lo diria en {cantidad_de_palabras/2*1.3} segundo sen decirlo')
if cantidad_de_palabras > 100:
    print("Para tampoco te pedi un testamento")