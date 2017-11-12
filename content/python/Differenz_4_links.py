import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
import math

x, h_kein , h_Gew = np.genfromtxt('../../content/values/Messwerte_4_links.txt',unpack=True)

print(x,h_kein,h_Gew)

#n = len(h_kein) # Alle Arrays haben dieselbe laenge

#berechnen der Minima bzw Maxima
D = h_kein - h_Gew
print (D)
