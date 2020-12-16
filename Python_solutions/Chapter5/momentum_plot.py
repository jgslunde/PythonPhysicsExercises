import numpy as np
import matplotlib.pyplot as plt

c = 3e8
m = 5.0

def p_clas(v, m):
    return m*v

def p_rel(v, m):
    gamma = 1/(1-(v**2/c**2))
    return m*v*gamma

v = np.linspace(0, 0.9*c, 1001)

plt.plot(v, p_clas(v, m))
plt.plot(v, p_rel(v, m))
plt.legend(["Classic Momentum", "Relativistic Momentum"])
plt.xlabel("Velocity [m/s]")
plt.ylabel("Momentum [kgm/s]")
plt.savefig("fig_momentum_plot.pdf")
