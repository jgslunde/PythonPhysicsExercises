import numpy as np
import matplotlib.pyplot as plt
def y(t,v0,m):
    g = 9.81
    return -g*.5*t**2 + v0*t
def v(t,v0,m):
    g = 9.81
    return -g*t + v0

def test_for_conservation(N,v0,m):
    g = 9.81
    T_max = v0/g
    N = 1000
    t1 = np.random.uniform(0,T_max,N)
    t2 =  np.random.uniform(0,T_max,N)
    energies_total1 = m*g*y(t1,v0,m)+.5*m*v(t1,v0,m)**2
    energies_total2 = m*g*y(t2,v0,m)+.5*m*v(t2,v0,m)**2
    success =  np.abs( energies_total2 - energies_total1) < 1e-10
    assert np.sum(success) > 0, "energy not conserved!"

m = 0.057
v0 = 17.
test_for_conservation(1000,v0,m)
