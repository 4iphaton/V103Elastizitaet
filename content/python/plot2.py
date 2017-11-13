import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const

a, b, c = np.genfromtxt('content/values/Messwerte_3.txt', unpack=True)
a/=100
b/=1000
c/=1000

d= b-c
F=9.81*533.9
L=0.493


E=L*a**2-a**3/3

def f(x, y, b):
    return x*b+y
   # return x*b**2-b**3*y

parameters, pcov = curve_fit(f, E, d)

t= np.linspace(0,E[len(E)-1],5000)

plt.plot(t, f(t, *parameters), 'g-', label='Fit')
plt.plot(E, b, 'rx', label='Biegung ohne Gewicht')
plt.plot(E, c, 'bx', label='Biegung mit Gewicht')
plt.plot(E, d, 'gx', label='$ D(x) $')
#plt.errorbar(i, v ,xerr=2*e_i ,yerr=2*e_v, fmt='rx', label='U gegen I')
plt.xlabel(r'$ Lx^2 - \frac{x^3}{3}$ / $\text{m}^3$')
plt.ylabel(r'Auslenkung in $ m$')
plt.legend(loc='best')

plt.tight_layout()

plt.savefig('build/plot2.pdf')
