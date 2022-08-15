from ctypes import sizeof
import numpy   as     np
from scipy import signal
import matplotlib.pyplot    as     plt
from   matplotlib.animation import FuncAnimation
np.set_printoptions(precision=3, suppress=False)
import scipy.signal as sc
import simpleaudio as sa

#Dado el segmento de audio almacenado en el archivo clases/tp2/chapu_noise.npy 
#con Fs=8000, mono de 16b y contaminado con ruido de alta frecuencia: 

fs = 8000 
p1 = np.load("chapu_noise.npy")
N1 = len(p1)

#1) Diseñe un ﬁltro que mitigue el efecto del ruido y permita percibir mejor la señal de interés 
#2) Filtre con la CIAA utilizando alguna de las técnicas vistas 
#3) Graﬁque el espectro antes y después del ﬁltro. 
#4) Reproduzca el audio antes y después del filtro 

nData1  = np.arange(0,N1,1) 
fData1  = nData1*(fs/N1)-fs/2
arrayp1 = np.array(p1)
fft1 = np.fft.fft(arrayp1)    
fft1 = np.fft.fftshift(fft1)
sp1 = np.abs(fft1/N1)**2 
plt.title('Espectro audio original, N='+str(N1))
plt.xlabel('Frecuency') 
plt.ylabel('Density of spectral power') 
plt.plot(fData1, sp1,linewidth=1,alpha=0.5)
plt.show()

for i in range(1000):
    play_obj = sa.play_buffer(p1, 1, 2, fs)
    play_obj.wait_done()

