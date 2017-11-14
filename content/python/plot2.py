import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
import math

a, b, c = np.genfromtxt('content/values/Messwerte_3.txt', unpack=True)
a/=100
b/=1000
c/=1000

d= b-c
F=9.81*0.5339
L=0.508


E=L*a**2-a**3/3
print(a[0],a[len(a)-1])
print(E[0],E[len(E)-1])

def f(x, b, y):
    return x*b+y
   # return x*b**2-b**3*y

parameters, pcov = curve_fit(f, E, d)
errors = np.sqrt(np.diag(pcov))
print( "a2:", parameters[0], errors[0])
print( "b2:", parameters[1], errors[1])
m = ufloat(parameters[0], errors[0])
print('Steigung m = {0:.8f}'.format(m),'1/(m^2)')

t= np.linspace(0,E[len(E)-1],5000)

plt.plot(t, f(t, *parameters), 'g-', label='Fit')
plt.plot(E, b, 'rx', label='ohne Gewicht')
plt.plot(E, c, 'bx', label='mit Gewicht')
plt.plot(E, d, 'gx', label='$ D(x) $')
#plt.errorbar(i, v ,xerr=2*e_i ,yerr=2*e_v, fmt='rx', label='U gegen I')
plt.xlabel(r'$ Lx^2 - \frac{x^3}{3}$ / $\text{m}^3$')
plt.ylabel(r'Auslenkung in $ m$')
plt.legend(loc='best')

plt.tight_layout()

plt.savefig('build/plot2.pdf')

I = const.pi * (0.005**4) / 2
print("Traegheitsmoment2:", I)
EM = F/(2*I*m)

print("Elastizitätmodul3: {0:.2f}".format(EM), "N/m^2")
print("-------------------------------")
