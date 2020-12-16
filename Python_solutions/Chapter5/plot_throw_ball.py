
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
v0 = 16
for alpha in [np.pi/6,np.pi/4,np.pi/3]:
    t = np.linspace(0,3.5/(v0*np.cos(alpha)))
    y = -.5*g*t**2 + v0*t*np.sin(alpha)
    x = v0*t*np.cos(alpha)
    plt.plot(x,y)

plt.legend(['pi/6','pi/4','pi/3'])
plt.show()
