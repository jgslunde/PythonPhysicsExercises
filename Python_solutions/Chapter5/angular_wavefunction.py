import matplotlib.pyplot as plt
import numpy as np

def P20(th):
    return .5*(3*np.cos(th)**2 - 1)
def P21(th):
    return 3*np.sin(th)*np.cos(th)
def P22(th):
    return 3*np.sin(th)**2

th = np.linspace(0,np.pi,1000)

for function in [P20,P21,P22]:
    r = np.abs(function(th))
    a = r*np.sin(th)
    b = r*np.cos(th)

    plt.figure()
    plt.plot(a ,b,'b',-a,b,'b')

plt.show()
