
'''

4.c. Defina los vectores necesarios para representar alrededor de 100 ciclos de 2 señales 
senoidales de amplitud unitaria, de la misma frecuencia, pero distinta fase.  
i. Explore cómo cambia la coherencia entre las 2 señales al ir cambiando la fase 
de una de ellas entre 0 y 90 grados.  

'''

import numpy as np
import matplotlib.pyplot as plt
from math import pi

print("\n ----- EJERCICIO 4.c. --------------------------------------------------------- \n")

ciclos = 10

#amplitudes
amp = 1
#frecuencias
f1 = 1
w1 = 2*pi*f1
#desfase
ø1 = 0
ø2 = pi/4

#muestreo
f_sampling = f1*20
T_sampling = 1/f_sampling
sampling_time = np.arange(0, ciclos/f1, T_sampling) #sampleo 100 ciclos

#genero vectores de amplitud para signal 1 y 2
signal_1 = amp*np.sin(w1*sampling_time + ø1)
signal_2 = amp*np.sin(w1*sampling_time + ø2)

#visualización de señales
plt.plot(signal_1, signal_2, label='Coherencia')
#plt.plot(sampling_time, signal_2, label='Signal 2')
#plt.xlabel("Tiempo [s]")
#plt.ylabel("Amplitud [V]")
plt.legend()
#plt.grid()
plt.show()

print("\n ----- EJERCICIO 4.c.i.: coherencia de señales -------------------------------- \n")

