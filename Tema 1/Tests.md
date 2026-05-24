# Pruebas ejecutadas

### Objetivo
Ejecutar y mostrar pruebas realizadas para mejorar el entendimiento de los ejercicios.

## Ejercicio 4.c.
### | Prueba №1
```text
f1 = 1
f2 = 1
ø1 = 0
ø2 = 0
f_sampling = max(f1,f2)*20

Señales SIN ruido
```

![Señales en t](<../pics/1. f1=f2, fs=x20, ø1=ø2, noise=0 signals.png>)


![Coherencia](<../pics/1. f1=f2, fs=x20, ø1=ø2, noise=0 coherence.png>)

La coherencia es alta, en todo el espectro

### | Prueba №2
```text
f1 = 1
f2 = 1.5
ø1 = 0
ø2 = 0
f_sampling = max(f1,f2)*20

Señales SIN ruido
```
![Señales en t](<../pics/2. f1=1, f2=1.5, fs=x20, ø1=ø2, noise=0 signals.png>)


![Coherencia](<../pics/2. f1=1, f2=1.5, fs=x20, ø1=ø2, noise=0 coherence.png>)

Aquí, para mi, la señal de coherencia no tiene sentido.


### | Prueba №3
```text
f1 = 1
f2 = 1
ø1 = 0
ø2 = 0
f_sampling = max(f1,f2)*20

Señales CON ruido de 5% de amplitud
```
![Señales en t](<../pics/4. f1=f2, fs=x20, ø1=ø2, noise=0.05 signals.png>)


![Coherencia](<../pics/3. f1=f2, fs=x20, ø1=ø2, noise=0.05 coherence.png>)

Aquí, para mi, la señal de coherencia no tiene sentido. Creo que el ruido se mezcla con la señal de muestreo, y por eso hay tantas "frecuencias con coherencia".

### | Prueba №4
```text
f1 = 1
f2 = 1
ø1 = 0
ø2 = 0
f_sampling = max(f1,f2)*100

Señales CON ruido de 5% de amplitud
```
![Señales en t](<../pics/4. f1=f2, fs=x100, ø1=ø2, noise=0.05 signals.png>)

![Coherencia](<../pics/4. f1=f2, fs=x100, ø1=ø2, noise=0.05 coherence.png>)

La coherencia aumenta considerablemente en la frecuencia de la señal, disminuyendo en las frecuencias lejanas.

### | Prueba №5
```text
f1 = 1
f2 = 2
ø1 = 0
ø2 = 0
f_sampling = max(f1,f2)*100

Señales CON ruido de 5% de amplitud
```
![Señales en t](<../pics/5. f1=1, f2=2, fs=x50, ø1=ø2, noise=0.05 signals.png>)

![Coherencia](<../pics/5. f1=1, f2=2, fs=x50, ø1=ø2, noise=0.05 coherence.png>)

Señales sin coherencia.


## Otros
- Estado: pendiente / completado
- Fecha: YYYY-MM-DD
- Autor: Nombre
- Referencias: enlaces o archivos relacionados
