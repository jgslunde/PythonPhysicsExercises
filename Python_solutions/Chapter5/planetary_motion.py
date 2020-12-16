import numpy as np
import matplotlib.pyplot as plt

def r(theta, e, p):
    return p/(1+e*np.cos(theta))

# __Exercise a__
p = 1.0
theta = np.linspace(0, 2*np.pi, 100)
for e in [0, 0.5, 0.8]:
    radius = r(theta, e, p)
    plt.plot(theta, radius, label = 'e = %.1f' % e)
plt.xlabel('Angle [Radians]')
plt.ylabel('Distance from star [AU]')
plt.legend()
plt.savefig('fig_planetary_motion1.pdf')
plt.clf()

# __Exercse b__
p = 1.0
theta = np.linspace(0, 2*np.pi, 100)
for e in [0, 0.5, 0.8]:
    radius = r(theta, e, p)
    x = radius*np.sin(theta)
    y = radius*np.cos(theta)
    plt.plot(x, y, label ='e = %.1f' % e)
plt.plot(0, 0, 'yo')
plt.xlabel('Distance [AU]')
plt.ylabel('Distance [AU]')
plt.axis('equal')
plt.legend()
plt.savefig('fig_planetary_motion2.pdf')
plt.clf()
