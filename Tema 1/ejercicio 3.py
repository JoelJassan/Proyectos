'''
Variables de rango y gráficos simples  

a. Creación de variables (vectores) conteniendo rango de valores. 
    Respuesta: Ver video en link 

b. Gráficas simples: 1 dimensión. 

En este ejercicio se harán gráficas sencillas utilizando la librería matplotlib. 
    import matplotlib.pyplot as plt  

● Grafique el vector positivo. 
● En una figura distinta, vuelva a graficar el vector positivos, pero modifique el tipo 
de marcador utilizado. En este caso se propone utilizar marcadores circulares 
azules. 
● En una figura distinta, grafique el vector enteros y el vector múltiplos.
'''

import numpy as np
import matplotlib.pyplot as plt
from math import pi


print("\n ----- EJERCICIO 3.a. --------------------------------------------------------- \n")
# se crean variables en un rango de valores

positivos = np.linspace(0, 10, 11, dtype='int') #vector de 11 elementos desde 0 hasta 10
negativos = np.linspace(-4, 2, 7, dtype='int')

# quiero que devuelva los multiplos de 3 en un rango
multiplos = np.arange(0, 14, step=3)

#mismo, pero con pasos negativos
reverse = np.arange(7, 2, step=-1.5)


print("\n ----- EJERCICIO 3.b. --------------------------------------------------------- \n")
# se grafican vectores creados, de una dimensión

plt.plot(positivos, "ro")
plt.plot(reverse,"gx")
plt.show()


# se crea y grafica un sinusoide

radianes = np.arange(0, 2*pi, 1/8*pi) #defino rango de valores, eje x

seno_vector = []    #lista vacía almacenadora
for radian in radianes:
    valor_seno = np.sin(radian) #radian toma el valor temporal de radianes (analiza todo el vector)
    seno_vector.append(valor_seno)

seno_vector = np.array(seno_vector) #convierto la lista a un vector de numpy

plt.plot(radianes, seno_vector) #paso 2 vectores: posición X y Y
plt.show()


print("\n ----- EJERCICIO 3.c. --------------------------------------------------------- \n")
# se crea y grafica un cosenoidal

cos_vector = []
for radian in radianes:
    valor_cos = np.cos(radian)
    cos_vector.append(valor_cos)

cos_vector = np.array(cos_vector)

plt.plot(radianes, cos_vector)
plt.show()
