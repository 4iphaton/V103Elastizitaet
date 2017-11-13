import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c = np.genfromtxt('content/values/Messwerte_4_links.txt', unpack=True)
a/=100
b/=1000
c/=1000

d= b-c
F=9.81*4.6937
L=0.565
