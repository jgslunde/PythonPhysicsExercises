import numpy as np
import matplotlib.pyplot as plt

R = 0.75          # m

g = 9.81
omega = np.sqrt(g/R)
ph0 = np.pi/6

T = 1
t = np.linspace(0,T,1000)
th = ph0*np.cos(omega*t)

x = R*np.sin(th)
y = -R*np.cos(th)

plt.figure()
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Motion of pendelum during T = 1 seconds')
plt.savefig('fig_pendelum.pdf')
plt.show()
