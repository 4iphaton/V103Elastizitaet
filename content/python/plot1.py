import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c = np.genfromtxt('content/values/Messwerte_2.txt', unpack=True)
l_e, b_e, h_e, m_e =np.genfromtxt('content/values/stab_eckig_einseitig.txt', unpack=True)
# = np.genfromtxt('../../content/values/Differenz_2.txt', unpack=True)
a= a*10**(-2) #m
b = b*10**(-3)
c = c*10**(-3)
d= b-c  #m
L= 49.3*10**(-2) #m
l_e = l_e* 10**(-2)
b_e = b_e* 10**(-2)
h_e = h_e* 10**(-2)
m_e = 1193.2* 10**(-3)

x_ap= L*a**2 - a**3/3 #m
y_ap= d               #m

def f(x, b, y):
    return x*b+y

parameters, pcov = curve_fit(f, x_ap, y_ap)
print("a1", parameters)
print("b2", np.sqrt(np.diag(pcov)), sep='\n')
t= np.linspace(0,0.08,1000)


plt.plot(t, f(t, *parameters), 'g-', label='Fit')
plt.plot(x_ap, b, 'rx', label='ohne Gewicht')
plt.plot(x_ap, c, 'bx', label='mit Gewicht')
plt.plot(x_ap, y_ap, 'gx', label='$ D(x) $')
#plt.errorbar(i, v ,xerr=2*e_i ,yerr=2*e_v, fmt='rx', label='U gegen I')
plt.xlabel(r'$ Lx^2 - \frac{x^3}{3} \ / \ \text{m}^3$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')
#eckig

I= ((b_e*h_e)/12)*(b_e**2 + h_e**2)
print("Traegheitsmoment1:",I)
g= 9.81
F = m_e*g
fehl = np.sqrt(np.diag(pcov))
m = ufloat(parameters[0], fehl[0])
print(m)
print(F)
E_1= F/((2*I)*m)
print("Elastizitaetsmodul11", E_1)
print("-------------------------------")
