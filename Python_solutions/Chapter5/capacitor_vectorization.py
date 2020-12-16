import numpy as np
import matplotlib.pyplot as plt

def I(t, R, C, V0):
    return C*V0*np.exp(-t/(R*C))

V0 = 50.0
R = 350.0
C = 0.007

t = 10
n = 1000
dt = float(t)/n

t_array = np.linspace(0, t, n)
I_array = I(t_array, R, C, V0)

plt.plot(t_array, I_array)
plt.savefig('fig_capacitor_vectorization.pdf')
