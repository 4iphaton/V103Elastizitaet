import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c = np.genfromtxt('content/values/Messwerte_4_rechts.txt', unpack=True)
