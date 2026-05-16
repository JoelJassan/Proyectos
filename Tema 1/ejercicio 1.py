# Ejercicio 1.a. Defincion e inicializaciones de variables escalares
print("\n ----- EJERCICIO 1.a. --------------------------------------------------------- \n")

a=5
A=7
b=8
B=11

print("Variables:",a,A,b,B)

# Ejercicio 1.b. Definición de un vector fila y dos vectores columna
print("\n ----- EJERCICIO 1.b. --------------------------------------------------------- \n")
#print(type(v))  #para ver el tipo de variable
#print(v.shape) #para ver las dimensiones

import numpy as np

#listas (sin comportamiento matemático)
v = [1, 3, 7, 0]
w = [[5], [6], [2]]
x = [[0], [-2], [3], [7]]

#vectores
v = np.array(v)                #fila 1x4. Esto hace v=[[1,3,7,0]]. Los corchetes agregan una dimension extra
w = np.array(w)                #columna 3x1
x = np.array(x)                #columna 4x1

#matrices
v = np.array([v]) #o v = np.array([1, 3, 7, 0]) directamente #matriz 1x4
#w = np.array([w])
#x = np.array([x])

#transponer vector columna
xt = np.transpose(x)                #fila 1x3

print("VECTORES:\n v: ", v,"\n w: ",w,"\n x: ",x,"\n xt: ",xt,"\n \n")

# Ejercicio 1.c. Producto ordinario y de vectores
print("\n ----- EJERCICIO 1.c. --------------------------------------------------------- \n")


print ("PRODUCTOS:\n")
print("a*A (producto escalar): \n",a*A,"\n") #escalares
print("v*x (python multiplica cada elemento del v por cada elemento de x): \n",v*x,"\n") #no es producto vectorial
print("v@x (producto vectorial): \n",v@x,"\n")  #1x4 @ 4x1 = 1x1
print("A partir de aqui, los productos vectoriales se hacen con @...")
print("x*v: \n",x@v,"\n") #4x1 @ 1x4 = 4x4
M = w @ v #3x1 @ 1x4 = 3x4
print("M=w*v: \n",M,"\n")
#print("v*w: \n",v@w,"\n") #1x4 @ 3x1 distintas dimensiones
N = M @ x #3x4 @ 4x1 = 3x1
print("N=M*x: \n",N,"\n")
wt=np.transpose(w)
P = wt @ M #1x3 @ 3x4 = 1x4
print("P=wt*'M: \n",P,"\n")

# Ejercicio 1.d. Extracción de un elemento de una matriz o vector
print("\n ----- EJERCICIO 1.d. --------------------------------------------------------- \n")
#Las variables están como matrices, por lo que tengo que acceder al elemento con dos indices.

# 1- Extraer 1er elemento de v
print("1er elemento de v:",v[0][0])
# 2- Extraer 3er elemento de v
print("3er elemento de v:",v[0][2])
# 3- Extraer M[2,3]
print("M[2,3]:",M[1][2])
# 4- Extraer 11vo elemento de M
print("Elemento 11:",M.item(10))
