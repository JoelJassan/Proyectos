'''
Calcular promedios temporales  CONTENIDO TEÒRICO 
a. Genere los vectores necesarios para representar alrededor de 100 ciclos de una 
función senoidal de 20Hz y 3v de amplitud, y otra de la misma duración con una 
frecuencia de 33.57Hz y 4V de amplitud.  
i. Usando promedios temporales, calcule los valores eficaces de cada señal, y 
de la suma y de la diferencia de cada una.  
ii. Compare los resultados usando la función desviación estándar (std). b. 
Averigüe si las 2 señales del ítem a son coherentes o no.  
 
c. Defina los vectores necesarios para representar alrededor de 100 ciclos de 2 señales 
senoidales de amplitud unitaria, de la misma frecuencia, pero distinta fase.  
i. Explore cómo cambia la coherencia entre las 2 señales al ir cambiando la fase 
de una de ellas entre 0 y 90 grados.  

 '''

import numpy as np
import matplotlib.pyplot as plt
from math import pi

print("\n ----- EJERCICIO 4.a. --------------------------------------------------------- \n")


#vector de muestras cada 1/8*pi, hasta 100 ciclos
ciclos = 100

#amplitudes
amp1 = 3
amp2 = 4
#frecuencias
f1 = 20
f2 = 33.57
f_sampling = f2*20 #asociado al peor caso

#muestreo
T_sampling = 1/f_sampling
sampling_time = np.arange(0, ciclos/f1, T_sampling) #sampleo 100 ciclos de la menor frec.

#genero vectores de amplitud para signal 1 y 2
signal_1 = amp1*np.sin(2*pi*f1*sampling_time)
signal_2 = amp2*np.sin(2*pi*f2*sampling_time)

#visualización de señales
plt.plot(sampling_time, signal_1, label='Signal 1')
plt.plot(sampling_time, signal_2, label='Signal 2')
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.legend()
#plt.grid()
#plt.show()


print("\n ----- EJERCICIO 4.a.i: promedios temporales y Vrms --------------------------- \n")

print("Promedios temporales: ")

# defino variables necesarias
suma_media_1 = 0
suma_media_2 = 0
suma_promedio_1 = 0
suma_promedio_2 = 0

# total de muestras <- numero de elementos del vector n_samples
n = int(len(sampling_time) / ciclos)

# diferencial de tiempo <- tiempo entre muestras consecutivas
delta_t = sampling_time[1] - sampling_time[0]

# sumatoria de todos los elementos de (vector señal [i] * deltaT), durante UN ciclo
for i in range(n):
    suma_media_1 += signal_1[i] * delta_t
    suma_media_2 += signal_2[i] * delta_t

Vmed1 = 1/(n*delta_t) * suma_media_1
print("Vmed1 = ", round(Vmed1,2))

Vmed2 = 1/(n*delta_t) * suma_media_2
print("Vmed2 = ", round(Vmed2,2))


print("\nValores RMS:") # valor eficaz -> raiz de la potencia

for i in range(n):
    suma_promedio_1 += signal_1[i]**2 * delta_t
    suma_promedio_2 += signal_2[i]**2 * delta_t

Vrms1 = np.sqrt(1/(n*delta_t) * suma_promedio_1)
print("Vrms1 = ", round(Vrms1,2))

Vrms2 = np.sqrt(1/(n*delta_t) * suma_promedio_2)
print("Vrms2 = ", round(Vrms2,2))


print("\nSuma y diferencia de señales:")
#defino variables necesarias
suma_signal_sum_media = 0
suma_signal_diff_media = 0
suma_signal_sum_promedio = 0
suma_signal_diff_promedio = 0

signal_sum = signal_1 + signal_2
signal_diff = signal_1 - signal_2

#plt.plot(sampling_time, signal_sum, label='Signal sum')
#plt.plot(sampling_time, signal_diff, label='Signal dif')
#plt.show()

for i in range(n):
    #suma y resta media
    suma_signal_sum_media += signal_sum[i] * delta_t
    suma_signal_diff_media += signal_diff[i] * delta_t

    #suma y resta rms
    suma_signal_sum_promedio += signal_sum[i]**2 * delta_t
    suma_signal_diff_promedio += signal_diff[i]**2 * delta_t

Vmed_sum = 1/(n*delta_t) * suma_signal_sum_media
print("Vmed_suma = ", round(Vmed_sum,2))

Vmed_diff = 1/(n*delta_t) * suma_signal_diff_media
print("Vmed_diff = ", round(Vmed_diff,2))

Vrms_sum = np.sqrt(1/(n*delta_t) * suma_signal_sum_promedio)
print("Vrms_sum = ", round(Vrms_sum,2))

Vrms_diff = np.sqrt(1/(n*delta_t) * suma_signal_diff_promedio)
print("Vrms_diff = ", round(Vrms_diff,2))

'''
El ejercicio buscaba lo siguiente:
Vrms1 = amp1/np.sqrt(2)
Vrms2 = amp2/np.sqrt(2)

Vef_suma = np.sqrt(Vrms1**2 + Vrms2**2)
Vef_resta = np.sqrt(Vrms1**2 + Vrms2**2)
'''

print("\n ----- EJERCICIO 4.a.ii: Comparación con std ---------------------------------- \n")
#Señal estacionaria y ergódica: los promedios temporales y estadísticos son iguales
print("\nDesvíos estandar:")
std_signal_1 = np.std(signal_1)
std_signal_2 = np.std(signal_2)
std_sum = np.std(signal_sum)
std_diff = np.std(signal_diff)

print("Desvío estándar señal 1: ", std_signal_1)
print("Desvío estándar señal 2: ", std_signal_2)
print("Desvío estándar suma: ", std_sum)
print("Desvío estándar resta: ", std_diff)

