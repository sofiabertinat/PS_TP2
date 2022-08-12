#!/usr/bin/python
# coding=utf-8
import numpy                as     np
import matplotlib.pyplot    as     plt
from signals import espectro
import matplotlib.patches


#Dado el archivo clases/tp2/resolucion_espectral.txt que contiene 100 valores reales sampleados a Fs=200Hz, indique: 

fs = 200
N = 100

with open('resolucion_espectral.txt', 'r') as G:
    stxt = G.read()
    stxt = stxt.lstrip('[')
    stxt = stxt.rstrip(']\n')
    stxt = stxt.split(',')

x = np.array(stxt)
s = x.astype(np.float)

t = np.linspace(0, 1, N, endpoint=True)

plt.subplot(2,2,1)
plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal , fs='+str(fs)+'Hz, N='+str(N))
plt.plot(t,s,linewidth=2,alpha=0.5)

# 1) Resolución espectral. 
resolucionEspectral = fs/N
print("Resolucion espectral:")
print(resolucionEspectral)

# 2) Espectro en frecuencia de la señal. 
m1s = espectro(s, fs, N)
plt.subplot(2,2,2)
plt.xlabel('Frecuency') 
plt.ylabel('Density of spectral power') 
plt.plot(m1s[1], m1s[0],linewidth=1,alpha=0.5)

# 3) A simple inspección que frecuencia(s) distingue. 

# Se observan dos picos en frecuencia en 50HZ y -50 Hz.

# 4) Aplique alguna técnica que le permita mejorar la resolución espectral y tome nuevamente el espectro. 

# Para una dererminada fs, cuanto mas grande N mejor resolución espectral, elijo N = 200.

N2 = 200
resolucionEspectral2 = fs/N2
print("Resolucion espectral mejorada:")
print(resolucionEspectral2)

s0 = np.zeros((N2-N ,), dtype=float)
s2 = np.concatenate((s, s0))

t2 = np.linspace(0, 1, N2, endpoint=True)

plt.subplot(2,2,3)
plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal , fs='+str(fs)+'Hz, N='+str(N2))
plt.plot(t2,s2,linewidth=2,alpha=0.5)

ms2 = espectro(s2, fs, N2)

plt.subplot(2,2,4)
plt.xlabel('Frecuency') 
plt.ylabel('Density of spectral power,zero padding ') 
plt.plot(ms2[1], ms2[0],linewidth=1,alpha=0.5)
plt.show()

# 5) Indique si ahora los resultados difieren del punto 3 y argumente su respuesta

# Se necesitaron mas puntos en la DFT, pero la señal ya fue capturada, por lo que se rellena con ceros:zero padding
# Los resultados difieren, se mejoró la resolución espectral, obteniendo cuatro picos en frecuencia, esto no se veía anteriormente.
# Un efecto adverso es que la amplitud de la DFT se ve disminuida, esto se observa en la gráfica









