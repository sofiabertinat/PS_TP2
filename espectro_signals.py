#!/usr/bin/python
# coding=utf-8
import numpy                as     np
import matplotlib.pyplot    as     plt
from signals import signalSine, signalSquare, signalSawtooth, signalDelta, potenciaPromedio, espectro
import matplotlib.patches

#Graﬁque las siguientes senales lado a lado con su respectivo espectro en frecuencias:  1) Senoidal. 2) Cuadrada. 3) Triangular 4) Delta en t=0. 
#Indicando en cada caso los siguientes parámetros (si corresponde):Frecuencia, Amplitud, Potencia promedio, Fs, N. 

fs = 1000
N = 1000            
f01 = 0.1 * fs
fase = 0
amp = 1 

plt.subplot(4,2,1)
m1 = signalSine(fs,f01, amp, N, fase)
p1 = potenciaPromedio(m1[0], N)
plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal sine, fs='+str(fs)+'Hz, N='+str(N)+', f='+str(f01)+'Hz, Potencia promedio = '+str(p1)+'W')
plt.ylim(-1.01, 1.01)
plt.plot(m1[1],m1[0],linewidth=2,alpha=0.5)

plt. subplot(4,2,2)
m1s = espectro(m1[0], fs, N)
plt.xlabel('Frecuency') 
plt.ylabel('Density of spectral power') 
plt.xlim(-50, 50)
plt.ylim(0, 0.26)
plt.plot(m1s[1], m1s[0],linewidth=2,alpha=0.5)

plt.subplot(4,2,3)
m2 = signalSquare(fs,f01, amp, N)
p2 = potenciaPromedio(m2[0], N)
plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal Square, fs='+str(fs)+'Hz, N='+str(N)+', f='+str(f01)+'Hz, Potencia promedio = '+str(p2)+'W')
plt.ylim(-1.05, 1.05)
plt.plot(m2[1],m2[0],linewidth=2,alpha=0.5)

plt. subplot(4,2,4)
m2s = espectro(m2[0], fs, N)
plt.xlabel('Frecuency') 
plt.ylabel('Density of spectral power') 
plt.xlim(-210, 210)
plt.ylim(-0.0001, 0.43)
plt.plot(m2s[1], m2s[0],linewidth=2,alpha=0.5)

plt.subplot(4,2,5)
m3 = signalSawtooth(fs,f01, amp, N)
p3 = potenciaPromedio(m3[0], N)
plt.xlabel('Time') 
plt.ylabel('Amplitude')
plt.title('Signal Sawtooth, fs='+str(fs)+'Hz, N='+str(N)+', f='+str(f01)+'Hz, Potencia promedio = '+str(p3)+'W')
plt.ylim(-1.05, 1.05)
plt.plot(m3[1],m3[0], linewidth=2,alpha=0.5)

plt. subplot(4,2,6)
m3s = espectro(m3[0], fs, N)
plt.xlabel('Frecuency') 
plt.ylabel('Density of spectral power') 
plt.xlim(-200, 200)
plt.ylim(-0.001, 0.11)
plt.plot(m3s[1], m3s[0],linewidth=2,alpha=0.5)

plt.subplot(4,2,7)
m4 = signalDelta(N)
p4 = potenciaPromedio(m4[0], N)
plt.xlabel('Time') 
plt.ylabel('Amplitude')
plt.title('Signal Delta en t=0, N='+str(N)+', Potencia promedio = '+str(p4)+'W')
plt.xlim(-0.02, 1)
plt.ylim(-0.01, 1.1)
plt.plot(m4[1],m4[0],linewidth=2,alpha=0.5)

plt. subplot(4,2,8)
m4s = espectro(m4[0], fs, N)
plt.xlabel('Frecuency') 
plt.ylabel('Density of spectral power') 
plt.plot(m4s[1], m4s[0],linewidth=2,alpha=0.5)
plt.ylim(-0.000002, 0.000002)
plt.show()



