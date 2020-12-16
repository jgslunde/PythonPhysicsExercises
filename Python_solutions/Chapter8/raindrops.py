from random import uniform
from math import sqrt
import numpy as np
import time

C = 0.47
rho_w = 1000    # kg/m^3
rho = 1.293       # kg/m^3
g = 9.81

N = 100000

# a)
avg_vT = 0

time_start = time.time()
for i in range(N):
    r = uniform(0.001,0.006)
    vT_tmp = sqrt((8.*rho_w*r*g)/(3*rho*C))
    avg_vT += vT_tmp/N

time_used = time.time() - time_start
print "Average vT = %g m/s"%avg_vT
print "Time used w/o numpy: %g seconds"%time_used

# b)
time_start = time.time()
r = np.random.uniform(0.001,0.006,N)
avg_vT = np.sum(np.sqrt((8.*rho_w*r*g)/(3*rho*C)))/N
time_used = time.time() - time_start
print "Average vT = %g m/s"%avg_vT
print "Time used with numpy: %g seconds"%time_used
