import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt

a, b, c = np.genfromtxt('content/values/Messwerte_2.txt', unpack=True)
# = np.genfromtxt('../../content/values/Differenz_2.txt', unpack=True)
d= b-c

F=9.81*1190.7
E_1=(49*0.01*(b*0.01)**2-(b*0.01)**3/3)*10**(-6)
#print(E_1)

s_1=np.mean(E_1)
#m_1=np.std(E_1)
print(s_1)

L=49
E=L*b**2-b**3/3

def f(x, y, b):
    return x*b+y
   # return x*b**2-b**3*y

parameters, pcov = curve_fit(f, E, d)
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')
t= np.linspace(0,80000,1000)

plt.plot(t, f(t, *parameters), 'g-', label='Fit')
#plt.plot(E, b, 'rx', label='Biegung ohne Gewicht')
#plt.plot(E, c, 'bx', label='Biegung mit Gewicht')
plt.plot(E, d, 'gx', label='$ D(x) $')
#plt.errorbar(i, v ,xerr=2*e_i ,yerr=2*e_v, fmt='rx', label='U gegen I')
plt.xlabel(r'$ Lx^2 - \frac{x^3}{3}$')
plt.ylabel(r'Auslenkung in $ 10 \mu m$')
plt.legend(loc='best')
plt.savefig('build/plot1.pdf')
