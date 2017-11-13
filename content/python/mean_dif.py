import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
import math

D_2 = np.genfromtxt('../../content/values/Differenz_2.txt',unpack=True)
D_3 = np.genfromtxt('../../content/values/Differenz_3.txt',unpack=True)
D_4r = np.genfromtxt('../../content/values/Differenz_4_links.txt',unpack=True)
D_4l = np.genfromtxt('../../content/values/Differenz_4_rechts.txt',unpack=True)



#n = len(h_kein) # Alle Arrays haben dieselbe laenge

#berechnen der Minima bzw Maxima
_D_2 = np.mean(D_2)
print (_D_2)
_D_3 = np.mean(D_3)
print (_D_3)
_D_4r = np.mean(D_4r)
print (_D_4r)
_D_4l = np.mean(D_4l)
print (_D_4l)
