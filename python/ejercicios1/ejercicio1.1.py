#promedio de duracion
otros_curso_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos, es la basura del video y es lo que se recorta
crudo_promedio = 5
crudo_dalto = 3.5

#Diferenecias de duracion
diferenciaa_con_min = 100 - dalto_curso / otros_curso_min * 100
diferenciaa_con_max = 100 - dalto_curso / otros_cursos_max * 100 #Nos da de resultado 78.57142857142857 para hacer que nos de el numero entenero y no en decimal se aplica la doble division //
diferenciaa_con_max = 100 - dalto_curso // otros_cursos_max * 100 #Aqui ya ase aplican la doble division paa que nos de e resultado en entero
diferenciaa_con_max = 100 -  dalto_curso  *1000 // otros_cursos_max / 10 # al hacer esta operaccion ya nos agrega una coma en el decimal 78.6
#El 1000 lo que agrega tres ceros al resultado. Entonces, si el resultado de la división es 25.7, con // obtienes 25.
diferenciaa_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
print("-------------------")

#Calculando el procentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 -  otros_cursos_promedio  *1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 -  dalto_curso *1000 // crudo_dalto/ 10
print("-------------------")

#Mostrando las fdiferenciad de duracion (ejercicico A)
print(f'El curso de Dalto dura un {diferenciaa_con_min} % menos que el mas rapido')
print(f'El curso de Dalto dura un {diferenciaa_con_max} % menos que el mas lento')
print(f'El curso de Dalto dura un {diferenciaa_con_promedio} % menos que el mas promedio')
print("-------------------")

#Mostrando la acantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso pormedio elimina {tiempo_vacio_promedio} % de tiempo vacio')
print(f'Este curso elimino el  {tiempo_vacio_dalto} % de tiempo vacio')
print("-------------------")


#Mostrando difrencias si los cursos duran 10 horas
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'ver 10 horas de este curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de otros cursos')
print("-------------------")