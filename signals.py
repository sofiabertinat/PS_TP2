import numpy   as     np
from scipy import signal
import matplotlib.pyplot    as     plt
from   matplotlib.animation import FuncAnimation
np.set_printoptions(precision=3, suppress=False)

# Sintetizar senales senoidal, cuadrada y triangular
# Frecuencia de muestreo: fs  (HZ)
# Frecuencia: f0 (HZ)
# Fase en radianes: fase
# Amplitud: amp = [0,1]
# cantidad de muestras: N 

#generators con funciones
def signalSine(fs,f0, amp, N, fase):    
    i = 0    
    # inicializo array
    s = np.zeros((N ,), dtype=float)
    m = np.empty((2,N), float)
    # linspace asegura la cantidad de valores (inicio, parada, cantidad de puntos)
    t = np.linspace(0, 1, N, endpoint=True)
    for  i in range(N):
        s[i] = amp * np.sin(2*np.pi*fs*t[i]*1/f0 + fase) 
        i+=1    
    m[0] = np.transpose(s)
    m[1] = t   
    return m

def signalSquare(fs,f0, amp, N):
    i = 0    
    # inicializo array
    s = np.zeros((N ,), dtype=float)
    m = np.empty((2,N), float)
    # linspace asegura la cantidad de valores (inicio, parada, cantidad de puntos)
    t = np.linspace(0, 1, N, endpoint=True)
    for  i in range(N):
        s[i] = amp * signal.square(2*np.pi*fs*t[i]*1/f0)
        i+=1
    m[0] = np.transpose(s)
    m[1] = t    
    return m

def signalSawtooth(fs,f0, amp, N):
    i = 0
    # inicializo array
    s = np.zeros((N ,), dtype=float)
    m = np.empty((2,N), float)
    # linspace asegura la cantidad de valores (inicio, parada, cantidad de puntos)
    t = np.linspace(0, 1, N, endpoint=True)
    for  i in range(N):
        s[i] = amp * signal.sawtooth(2*np.pi*fs*t[i]*1/f0)
        i+=1
    m[0] = np.transpose(s)
    m[1] = t    
    return m

def signalDelta(N):   
    # inicializo array
    s = np.zeros((N ,), dtype=float)
    m = np.empty((2,N), float)
    # linspace asegura la cantidad de valores (inicio, parada, cantidad de puntos)
    t = np.linspace(0, 1, N, endpoint=True)
    s[0] = 1     
    m[0] = np.transpose(s)
    m[1] = t    
    return m

def potenciaPromedio(s, N):
    i = 0
    sum = 0
    for  i in range(N):
        sum = sum + s[i]**2
    p = round(sum/N, 3)
    return p

def espectro(s, fs, N):
    m = np.empty((2,N), float)
    nData  = np.arange(0,N,1) 
    fData  = nData*(fs/N)-fs/2
    arrayS = np.array(s)
    fftS = np.fft.fft(arrayS )
    fftS = np.fft.fftshift(fftS)
    spS = np.abs(fftS/N)**2  
    m[0] = spS
    m[1] = fData    
    return m