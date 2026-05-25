'''
Dada la señal periódica de la figura con T2=2.T1, calcular: 
-A < V < 0,5A (amplitudes en V)

a. el valor medio. 
Respuesta: -A/2

b. La potencia normalizada. 
Respuesta: sqrt(3/4 * A^2

c. su valor eficaz de alterna. 
Respuesta: A/sqrt(2) 

d. Compruebe la relación existente entre las 3 cantidades. 
Respuesta: A realizar por el alumno. 
e. Dibuje la función de densidad de probabilidad acumulada, F(x). 
Respuesta: A realizar por el alumno 
'''

import numpy as np
import math
import matplotlib.pyplot as plt

# --- Parametros generales
# tiempo
T1 = 1/3
T2 = 2*T1
T = T1 + T2
f_signal = 1/T

# amplitud
A = 1
positive =A*0.5
negative = -A 

#muestreo
ciclos = 3
f_sampling = f_signal*100
T_sampling = 1/f_sampling
sampling_time = np.arange(0, ciclos*T, T_sampling)


#generacion de señal
signal = []

for i in range(len(sampling_time)):
    if sampling_time[i] % T < T1:
        signal.append(positive)
    else:
        signal.append(negative)

signal = np.array(signal)

#imprimir datos
print("\n ----- EJERCICIO 1.a., 1.b. y 1.c. -------------------------------------------------- \n")

Vmean = np.mean(signal)
print("Vmed: ", Vmean)
print("Vmed teórico: ", -A/2)

Vrms = np.sqrt(np.mean(signal**2))
print("Vrms: ", Vrms)
print("Vrms teórico: ", np.sqrt(3/4 * A**2))

Vrms_ac = np.std(signal)
print("Vrms_ac: ", Vrms_ac)
print("Vrms_ac teórico: ", A/np.sqrt(2))

#graficas
plt.plot(sampling_time,signal)
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.show()

print("\n ----- EJERCICIO 1.e. --------------------------------------------------------------- \n")



fig, ax = plt.subplots(2, 1)
# ----- PDF -----
ax[0].hist(signal, 100, density=True, edgecolor='black', linewidth=.5)
ax[0].set_xlabel("Amplitud [V]")
ax[0].set_ylabel("Densidad")


# ----- CDF -----
sorted_signal = np.sort(signal)
cdf = np.arange(1, len(sorted_signal)+1) / len(sorted_signal)

ax[1].plot(sorted_signal, cdf)
ax[1].set_xlabel("Amplitud [V]")
ax[1].set_ylabel("F(x)")

plt.tight_layout()
plt.show()


