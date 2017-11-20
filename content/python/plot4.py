import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
from uncertainties import ufloat
import scipy.constants as const

a, b, c = np.genfromtxt('content/values/Messwerte_4_links.txt', unpack=True)
a/=100
b/=1000
c/=1000

d= b-c
F=9.81*4.6937
L=0.565

E=4*a**3-12*L*a**2+9*L**2*a-L**3
print(a[0],a[len(a)-1])
print(E[0],E[len(E)-1])
def f(x, b):
    return x*b

parameters, pcov = curve_fit(f, E, d)
errors = np.sqrt(np.diag(pcov))
print(parameters[0], errors[0])
m = ufloat(parameters[0], errors[0])
print('Steigung m = {0:.8f}'.format(m),'1/(m^2)')
t= np.linspace(E[0],E[len(E)-1],5000)

plt.plot(t, f(t, *parameters), 'g-', label='Fit')
#plt.plot(E, b, 'rx', label='ohne Gewicht')
#plt.plot(E, c, 'bx', label='mit Gewicht')
plt.plot(E, d, 'gx', label='$ D(x) $')
#plt.errorbar(i, v ,xerr=2*e_i ,yerr=2*e_v, fmt='rx', label='U gegen I')
plt.xlabel(r'$ 3L^2x - 4x^3$ / $\text{m}^3$')
plt.ylabel(r'D(x)/$ m$')
plt.legend(loc='best')

plt.tight_layout()

plt.savefig('build/plot4.pdf')
I = const.pi * (0.005**4) / 4
print(I)
EM = F/(48*I*m)

print("Elastizitätmodul: {0:.2f}".format(EM), "N/m^2")
print("--------------------------------")
