from ctypes import sizeof
import numpy   as     np
from scipy import signal
import matplotlib.pyplot    as     plt
from   matplotlib.animation import FuncAnimation
np.set_printoptions(precision=3, suppress=False)

#En el archivo clases/tp2/ﬀt_hjs.npy se almacenaron los valores de un espectro en frecuencia correspondientes a una señal desconocida. Indique:

p = np.load("fft_hjs.npy")

# 1) ¿Puede estimar que representa esta señal? (tip: grafique en 2d la idft) 

fftDataShifted = np.fft.fftshift(p)
ifftData= np.fft.ifft(p)
N = len(ifftData)
nData  = np.arange(-N/2,N/2,1)
t = np.linspace(0,1,N)

plt.subplot(3,3,1)
plt.title('Señal FFT shifted')
plt.plot(nData,fftDataShifted,'b-o',linewidth=1,alpha=0.5)

plt.subplot(3,3,2)
plt.title('Señal ')
plt.plot(t,np.real(ifftData),'b-o',linewidth=4,alpha=0.5,label="real")
plt.plot(t,np.imag(ifftData),'r-o',linewidth=4,alpha=0.5,label="imag")

plt.subplot(3,3,3)
plt.title('Antitrasnformada IDFT, N='+str(N))
plt.xlim(-0.7, 1.1)
plt.plot(np.imag(ifftData), np.real(ifftData),'b-o',linewidth=4,alpha=0.5)

N2 = 500
fftDataShifted2 = fftDataShifted[N2/2:N-N2/2]
ifftData2= np.fft.ifft(np.fft.ifftshift(fftDataShifted2))
nData2 = np.arange(-N2/2,N2/2,1)
t2 = np.linspace(0,1,len(ifftData2))

plt.subplot(3,3,4)
plt.title('Señal FFT shitfed')
plt.plot(nData2,fftDataShifted2 ,'b-o',linewidth=1,alpha=0.5)

plt.subplot(3,3,5)
plt.title('Señal ')
plt.plot(t2,np.real(ifftData2),'b-o',linewidth=4,alpha=0.5,label="real")
plt.plot(t2,np.imag(ifftData2),'r-o',linewidth=4,alpha=0.5,label="imag")

plt.subplot(3,3,6)
plt.title('Antitrasnformada IDFT, N='+str(len(ifftData2)))
plt.plot(np.imag(ifftData2), np.real(ifftData2),'b-o',linewidth=4,alpha=0.5)

N3 = 499
fftDataShifted3 = fftDataShifted[N2/2:N-N2/2-1]
ifftData3= np.fft.ifft(np.fft.ifftshift(fftDataShifted3))
nData3 = np.arange(-N2/2,N2/2-1,1)
t3 = np.linspace(0,1,len(ifftData3))

plt.subplot(3,3,7)
plt.title('Señal FFT shitfed')
plt.plot(nData3,fftDataShifted3 ,'b-o',linewidth=1,alpha=0.5)

plt.subplot(3,3,8)
plt.title('Señal ')
plt.plot(t3,np.real(ifftData3),'b-o',linewidth=4,alpha=0.5,label="real")
plt.plot(t3,np.imag(ifftData3),'r-o',linewidth=4,alpha=0.5,label="imag")

plt.subplot(3,3,9)
plt.title('Antitrasnformada IDFT, N='+str(len(ifftData3)))
plt.plot(np.imag(ifftData3), np.real(ifftData3),'b-o',linewidth=4,alpha=0.5)
plt.show()

# 2) Hasta qué punto podría limitar el ancho de banda del espectro dado en el archivo y que aún se logre interpretar la señal? 

# Se puede observar d ela gráfica de la fft shifted que la información se encuentra consentrada en las bajas frecuencias.
# Entonces eliminando las muestras correspondientes con las altas frecuencias podemos seguir distinguiendo la imágen de Homero.
# Como se observa el límite esta en tomar 500 muestras correspondientes al rango de frecuencias bajas.
